""" Ko-hi Coffee Software
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.04-1221 """


import menu


def resources():
    """ Prints current available resources."""
    print(f"Water: {menu.resources['water']} ml\nMilk: {menu.resources['milk']} ml\nCoffee: {menu.resources['coffee']}"
          f" ml\nMoney: ${menu.bank['money']}")


def check_tank(item):
    """ Takes selected item and checks if enough resources to make."""
    drink = item
    menu_stuff = menu.MENU[drink]['ingredients']
    for key in menu_stuff:
        if menu_stuff[key] > menu.resources[key]:
            return False
        else:
            return True


def payment(item):
    """ Gathers item cost and handles transaction / refund"""
    cost = menu.MENU[item]['cost']
    quarters = int(input(f"Your {item} costs ${cost: .2f}. How many Quarters do you have?: "))
    dimes = int(input(f"Your {item} costs ${cost: .2f}. How many Dimes do you have?: "))
    nickles = int(input(f"Your {item} costs ${cost: .2f}. How many Nickles do you have?: "))
    pennies = int(input(f"Your {item} costs ${cost: .2f}. How many Pennies do you have?: "))
    quarters = quarters * 0.25
    dimes = dimes * 0.10
    nickles = nickles * 0.05
    pennies = pennies * 0.01
    total = quarters + dimes + nickles + pennies
    if total == cost:
        print("Exact change!")
        menu.bank['money'] += int(cost)
        make_drink(item)
        home_screen()

    elif total > cost:
        change = total - cost
        print(f"You're due back ${change: .2f}")
        menu.bank['money'] += int(cost)
        make_drink(item)
        home_screen()

    elif total < cost:
        print("Oops that's not enough. Dispensing refund")
        home_screen()

    else:
        print("Something is wrong")
        home_screen()


def make_drink(item): # TODO fix resources bug
    """ Makes drink and tallies resources """
    drink = item
    menu_items = menu.MENU[drink]['ingredients']
    for key in menu_items:
        menu.resources[key] -= menu_items[key]

    print(f"Here is your {drink} enjoy!")


def home_screen():
    selection = input(f"Welcome to KoHi which drink would you like? [Espresso: ${menu.MENU['espresso']['cost']: .2f}, "
                   f"Latte: ${menu.MENU['latte']['cost']: .2f}, Cappuccino: ${menu.MENU['cappuccino']['cost']: .2f}]: ")

    selection = selection.upper()
    print(selection)

    if selection.startswith("M"):
        print("Maintenance mode: Sorry we are working to fix the issue quickly.")

    elif selection.startswith('R'):
        resources()
        home_screen()

    elif selection.startswith('E'):
        can_make = check_tank('espresso')
        if can_make:
            payment('espresso')

        else:
            print("fail")

    elif selection.startswith('L'):
        can_make = check_tank('latte')
        if can_make:
            payment('latte')

        else:
            print("fail")

    elif selection.startswith('C'):
        can_make = check_tank('cappuccino')
        if can_make:
            payment('cappuccino')

        else:
            print("fail")

    else:
        print("Please try a valid selection!")
        home_screen()


home_screen()
