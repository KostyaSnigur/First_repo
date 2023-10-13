from random import randint
password_lenght = 8
random = randint(40, 126)
password = chr(random)
res = password*password_lenght
for i in range(8):
    print(i)
