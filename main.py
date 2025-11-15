import asyncio
import json
from contextlib import redirect_stdout
from io import StringIO
from typing import Any, Callable, TypedDict

import pandas as pd
from anthropic import AsyncAnthropic
from anthropic.types import MessageParam, ToolUnionParam
import os

from generate_gt_data import generate_test_data
api_key = os.getenv("ANTHROPIC_API_KEY_PERSONAL")
if api_key is None:
    raise ValueError("ANTHROPIC_API_KEY_PERSONAL is not set")

class PythonExpressionToolResult(TypedDict):
    result: Any
    error: str | None


class SubmitAnswerToolResult(TypedDict):
    answer: Any
    submitted: bool


def python_expression_tool(expression: str) -> PythonExpressionToolResult:
    """
    Tool that evaluates Python expressions using exec.
    Use print(...) to emit output; stdout will be captured and returned.
    """
    try:
        namespace = {}
        stdout = StringIO()
        with redirect_stdout(stdout):
            exec(expression, namespace, namespace)
        return {"result": stdout.getvalue(), "error": None}
    except KeyboardInterrupt:
        raise
    except Exception as e:
        return {"result": None, "error": str(e)}


def submit_answer_tool(answer: Any) -> SubmitAnswerToolResult:
    """
    Tool for submitting the final answer.
    """
    return {"answer": answer, "submitted": True}


async def run_agent_loop(
    prompt: str,
    tools: list[ToolUnionParam],
    tool_handlers: dict[str, Callable[..., Any]],
    max_steps: int = 20,
    model: str = "claude-3-5-haiku-latest",
    verbose: bool = True,
) -> Any | None:
    """
    Runs an agent loop with the given prompt and tools.

    Args:
        prompt: The initial prompt for the agent
        tools: List of tool definitions for Anthropic API
        tool_handlers: Dictionary mapping tool names to their handler functions
        max_steps: Maximum number of steps before stopping (default 5)
        model: The Anthropic model to use
        verbose: Whether to print detailed output (default True)

    Returns:
        The submitted answer if submit_answer was called, otherwise None
    """
    client = AsyncAnthropic(api_key=api_key)
    messages: list[MessageParam] = [{"role": "user", "content": prompt}]

    for step in range(max_steps):
        if verbose:
            print(f"\n=== Step {step + 1}/{max_steps} ===")

        response = await client.messages.create(
            model=model, max_tokens=4096, tools=tools, messages=messages
        )

        # Track if we need to continue
        has_tool_use = False
        tool_results = []
        submitted_answer = None

        # Process the response
        for content in response.content:
            if content.type == "text":
                if verbose:
                    print(f"Assistant: {content.text}")
            elif content.type == "tool_use":
                has_tool_use = True
                tool_name = content.name

                if tool_name in tool_handlers:
                    if verbose:
                        print(f"Using tool: {tool_name}")

                    # Extract arguments based on tool
                    handler = tool_handlers[tool_name]
                    tool_input = content.input

                    # Call the appropriate tool handler
                    if tool_name == "python_expression":
                        if not (isinstance(tool_input, dict) and "expression" in tool_input):
                            print(f"ERROR: Invalid tool_input for python_expression: {tool_input}")
                            result = {"result": None, "error": "Invalid tool input"}
                        else:
                            if verbose:
                                print("\nInput:")
                                print("```")
                                for line in tool_input["expression"].split("\n"):
                                    print(f"{line}")
                                print("```")
                            result = handler(tool_input["expression"])
                            if verbose:
                                print("\nOutput:")
                                print("```")
                                print(result)
                                print("```")
                    elif tool_name == "submit_answer":
                        if not (isinstance(tool_input, dict) and "answer" in tool_input):
                            print(f"ERROR: Invalid tool_input for submit_answer: {tool_input}")
                            print(f"Type: {type(tool_input)}")
                            result = {"answer": None, "submitted": False}
                        else:
                            result = handler(tool_input["answer"])
                            submitted_answer = result["answer"]
                    else:
                        # Generic handler call
                        result = (
                            handler(**tool_input)
                            if isinstance(tool_input, dict)
                            else handler(tool_input)
                        )

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": content.id,
                            "content": json.dumps(result),
                        }
                    )

        # If we have tool uses, add them to the conversation
        if has_tool_use:
            messages.append({"role": "assistant", "content": response.content})

            messages.append({"role": "user", "content": tool_results})

            # If an answer was submitted, return it
            if submitted_answer is not None:
                if verbose:
                    print(f"\nAgent submitted answer: {submitted_answer}")
                return submitted_answer
        else:
            # No tool use, conversation might be complete
            if verbose:
                print("\nNo tool use in response, ending loop.")
            break

    if verbose:
        print(f"\nReached maximum steps ({max_steps}) without submitting answer.")
    return None


