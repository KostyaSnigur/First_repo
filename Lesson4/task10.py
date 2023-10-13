from random import randint

def get_random_password():
    #symbols = "()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    password = ""
    for i in range(8):
        random_num = randint(40, 126)
        password += chr(random_num)
    return password
res = get_random_password()
print(res)