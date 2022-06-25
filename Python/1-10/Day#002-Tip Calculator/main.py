""" Tip Calculator
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.01-1724 """

bill = float(input("What was your bill total?\n"))
party = int(input("How many people in your party?\n"))
tip = float(input("What percent would you like to tip? 10%, 12%, 15 etc?\n"))

total = round(bill * (1 + tip/100), 2)
share = round(total / party, 2)

print(f'Each person owes ${share:.2f}. Total due with tip ${total:.2f}')