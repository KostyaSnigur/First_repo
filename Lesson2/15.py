result = None
operand = None
operator = None
wait_for_number = True
operators = "+-*/"

while True:
    try:
        if wait_for_number:
            operand = float(input(">>> "))
            if not result:
                result = operand
            else:
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "*":
                    result *= operand
                elif operator == "/":
                    result /= operand
            wait_for_number = False
        else:
            operator = input(">>> ")
            if operator == "=":
                print(f"Result: {result}")
                break
            elif operator in operators:
                wait_for_number = True
            else:
                print("Unknown operator. Try again!")

    except ValueError:
        print("That's not an int! Try again!")
    except ZeroDivisionError:
        print("Can't divide by 0. Try again!")
    except Exception as e:
        print(e)