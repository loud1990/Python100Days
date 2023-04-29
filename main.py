# This is a Python Calculator Program

from art import logo

# Add
def add(x, y):
    return x + y

# Subtract
def subtract(x, y):
    return x - y

# Multiply
def multiply(x, y):
    return x * y

# Divide
def divide(x, y):
    return x / y

# Dictionary of operations
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# Calculator Program
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()