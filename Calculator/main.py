from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator ():
    print(logo)
    should_accumulate = True
    first_number = float(input("what's your first number?"))
    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operator = input("Pick an operation: ")
        second_number = float(input("What's your second number?"))
        result = operation[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
        print("\n" * 20)


calculator()

