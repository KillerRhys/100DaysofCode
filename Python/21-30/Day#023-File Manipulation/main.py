""" Mail Merge
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.02-0827 """


with open('Input/Letters/starting_letter.txt', 'r') as blank_letter:
    letter = blank_letter.read()


with open("Input/Names/invited_names.txt", 'r') as names:
    names_list = names.read().splitlines()


for name in names_list:
    new_letter = letter.replace('[name]', name)
    file = open(f'Output/ReadyToSend/{name}.txt', 'w')
    file.write(new_letter)
