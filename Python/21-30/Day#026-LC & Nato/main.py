""" Phonetic Phone-Helper
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.10 1851 """


import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

phon_dict = {row.letter:row.code for (index, row) in data.iterrows()}
word = input('Please input the word you need help conveying: ').upper()
result = [phon_dict[letter] for letter in word]
print(result)
