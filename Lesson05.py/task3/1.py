phone = ["    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",]
def sanitize_phone_number(phone):
    new_phone = ''
    for i in phone:
        new_phone += i
    new_phone = (new_phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", ""))
    return new_phone
res = sanitize_phone_number(phone)
print(res)