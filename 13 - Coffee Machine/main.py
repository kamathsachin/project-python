from menu import MENU, resources

ingredients_left = resources


def take_payment():
    """Takes the payment from the customer and returns a payment dictionary"""
    no_of_quarters = int(input("how many quarters?: "))
    no_of_dimes = int(input("how many dimes?: "))
    no_of_nickles = int(input("how many nickles?: "))
    no_of_pennies = int(input("how many pennies?: "))

    payment = {
        "quarters": no_of_quarters,
        "dimes": no_of_dimes,
        "nickles": no_of_nickles,
        "pennies": no_of_pennies,
    }

    return payment


def calculate_payment(payment_details):
    quarters_amt = int(payment_details['quarters']) * 0.25
    dime_amt = int(payment_details['dimes']) * 0.10
    nickle_amt = int(payment_details['nickles']) * 0.05
    pennies_amt = int(payment_details['pennies']) * 0.01

    total_payment_amount = quarters_amt + dime_amt + nickle_amt + pennies_amt

    return total_payment_amount


def calculate_change(beverage, payment_made):
    beverage_cost = MENU[beverage]['cost']
    cost_difference = payment_made - beverage_cost

    return cost_difference


def process_payment(user_selection):
    payment_details = take_payment()
    total_payment_made = calculate_payment(payment_details)
    change = calculate_change(user_selection, total_payment_made)

    return change


def calculate_ingredients(user_selection):
    global ingredients_left
    ingredients_left['water'] = resources


def make_coffee(user_selection):
    pass


def display_user_choice(user_option):
    if user_option == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
    else:
        change_amt = process_payment(user_option)
        make_coffee(user_option, MENU[user_option]['ingredients'])

display_user_choice(input("What would you like? (espresso/latte/cappuccino): "))
