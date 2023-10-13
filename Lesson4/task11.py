def is_valid_password(password):
    if len(password) != 8:
        return False
    
    upper = False
    lower = False
    digit = False

    for char in password:
        if char.isdigit():
            upper = True 
        if char.isupper():
            lower = True
        if char.islower():
            digit = True 
    if upper and lower and digit:
        return True
    else:
        return False

a = 'длlдлL11'
print(type(is_valid_password(a)))
