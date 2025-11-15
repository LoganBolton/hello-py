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
        f"{zip_code} {state} {street_num} {street_name} {street_end} {city}",
        f"{street_num}_{street_name}_{street_end}-{city}-{state_abbrev}-{zip_code}",
    ]
    return random.choice(template_address)

def noise_phone_number(phone_info):

    area_code = phone_info["area_code"]
    first_digits = phone_info["first_digits"]
    last_digits = phone_info["last_digits"]
    
    template_phone_number = [
        f"{area_code}-{first_digits}-{last_digits}",
        f"{area_code}{first_digits}{last_digits}",
        f"{area_code}-{first_digits}_{last_digits}",
        f"{area_code} .  {first_digits} {last_digits}",
        f"{area_code}-{area_code}-{first_digits}-{last_digits}",
    ]
    return random.choice(template_phone_number)

def noise_email(email_info):
    user = email_info["user"]
    org = email_info["org"]
    domain = email_info["domain"]
    template_email = [
        f"{user}@{org}.{domain}",
        f"{user}@{org}.{domain}".upper(),
        f"{user}@{org}@{domain}",
        f"{user}@{org}{domain}.{domain}",
    ]
    return random.choice(template_email)

def noise_name(name_info):
    first_name = name_info["first_name"].lower()
    last_name = name_info["last_name"].lower()
    template_name = [
        f"{first_name} {last_name}",
        f"{first_name} {last_name}".upper(),
        f"{first_name}_{last_name}",
        f"{first_name},{last_name},{last_name}"
    ]
    return random.choice(template_name)

gt_df = pd.DataFrame()
cols = ["noisy_full_name", "noisy_address", "noisy_phone_num", "noisy_email", "full_name", "full_address", "phone_num", "email", "first_name", "last_name", "phone_number", "city", "state", "state_abbrev", "zip_code", "street_address", "full_address", "area_code", "first_digits", "last_digits"]

display_df = pd.DataFrame()
display_cols = ["noisy_full_name", "noisy_address", "noisy_phone_num", "noisy_email"]

answer_df = pd.DataFrame()
answer_cols = ["first_name", "last_name", "phone_num", "email", "street_address", "city", "state", "zip_code"]
NOISE_ODDS = 0.4
DROPPOUT_ODDS = 0.05
for i in range(10):

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
    
    if random.random() < NOISE_ODDS:
        display_name = noise_name(name_info)
    if random.random() < NOISE_ODDS:
        display_address = noise_address(address_info)
    if random.random() < NOISE_ODDS:
        display_phone_number = noise_phone_number(phone_info)
    if random.random() < NOISE_ODDS:
        display_email = noise_email(email_info)


    display_df = pd.concat([display_df, pd.DataFrame([{
        "noisy_full_name": display_name,
        "noisy_address": display_address,
        "noisy_phone_num": display_phone_number,
        "noisy_email": display_email,
    }])], ignore_index=True)

    gt_df = pd.concat([gt_df, pd.DataFrame([{
        "full_name": name_info["full_name"],
        "full_address": address_info["full_address"],
        "phone_num": phone_info["phone_num"],
        "email": email_info["email"],
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_info["phone_num"],
        "city": address_info["city"],
        "state": address_info["state"],
        "state_abbrev": address_info["state_abbrev"],
        "zip_code": address_info["zip_code"],
        "street_address": address_info["street_address"],
        "area_code": phone_info["area_code"],
        "first_digits": phone_info["first_digits"],
        "last_digits": phone_info["last_digits"]
    }])], ignore_index=True)
    
    answer_df = pd.concat([answer_df, pd.DataFrame([{
        "first_name": first_name,
        "last_name": last_name,
        "phone_num": phone_info["phone_num"],
        "email": email_info["email"],
        "street_address": address_info["street_address"],
        "city": address_info["city"],
        "state": address_info["state"],
        "zip_code": address_info["zip_code"]
    }])], ignore_index=True)

    answer_df.to_csv("data/answer_df.csv", index=False)
    display_df.to_csv("data/display_df.csv", index=False)
    gt_df.to_csv("data/gt_df.csv", index=False)

print(display_df)
print(answer_df)