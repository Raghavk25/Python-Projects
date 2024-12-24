from replit import clear
import time

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost, index):
        self.name = name
        self.cost = cost
        self.index = index
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
    
class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name = "Espresso  ", water = 50, milk = 0, coffee = 18, cost = 1.5, index = 1),
            MenuItem(name = "Latte     ", water = 200, milk = 150, coffee = 24, cost = 2.5, index = 2),
            MenuItem(name = "Cappuccino", water = 250, milk = 50, coffee = 24, cost = 3, index = 3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = '' 
        for item in self.menu:
            options += f"Press {item.index} for {item.name} : ${item.cost}\n"
        options += f"Press 4 to view machine earnings (for office use).\n"
        options += f"Press 5 to view remaining ingredients (for office use).\n"
        options += f"Press 6 to shut down the machine (for office use).\n"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.index == order_name:
                return item
        print("Sorry that item is not available.")
    
    def password(self):
        if input("\nEnter password: ") == "Kaffeeland":
            clear()
            return True
        else:
            clear()
            return False
        
    def wait_and_clear(self):
        time.sleep(7)
        clear()
        