async def run_single_test(
    run_id: int,
    num_runs: int,
    prompt_template: str,
    tools: list[ToolUnionParam],
    tool_handlers: dict[str, Callable[..., Any]],
    verbose: bool = False,
) -> tuple[int, bool, Any]:
    if verbose:
        print(f"\n\n{'=' * 20} RUN {run_id}/{num_runs} {'=' * 20}")

    # Generate fresh data for this test run
    display_csv, expected_answer = generate_test_data()

    # Fill in the prompt template
    prompt = prompt_template.format(display_csv_raw=display_csv)

    result = await run_agent_loop(
        prompt=prompt,
        tools=tools,
        tool_handlers=tool_handlers,
        max_steps=5,
        verbose=verbose,
    )

    # Normalize whitespace for comparison
    result_normalized = result.strip() if isinstance(result, str) else result
    expected_normalized = expected_answer.strip() if isinstance(expected_answer, str) else expected_answer

    success = result_normalized == expected_normalized

    if success:
        print(f"✓ Run {run_id}: SUCCESS")
    else:
        print(f"✗ Run {run_id}: FAILURE")
        if isinstance(result, str) and isinstance(expected_answer, str):
            result_lines = result_normalized.split('\n')
            expected_lines = expected_normalized.split('\n')
            original_lines = display_csv.strip().split('\n')
            print(f"  Got {len(result_lines)} lines, expected {len(expected_lines)} lines")

            # Show line-by-line differences
            for i, (got, exp) in enumerate(zip(result_lines, expected_lines)):
                if got != exp:
                    print(f"  Line {i+1} differs:")
                    # Show original if available (skip header)
                    if i > 0 and i < len(original_lines):
                        print(f"    Original: {original_lines[i]}")
                    print(f"    Expected: {exp}")
                    print(f"    Got:      {got}\n")

            # Show extra or missing lines
            if len(result_lines) > len(expected_lines):
                print(f"  Extra lines in result:")
                for line in result_lines[len(expected_lines):]:
                    print(f"    {line}")
            elif len(result_lines) < len(expected_lines):
                print(f"  Missing lines in result:")
                for line in expected_lines[len(result_lines):]:
                    print(f"    {line}")
        else:
            print(f"  Got: {result}")
            print(f"  Expected: {expected_answer}")

    return run_id, success, result


async def main(concurrent: bool = True):
    # Prompt template - data will be filled in for each test run
    prompt_template = """You are given noisy customer data in CSV format that needs to be parsed and cleaned.

Here is the input CSV:
{display_csv_raw}

Parse and clean this data. Output a CSV with these exact columns in this order:
first_name,last_name,phone_num,email,street_address,city,state,zip_code

Rules:
- first_name: title case
- last_name: title case
- phone_num: format XXX-XXX-XXXX (remove any extra digits)
- email: do not change the original email address, just fix formatting issues (like double @ or missing dots between domain parts)
- street_address: (number + street name + type) (e.g. 123 Main Street)
- city: city name (title case)
- state: full state name (title case)
- zip_code: 5-digit zip code
- If there is nothing for that field in the original data, leave it empty.

Output ONLY the CSV with header row and data rows. No extra text or explanation.
Submit your answer using the submit_answer tool."""

    tools: list[ToolUnionParam] = [
        {
            "name": "submit_answer",
            "description": "Submit the final answer as a CSV string",
            "input_schema": {
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "string",
                        "description": "The cleaned CSV data as a string"
                    }
                },
                "required": ["answer"],
            },
        },
    ]

    tool_handlers = {
        "submit_answer": submit_answer_tool,
    }

    num_runs = 5

    execution_mode = "concurrently" if concurrent else "sequentially"
    print(f"Running {num_runs} test iterations {execution_mode}...")
    print("=" * 60)

    # Create all test coroutines
    tasks = [
        run_single_test(
            run_id=i + 1,
            num_runs=num_runs,
            prompt_template=prompt_template,
            tools=tools,
            tool_handlers=tool_handlers,
            verbose=False,
        )
        for i in range(num_runs)
    ]

    # Run concurrently or sequentially based on the flag
    if concurrent:
        # Process results as they complete
        results = []
        for coro in asyncio.as_completed(tasks):
            result = await coro
            results.append(result)
    else:
        # Run sequentially by awaiting each task in order
        results = []
        for task in tasks:
            result = await task
            results.append(result)

    # Count successes
    successes = sum(1 for _, success, _ in results if success)

    # Calculate and display pass rate
    pass_rate = (successes / num_runs) * 100
    print(f"\n{'=' * 60}")
    print("Test Results:")
    print(f"  Passed: {successes}/{num_runs}")
    print(f"  Failed: {num_runs - successes}/{num_runs}")
    print(f"  Pass Rate: {pass_rate:.1f}%")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    # Set to True for concurrent execution, False for sequential execution
    asyncio.run(main(concurrent=True))
