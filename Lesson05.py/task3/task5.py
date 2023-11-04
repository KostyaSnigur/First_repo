def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    country_phone_numbers = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }

    for phone in list_phones:
        sanitized_phone = sanitize_phone_number(phone)
        if sanitized_phone.startswith("380"):
            country_phone_numbers["UA"].append(sanitized_phone)
        elif sanitized_phone.startswith("81"):
            country_phone_numbers["JP"].append(sanitized_phone)
        elif sanitized_phone.startswith("886"):
            country_phone_numbers["TW"].append(sanitized_phone)
        elif sanitized_phone.startswith("65"):
            country_phone_numbers["SG"].append(sanitized_phone)
        else:
            country_phone_numbers["UA"].append(sanitized_phone)

    return country_phone_numbers