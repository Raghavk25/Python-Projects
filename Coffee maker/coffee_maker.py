from replit import clear
import time

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 3000,
            "milk": 2000,
            "coffee": 400,
        }

    def report(self):
        """Prints a report of all resources."""
        if input("\nEnter password: ") == "Kaffeeland":
            clear()
            print("REMAINING INGREDIENTS\n")
            print(f"Water  : {self.resources['water']}ml")
            print(f"Coffee : {self.resources['coffee']}g")
            print(f"Milk   : {self.resources['milk']}ml")
        else:
            clear()
            print("Incorrect password.")
        time.sleep(7)
        clear()
        

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\nSorry, there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}\nEnjoy!")
        time.sleep(7)
        clear()

