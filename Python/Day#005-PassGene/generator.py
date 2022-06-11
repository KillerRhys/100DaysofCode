""" OOP Practice """

import random


class PassMaker:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    new_password = []

    def config(self):
        print("Welcome to the Password Generator PGen for short!")
        num_letters = int(input("How many numbers would you like? "))
        num_symbols = int(input("How many symbols would you like? "))
        num_nums = int(input("How many numbers would you like? "))
        while num_letters > 0:
            self.new_password += random.choice(self.letters)
            num_letters -= 1

        while num_symbols > 0:
            self.new_password += random.choice(self.symbols)
            num_symbols -= 1

        while num_nums > 0:
            self.new_password += random.choice(self.numbers)
            num_nums -= 1

        shuffs = 3
        while shuffs > 0:
            random.shuffle(self.new_password)
            shuffs -= 1

        password = "".join(self.new_password)
        print(password)