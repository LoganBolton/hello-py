hello-py
===

# Take-home Summary

One pain I've run into when using LLMs for data cleaning is that they will frequently hallucinate details that seem reasonable, but do not exist in the original data. To help prevent this, I made an environment where the model has to take semi-structured noisy data and convert it into clean, structured data. 

For my ground truth dataset, I synthetically generate a csv file with plausible looking customer information. Then, I purposelly add noise to the data with repeated fields, obvious typos, etc. The model's job is to take the noisy data and put it into a clean format, _without_ hallucinating any new information. 

## Code Overview

_n_ rows of unique data are generated for each run through the `generate_gt_data.py` file. 

To control the amount of noise in the data, adjust the `noise_odds` or `dropout_odds` arguments in `run_single_test()`. These variables control the probability that a field has noise applied or is removed entirely. 

## Example Failure cases 

A frequent mistake that occures is that the model will forget to include information. For example in this row, the model forgot to include the email from the original data.
```
Original: CALEB FLORES,905-874-2142,cflores94@hotmail.net,"78 Elm Parkway -- Franklin -- Massachusetts -- 44195"
Expected: Caleb,Flores,905-874-2142,cflores94@hotmail.net,78 Elm Parkway,Franklin,Massachusetts,44195
Got:      Caleb,Flores,905-874-2142,,78 Elm Parkway,Franklin,Massachusetts,44195
```

For this row, the first and last name are NOT provided to the model. However, the model makes the unfounded assumption that the user's name is Daniel Cooper based off the email address
```
Original: ,+1 973-309-3597,dcooper@yahoo.com,"82 Maple Trail, Fairview, Ohio 61391"
Expected: ,,973-309-3597,dcooper@yahoo.com,82 Maple Trail,Fairview,Ohio,61391
Got:      Daniel,Cooper,973-309-3597,dcooper@yahoo.com,82 Maple Trail,Fairview,Ohio,61391
```

# Original Code

Setup instructions:

1. Clone the repository:
   ```
   git clone https://github.com/preferencemodel/hello-py.git
   ```

2. Navigate to the project directory:
   ```
   cd hello-py
   ```

3. Set up `ANTHROPIC_API_KEY` environment variable:
   ```
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

4. Run the agent:
   ```
   uv run main.py
   ```

## Execution Modes

The test suite supports both concurrent and sequential execution. 

To change modes, edit the `concurrent` parameter at the bottom of `main.py`:

```python
asyncio.run(main(concurrent=True))
asyncio.run(main(concurrent=False))
```

When running concurrently, results print as they complete (not in run order) for faster overall execution.
