a = 5
b = 0


def fun():
    global a
    a = 10
    b = 2


fun()
print(a)  # 10
print(b)  # 0