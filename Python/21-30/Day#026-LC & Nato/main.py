""" Phonetic Phone-Helper
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.10 1851 """


import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

phon_dict = {row.letter:row.code for (index, row) in data.iterrows()}


def xfer_phone():
    word = input('Please input the word you need help conveying: ').upper()
    try:
        result = [phon_dict[letter] for letter in word]

    except KeyError:
        print('Sorry only letters in the alphabet please!')
        xfer_phone()

    else:
        print(result)
        print()
        xfer_phone()


xfer_phone()
