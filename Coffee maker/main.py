#Coffee Machine

from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from art import *

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
print(text2art("Coffee      Machine"))
if menu.password():
    is_on = True
    while is_on:
        options = menu.get_items()
        choice = int(input(f"\nWhat would you like to have?\n{options}\n"))
        if choice == 6:
            if menu.password():
                print("\nMachine is shutting down...")
                is_on = False
            else:
                print("\nIncorrect password.")
                menu.wait_and_clear()
        elif choice == 5:
            coffee_maker.report()
        elif choice == 4:
            money_machine.report()
        elif choice == 1 or choice == 2 or choice == 3:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            is_on = False
            print("\nInvalid input.")
else:
    print("\nIncorrect password.")
menu.wait_and_clear()
