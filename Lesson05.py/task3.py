phone = ["    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",]

def sanitize_phone_number(phone):
    phone_list = []
    for i in phone:
        new_phone = (i.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
        .replace("'", ""))
        phone_list.append(new_phone)
    return phone_list
res = sanitize_phone_number(phone)
print(res)








    
        
        
        
        
        
        
    
    