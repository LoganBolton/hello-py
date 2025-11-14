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

    possible_nums = [f"{i}" for i in range(1, 9999)]
    possible_street_names = ["Main", "Oak", "Pine", "Maple", "Cedar", "Elm", "Washington", "Lake", "Hill", "Sunset", "Park", "River", "Cherry", "Walnut", "Birch", "Spruce", "Willow", "Chestnut", "Dogwood", "Magnolia"]
    possible_street_ends = ["Lane", "Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Terrace", "Way", "Trail", "Parkway"]

    possible_cities = ["Springfield", "Riverside", "Greenville", "Fairview", "Madison", "Georgetown", "Arlington", "Ashland", "Clinton", "Franklin", "Salem", "Bristol", "Milton", "Oakland", "Centerville", "Dayton", "Lexington", "Dover", "Hudson", "Kingston"]
    possible_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    possible_zip_codes = [f"{i:05d}" for i in range(10000, 99999)]

    num = random.choice(possible_nums)
    street_name = random.choice(possible_street_names)
    street_end = random.choice(possible_street_ends)
    city = random.choice(possible_cities)
    state = random.choice(possible_states)
    zip_code = random.choice(possible_zip_codes)
    address = f"{num} {street_name} {street_end}, {city}, {state} {zip_code}"

    output = {
        "street_num": num,
        "street_name": street_name,
        "street_end": street_end,
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "full_address": address
    }
    return output

def generate_email(first_name, last_name):
    possible_domains = ["org", "com", "net", "io", "edu"]
    possible_orgs = ["gmail", "yale", "outlook", "nike", "yahoo", "hotmail", "instantmail"]

    possible_words = ["fast", "quick", "speedy", "smart", "bright", "clever", "brave", "strong", "mighty", "fierce"]

    first_name_letter = first_name[0]
    
    email_formats = [
        f"{first_name}.{last_name}",
        f"{first_name_letter}{last_name}",
        f"{first_name}_{last_name}",
        f"{first_name}{random.choice(possible_words)}",
        f"{last_name}{random.randint(1,99)}"
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

for i in range(10):
    # print(generate_phone_number()["phone_num"])

    # print(generate_name()["full_name"])
    # print(generate_address()["full_address"])

    name_info = generate_name()
    first_name = name_info["first_name"].lower()
    last_name = name_info["last_name"].lower()
    email_info = generate_email(first_name, last_name)
    print(email_info["email"])

