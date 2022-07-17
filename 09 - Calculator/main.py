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
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    n1 = float(input("What's the first number?: "))
    continue_calc = True

    while continue_calc:
        for operator in operation:
            print(operator)
        operation_to_do = input("Pick an operation from the line above: ")

        n2 = float(input("What's the next number?: "))

        perform_operation = operation[operation_to_do]
        answer = perform_operation(n1, n2)
        print(f"{n1} {operation_to_do} {n2} = {answer}")

        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == "n":
            continue_calc = False
            calculator()
        else:
            n1 = answer


calculator()
