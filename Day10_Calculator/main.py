from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))

    continue_calculating = True
    while continue_calculating:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("What operation would you like to perform?: ")
        num2 = float(input("What's the next number?: "))

        chosen_func = operations.get(operation_symbol)
        try:
            answer = chosen_func(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer} ")

            continue_response = input(f"Type 'y' to continue calculating with the previous result: {answer}. "
                                      f"Type 'n' to start a new calculation: ").lower()
            print()
            if continue_response == "y":
                continue_calculating = True
                num1 = answer
                print(f"First number is {num1}.")
            else:
                continue_calculating = False
                calculator()

        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")
            print()
            print(f"First Number: {num1}")
            continue_calculating = True


calculator()
