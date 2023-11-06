from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
coffee_machine = CoffeeMaker()
atm = MoneyMachine()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        atm.report()
        coffee_machine.report()
    else:
        drink_choice = my_menu.find_drink(choice)
        if drink_choice is None:
            is_on = True
        elif coffee_machine.is_resource_sufficient(drink_choice) and atm.make_payment(drink_choice.cost):
            coffee_machine.make_coffee(drink_choice)
        else:
            is_on = True
