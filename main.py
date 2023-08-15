from art import logo
from replit import clear


# print(logo)
# add
def add(n1, n2):
    return n1 + n2


# subtract
def substract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


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

        if input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculator: ") == "y":
            num1 = answer
        else:
            clear()
            should_continue = False
            calculator()


calculator()

# function = operations["+"]
# print(function(4, 4))

# def calculator():
#   num1 = int(input("What's the first number?: "))

#   for symbol in operations:
#     print(symbol)

#   operation_symbol = input("Pick an operation: ")
#   num2 = int(input("What's the second number?: "))


#   def op(num1, num2, operation_select):
#     calculation_function = operations[operation_select]
#     first_answer = calculation_function(num1, num2)
#     return first_answer

#   result= op(num1, num2, operation_symbol)
#   print(f"{num1} {operation_symbol} {num2} = {result}")

#   start = True
#   while start:
#     if input(f"Type 'y' to continue with {result} or type 'n' to continue: ") == "y":
#       operation_symbol = input("Pick next operation: ")
#       num3 = int(input("What's the next number?: "))
#       result= op(result, num3, operation_symbol)
#       print(f"{result} {operation_symbol} {num3} = {result}")
#     else:
#       if input("Restart:(y/n) ") == "y":
#         clear()
#         calculator()
#       else:
#         start = False

# calculator()


# calculation_function = operations[operation_symbol]
# first_answer = calculation_function(num1, num2)
# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# operation_symbol = input("pick another operation: ")
# num3 = int(input("What's the third number?: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

