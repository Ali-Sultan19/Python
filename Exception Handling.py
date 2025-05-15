# Exception handling example with try, except, else, and finally

def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution complete.")


def calculator():
    print("Welcome to the simple calculator!")
    try:
        num1 = float(input("Enter the first number: "))
        op = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("You cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError(f"Unsupported operation: {op}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Math error: {zde}")
    else:
        print(f"Result: {result}")
    finally:
        print("Calculation attempt finished.\n")




# Run the calculator
calculator()

# Run the function
divide_numbers()


