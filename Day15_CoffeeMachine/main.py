MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_resources_spent = {
        "water": 0,
        "milk": 0,
        "coffee": 0
    }

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01
}

total_money = 0
continue_ordering = True


# Print a report. What resources the machine has left
def print_report():
    report_contents = {
        "Water": resources.get("water"),
        "Milk": resources.get("milk"),
        "Coffee": resources.get("coffee"),
        "Money": total_money
    }

    return report_contents


def determine_drink_choice(user_entry):
    if user_entry == "espresso":
        return 1
    elif user_entry == "latte":
        return 2
    elif user_entry == "cappuccino":
        return 3
    elif user_entry == "report":
        return print_report()
    elif user_entry == "off":
        return False


def determine_total_bill():
    if user_choice == "espresso":
        total_bill = float(MENU['espresso']['cost'])
        return total_bill
    elif user_choice == "latte":
        total_bill = float(MENU['latte']['cost'])
        return total_bill
    elif user_choice == "cappuccino":
        total_bill = float(MENU['cappuccino']['cost'])
        return total_bill
    else:
        return 0


def cannot_make_drink():
    return "Not enough ingredients to make your drink or you didn't provide enough funds."


# Check if resources are sufficient to create the ordered drink. If not, tells user what is missing
def check_machine_resources(selected_drink):
    if selected_drink == 1:
        resources_required = MENU['espresso']['ingredients']
        for item in resources:
            if item not in resources_required:
                continue
            elif item == "water":
                amount_water = MENU['espresso']['ingredients']['water']
                total_water = resources['water']
                if total_water < amount_water:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True
            elif item == "milk":
                amount_milk = MENU['espresso']['ingredients']['milk']
                total_milk = resources['milk']
                if total_milk < amount_milk:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True
            elif item == "coffee":
                amount_coffee = MENU['espresso']['ingredients']['coffee']
                total_coffee = resources['coffee']
                if total_coffee < amount_coffee:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True
        store_drink_resource_cost(resources_required)
    elif selected_drink == 2:
        resources_required = MENU['latte']['ingredients']
        for item in resources:
            if item not in resources_required:
                continue
            elif item == "water":
                amount_water = MENU['latte']['ingredients']['water']
                total_water = resources['water']
                if total_water < amount_water:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True
            elif item == "milk":
                amount_milk = MENU['latte']['ingredients']['milk']
                total_milk = resources['milk']
                if total_milk < amount_milk:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True
            elif item == "coffee":
                amount_coffee = MENU['latte']['ingredients']['coffee']
                total_coffee = resources['coffee']
                if total_coffee < amount_coffee:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True
        store_drink_resource_cost(resources_required)
    elif selected_drink == 3:
        resources_required = MENU['cappuccino']['ingredients']
        for item in resources:
            if item not in resources_required:
                continue
            elif item == "water":
                amount_water = MENU['cappuccino']['ingredients']['water']
                total_water = resources['water']
                if total_water < amount_water:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True
            elif item == "milk":
                amount_milk = MENU['cappuccino']['ingredients']['milk']
                total_milk = resources['milk']
                if total_milk < amount_milk:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True
            elif item == "coffee":
                amount_coffee = MENU['cappuccino']['ingredients']['coffee']
                total_coffee = resources['coffee']
                if total_coffee < amount_coffee:
                    resource_result = cannot_make_drink()
                    break
                else:
                    resource_result = True

        store_drink_resource_cost(resources_required)

    return resource_result


def calculate_coin_total(quarters, dimes, nickels, pennies):
    value_quarters = quarters * coins['quarter']
    value_dimes = dimes * coins['dime']
    value_nickels = nickels * coins['nickel']
    value_pennies = pennies * coins['penny']
    values = [value_quarters, value_dimes, value_nickels, value_pennies]
    coin_value = round(sum(values), 2)
    print(f"Coin total: ${coin_value}")
    return coin_value


def check_if_transaction_can_be_completed(ingredients, payment):
    total_bill = determine_total_bill()
    print(f"Total bill: ${total_bill}")
    if payment >= total_bill and ingredients is True:
        return True
    else:
        return False


def calculate_change():
    total_bill = determine_total_bill()
    if total_payment_provided > total_bill:
        user_change = round((total_payment_provided - total_bill), 2)
    else:
        user_change = 0

    return user_change


def store_drink_resource_cost(resources_used):
    for key in resources_used:
        if key not in resources_used:
            continue
        elif key == "water":
            water_used = resources_used['water']
            total_resources_spent["water"] = water_used
        elif key == "milk":
            milk_used = resources_used['milk']
            total_resources_spent["milk"] = milk_used
        elif key == "coffee":
            coffee_used = resources_used['coffee']
            total_resources_spent["coffee"] = coffee_used
    return total_resources_spent


def deduct_resources_after_successful_sale(resource_cost):
    for key in resource_cost:
        if key == "water":
            resources['water'] -= resource_cost['water']
        elif key == "milk":
            resources['milk'] -= resource_cost['milk']
        elif key == "coffee":
            resources['coffee'] -= resource_cost['coffee']

    return resources


while continue_ordering == True:

    user_choice = input("\tWhat would you like? (espresso, latte, cappuccino): ").lower()

    drink_choice = determine_drink_choice(user_choice)
    if drink_choice == 1 or drink_choice == 2 or drink_choice == 3:
        print("Please insert coins.")
        num_quarters = float(input("How many quarters? "))
        num_dimes = float(input("How many dimes? "))
        num_nickels = float(input("How many nickels? "))
        num_pennies = float(input("How many pennies? "))
        result = check_machine_resources(drink_choice)
        total_payment_provided = calculate_coin_total(num_quarters, num_dimes, num_nickels, num_pennies)
        charge_customer = check_if_transaction_can_be_completed(result, total_payment_provided)

        if charge_customer:
            change = calculate_change()
            deduct_resources_after_successful_sale(total_resources_spent)
            if change > 0:
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice}. Enjoy!")
            else:
                print(f"Here is your {user_choice}. Enjoy!")
            total_money += total_payment_provided - change
        else:
            response = cannot_make_drink()
            print(response)
    elif drink_choice is False:
        continue_ordering = False
    else:
        if drink_choice is None:
            print("Please select a drink from the list.")
        else:
            print(drink_choice)
