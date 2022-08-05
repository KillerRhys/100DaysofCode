""" Gatekeeper
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.27-1743 """


# Imports
import tkinter.simpledialog
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# TODO Find a way to use pwg from dialog box
def gen_pass():
    pass_entry.delete(0, END)
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    pass_entry.insert(0, password)


def search():
    site = site_entry.get().title()
    if len(site) == 0:
        answer = tkinter.simpledialog.askstring(title="Missing Data", prompt="Please enter a valid site!")
        site_entry.insert(0, answer)

    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            tkinter.messagebox.showwarning(message='There is no saved data! Save a site before trying again!')

        else:
            try:
                result = data[site]
            except KeyError:
                tkinter.messagebox.showwarning(message="There is no site by that name currently recorded.. Try again?")
            else:
                name_entry.delete(0, END)
                pass_entry.delete(0, END)
                user = result['email']
                password = result['password']
                name_entry.insert(0, user)
                pass_entry.insert(0, password)


# TODO Fix is_ok error
def save_info():
    site = site_entry.get().title()
    user = name_entry.get()
    password = pass_entry.get()
    new_data = {site: {
        'email': user,
        'password': password

        }
    }

    if len(site) == 0:
        answer = tkinter.simpledialog.askstring(title="Missing Data", prompt="Please enter a valid site!")
        site_entry.insert(0, answer.title())
        save_info()

    elif len(user) == 0:
        answer = tkinter.simpledialog.askstring(title="Missing Data", prompt="Please enter a valid user!")
        name_entry.insert(0, answer)
        save_info()

    elif len(password) == 0:
        answer = tkinter.simpledialog.askstring(title="Missing Data", prompt="Please enter a valid password!")
        pass_entry.insert(0, answer)
        save_info()

    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            site_entry.delete(0, END)
            pass_entry.delete(0, END)


# TODO Needs revamp
display = Tk()
display.title('Gatekeeper')
display.config(padx=30, pady=30)
backdrop = Canvas(width=200, height=200)
logo_img = PhotoImage(file='gatekeeper.png')
backdrop.create_image(75, 100, image=logo_img)
backdrop.grid(column=1, row=0)


# Labels
web_addr = Label(text='Website:', font=('Arial', 15, 'bold'))
web_addr.grid(column=0, row=1, sticky='e')
user_mail = Label(text='Email/Username:', font=('Arial', 15, 'bold'))
user_mail.grid(column=0, row=2, sticky='e')
pass_label = Label(text='Password:', font=('Arial', 15, 'bold'))
pass_label.grid(column=0, row=3, sticky='e')


# Entries
site_entry = Entry(width=35)
site_entry.grid(column=1, row=1, columnspan=2, sticky='w')
site_entry.focus()
name_entry = Entry(width=35)
name_entry.grid(column=1, row=2, columnspan=2, sticky='w')
name_entry.insert(0, 'user@mail.com')
pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3, columnspan=2, sticky='w')


# Buttons
search_button = Button(text='Search', width=30, command=search)
search_button.grid(column=1, row=4, sticky='w')
pass_button = Button(text='Generate Password', width=30, command=gen_pass)
pass_button.grid(column=1, row=5, sticky='w')
add_button = Button(text='Add', width=30, command=save_info)
add_button.grid(column=1, row=6, columnspan=2, sticky='w')


display.mainloop()
