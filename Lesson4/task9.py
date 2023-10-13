def have_duplicates(array):
    return not (len(set(array)) == len(array))

def is_valid_pin_codes(pin_codes):
    is_valid = True
    if not pin_codes:
        return False
    
    if have_duplicates(pin_codes):
        return False
    
    for pincode in pin_codes:
        if not len(pincode) == 4:
            is_valid = False

        if not pincode.isdigit():
            is_valid = False

        if not isinstance(pincode, str):
            is_valid = False    

    return is_valid
    