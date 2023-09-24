name = input("What's your name>>> ")
age = int(input("How old are you >>> "))


# formatted stringst
# snake case exp. datacase_results
 
upper_name = name.upper()

print(type(name))
print(type(age))
print(f"Hello Mr: {name} $ {upper_name} {age}")

print("*" * 10)
print("Mr: " + name + str(age))

print("Mr: ", name, age)