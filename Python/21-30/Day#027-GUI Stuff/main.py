""" Conversion 7.0
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.11:1829 """


from tkinter import *


FONT = ('Arial', 20, 'bold')


def get_kms():
    miles = int(user_input.get())
    kilos = miles * 1.6
    kms['text'] = round(kilos)


display = Tk()
display.title('Conversion 7.0')
display.minsize(width=480, height=150)
display.configure(bg='Black')
equal_label = Label(text='is equal to', font=FONT, bg='black', fg='lime')
equal_label.grid(column=0, row=1)
user_input = Entry(width=15, font=FONT, bg='black', fg='lime')
user_input.grid(column=1, row=0)
kms = Label(text='0', font=FONT, bg='black', fg='lime')
kms.grid(column=1, row=1)
km_label = Label(text='Km', font=FONT, bg='black', fg='lime')
km_label.grid(column=2, row=1)
miles_label = Label(text='Miles', font=FONT, bg='black', fg='lime')
miles_label.grid(column=2, row=0)
button = Button(text='Calculate', font=FONT, bg='black', fg='purple', command=get_kms)
button.grid(column=1, row=2)


display.mainloop()
