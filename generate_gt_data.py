import pandas as pd
import random

def generate_phone_number():
    possible_area_codes = [f"{i:03d}" for i in range(100, 999)]
    possible_first_phone_digits = [f"{i:03d}" for i in range(100, 999)]
    possible_last_phone_digits = [f"{i:04d}" for i in range(1000, 9999)]

    area_code = random.choice(possible_area_codes)
    first_digits = random.choice(possible_first_phone_digits)
    last_digits = random.choice(possible_last_phone_digits)

    phone_num = f"{area_code}-{first_digits}-{last_digits}"

    output = {
        "area_code": area_code,
        "first_digits": first_digits,
        "last_digits": last_digits,
        "phone_num": phone_num
    }

    return output 

def generate_name():
    possible_first_names = ["John", "Logan", "Ethan", "Davis", "Jack", "Scott", "James", "Daniel", "Aiden", "Michael", "Benjamin", "Eli", "David", "Jacob", "William", "Alexander", "Ryan", "Matthew", "Henry", "Joseph", "Jackson", "Samuel", "Judson", "Braden", "Luke", "Gabriel", "Owen", "Carter", "Wyatt", "Jayden", "Julian", "Grayson", "Levi", "Isaac", "Lincoln", "Anthony", "Joshua", "Christopher", "Andrew", "Theodore", "Caleb", "Christian", "Jaxon", "Landon", "Jonathan", "Nolan", "Hunter", "Cameron", "Connor","Jeremiah", "Ezekiel", "Angel", "Rachel", "Emma", "Olivia", "Ava", "Sophia", "Isabella", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Ella", "Scarlett", "Grace", "Chloe"]

    possible_last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes", "Bolton"]

    first_name = random.choice(possible_first_names)
    last_name = random.choice(possible_last_names)
    full_name = f"{first_name} {last_name}"
    output = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name
    }
    return output

def generate_address():

    possible_nums = [f"{i}" for i in range(1, 999)]
    possible_street_names = ["Main", "Oak", "Pine", "Maple", "Cedar", "Elm", "Washington", "Lake", "Hill", "Sunset", "Park", "River", "Cherry", "Walnut", "Birch", "Spruce", "Willow", "Chestnut", "Dogwood", "Magnolia"]
    possible_street_ends = ["Lane", "Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Terrace", "Way", "Trail", "Parkway"]

    possible_cities = ["Springfield", "Lancaster", "Greenville", "Fairview", "Madison", "Georgetown", "Arlington", "Ashland", "Clinton", "Franklin", "Salem", "Bristol", "Milton", "Oakland", "Centerville", "Dayton", "Lexington", "Dover", "Hudson", "Kingston"]
    possible_states_abbrev = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    possible_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    possible_zip_codes = [f"{i:05d}" for i in range(10000, 99999)]

    num = random.choice(possible_nums)
    street_name = random.choice(possible_street_names)
    street_end = random.choice(possible_street_ends)
    city = random.choice(possible_cities)
    state_id = random.choice(possible_states_abbrev)
    state = possible_states[possible_states_abbrev.index(state_id)]
    
    zip_code = random.choice(possible_zip_codes)
    address = f"{num} {street_name} {street_end}, {city}, {state} {zip_code}"

    output = {
        "street_num": num,
        "street_name": street_name,
        "street_end": street_end,
        "street_address": f"{num} {street_name} {street_end}",
        "city": city,
        "state": state,
        "state_abbrev": state_id,
        "zip_code": zip_code,
        "full_address": address
    }
    return output

def generate_email(first_name, last_name):
    possible_domains = ["org", "com", "net", "io", "edu"]
    possible_orgs = ["gmail", "yale", "outlook", "nike", "yahoo", "hotmail", "instantmail"]

    possible_words = ["fast", "quick", "speedy", "smart", "bright", "clever", "brave", "strong", "mighty", "fierce"]

    first_name_letter = first_name[0]
    random_num = random.randint(1,99)
    
    email_formats = [
        f"{first_name}.{last_name}",
        f"{first_name_letter}{last_name}",
        f"{first_name_letter}{last_name}{random_num}",
        f"{first_name}_{last_name}_{random_num}{random_num}",
        f"{first_name}{random.choice(possible_words)}",
        f"{last_name}{random_num}"
    ]

    email_user = random.choice(email_formats)
    email_org = random.choice(possible_orgs)
    email_domain = random.choice(possible_domains)

    email = f"{email_user}@{email_org}.{email_domain}"
    output = {
        "user": email_user,
        "org": email_org,
        "domain": email_domain,
        "email": email
    }
    return output

