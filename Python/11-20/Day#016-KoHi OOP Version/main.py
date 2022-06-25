""" KoHi Machine OOP Version
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.07-2125 """

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
operational = True

gob = MoneyMachine()
kohi = CoffeeMaker()
garcon = Menu()


def reports():
    kohi.report()
    gob.report()


while operational:
    selection = garcon.get_items()
    choice = input(f"What would you like? {selection}: ")
    if choice == "off":
        operational = False

    elif choice == "report":
        reports()

    else:
        drink = garcon.find_drink(choice)
        if kohi.is_resource_sufficient(drink):
            if gob.make_payment(drink.cost):
                kohi.make_coffee(drink)