""" Password Generator
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.08-1243 """

# Ports
import random

# Lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Funcs
def new_pass():
    new_password = []
    hard_mode = False
    print("Welcome to the Password Generator PGen for short!")
    num_letters = int(input("How many numbers would you like? "))
    num_symbols = int(input("How many symbols would you like? "))
    num_nums = int(input("How many numbers would you like? "))
    shuffle = input("Want us to mix it up real good for ya? Yes or No? ")
    shuffle = shuffle.upper()
    if shuffle.startswith("Y"):
        hard_mode = True
    else:
        hard_mode = False

    if not hard_mode:
        while num_letters > 0:
            new_password += random.choice(letters)
            num_letters -= 1

        while num_symbols > 0:
            new_password += random.choice(symbols)
            num_symbols -= 1

        while num_nums > 0:
            new_password += random.choice(numbers)
            num_nums -= 1

        password = "".join(new_password)
        return password

    elif hard_mode:
        while num_letters > 0:
            new_password += random.choice(letters)
            num_letters -= 1

        while num_symbols > 0:
            new_password += random.choice(symbols)
            num_symbols -= 1

        while num_nums > 0:
            new_password += random.choice(numbers)
            num_nums -= 1

        random.shuffle(new_password)
        password = "".join(new_password)
        return password


print(new_pass())