def noise_address(address_info):
    street_num = address_info["street_num"]
    street_name = address_info["street_name"]
    street_end = address_info["street_end"]
    city = address_info["city"]
    state = address_info["state"]
    state_abbrev = address_info["state_abbrev"]
    zip_code = address_info["zip_code"]
    
    template_address = [
        f"{street_num} {street_name} {street_end}, {city}, {state} {zip_code}",
        f"{street_num} {street_name} {street_end}, {city}, {state_abbrev} {zip_code}",
        f"{street_num}{street_name}{street_end}{city}{state_abbrev}{zip_code}",
        f"zip code: {zip_code} -- {state} {street_num} {street_name} {street_end} {city}",
        f"{street_num}_{street_name}_{street_end}-{city}-{state_abbrev}-{zip_code}",
    ]
    return random.choice(template_address)

def noise_phone_number(phone_info):

    area_code = phone_info["area_code"]
    first_digits = phone_info["first_digits"]
    last_digits = phone_info["last_digits"]
    
    template_phone_number = [
        f"{area_code}-{first_digits}-{last_digits}",
        f"{area_code}-{first_digits}-{last_digits}-{area_code}-{first_digits}-{last_digits}",
        f"+1 {area_code}-{first_digits}-{last_digits}",
        f"{area_code}{first_digits}{last_digits}",
        f"{area_code}-{first_digits}_{last_digits}",
        f"{area_code} .  {first_digits} {last_digits}",
    ]
    return random.choice(template_phone_number)

def noise_email(email_info):
    user = email_info["user"]
    org = email_info["org"]
    domain = email_info["domain"]
    template_email = [
        f"{user}@{org}.{domain}{user}@{org}.{domain}",
        f"{user}@{org}.{domain}",
        f"{user}@{org}.{domain}",
        f"{user}@{org}@{domain}",
        f"{user}@{org}  {domain}.{domain}",
    ]
    return random.choice(template_email)

def noise_name(name_info):
    first_name = name_info["first_name"].lower()
    last_name = name_info["last_name"].lower()
    template_name = [
        f"{first_name} {last_name}",
        f"{first_name} {last_name} {first_name.upper()} {last_name.upper()}",
        f"{first_name} {last_name}".upper(),
        f"{first_name}_{last_name}",
        f"{first_name},{last_name},{last_name}"
    ]
    return random.choice(template_name)

def generate_test_data(n_rows=10, noise_odds=0.6, dropout_odds=0.10):
    """Generate test data without saving to files. Returns CSV strings."""
    display_rows = []
    answer_rows = []

    for i in range(n_rows):
        name_info = generate_name()
        first_name = name_info["first_name"].lower()
        last_name = name_info["last_name"].lower()

        email_info = generate_email(first_name, last_name)
        phone_info = generate_phone_number()
        address_info = generate_address()

        display_name = name_info["full_name"]
        display_address = address_info["full_address"]
        display_phone_number = phone_info["phone_num"]
        display_email = email_info["email"]

        if random.random() < noise_odds:
            display_name = noise_name(name_info)
        if random.random() < noise_odds:
            display_address = noise_address(address_info)
        if random.random() < noise_odds:
            display_phone_number = noise_phone_number(phone_info)
        if random.random() < noise_odds:
            display_email = noise_email(email_info)

        if random.random() < dropout_odds:
            display_name = ""
            first_name = ""
            last_name = ""
        if random.random() < dropout_odds:
            display_address = ""
            address_info["street_address"] = ""
            address_info["city"] = ""
            address_info["state"] = ""
            address_info["zip_code"] = ""
        if random.random() < dropout_odds:
            display_phone_number = ""
            phone_info["phone_num"] = ""
        if random.random() < dropout_odds:
            display_email = ""
            email_info["email"] = ""

        display_rows.append({
            "noisy_full_name": display_name,
            "noisy_phone_num": display_phone_number,
            "noisy_email": display_email,
            "noisy_address": display_address,
        })

        answer_rows.append({
            "first_name": first_name.title(),
            "last_name": last_name.title(),
            "phone_num": phone_info["phone_num"],
            "email": email_info["email"],
            "street_address": address_info["street_address"],
            "city": address_info["city"].title(),
            "state": address_info["state"].title(),
            "zip_code": address_info["zip_code"]
        })

    display_df = pd.DataFrame(display_rows)
    answer_df = pd.DataFrame(answer_rows)

    # Convert to CSV strings
    display_csv = display_df.to_csv(index=False)
    answer_csv = answer_df.to_csv(index=False)

    return display_csv, answer_csv


def main():
    """Save generated data to files for testing"""
    display_csv, answer_csv = generate_test_data()

    with open("data/display_df.csv", "w") as f:
        f.write(display_csv)
    with open("data/answer_df.csv", "w") as f:
        f.write(answer_csv)


if __name__ == "__main__":
    main()