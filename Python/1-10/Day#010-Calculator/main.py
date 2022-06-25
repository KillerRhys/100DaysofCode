""" Calculator
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.19-2225 """

import os
import sys


def clear_screen():
    """Clears the current console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 80)


def add(n1, n2):
    """Adds two numbers together"""
    return n1 + n2


def subtract(n1, n2):
    """subtracts two given numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two values"""
    return n1 * n2


def divide(n1, n2):
    """Divides two values"""
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
first_run = True
conti = True

while conti:
    if first_run:
        num1 = float(input("What's the first number? "))

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number? "))

        calc_func = operations[operation_symbol]

        answer = float(calc_func(num1, num2))

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        more = input("Type y to continue with solution, n for a new caclulation or q to quit: ")
        if more.startswith("y"):
            num1 = answer
            first_run = False
        elif more.startswith("n"):
            num1 = float(input("What's the first number? "))
            first_run = False

        else:
            sys.exit()

    else:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number? "))

        calc_func = operations[operation_symbol]

        answer = float(calc_func(num1, num2))

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        more = input("Type y to continue with solution, n for a new caclulation or q to quit: ")
        if more.startswith("y"):
            num1 = answer
            first_run = False
        elif more.startswith("n"):
            num1 = float(input("What's the first number? "))
            first_run = False

        else:
            sys.exit()
