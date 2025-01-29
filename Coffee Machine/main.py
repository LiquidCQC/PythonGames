from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()


while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        CoffeeMaker().report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)