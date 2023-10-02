def get_fullname (first_name="Kostiantin ", middle_name=" ", last_name="Snihur"):
    if middle_name == False:
        return first_name + last_name
    else: 
        return first_name + middle_name + last_name
get_fullname()