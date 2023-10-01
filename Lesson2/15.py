result = None
operand = None
operator = None
wait_for_number = True

while True:
    enter = input(">>> ")
    if enter == "=":
        print(f"Result: {result}")
    if wait_for_number:
        try:
            operand = float(enter)
            wait_for_number = False
        except ValueError:
            print("Invalid number")
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result *operand
        elif operator == "/":
            result / operand
            try:
                result = result / operand
            except ZeroDivisionError:
                print("Divide by zero!")
        else:
            result = operand      



