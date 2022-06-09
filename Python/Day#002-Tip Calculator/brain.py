""" OOP practice Coded by TechGYQ"""


class CalcSystem():
    bill = float(input("How much is the bill: "))
    party = int(input("How many people in your party: "))
    tip = float(input("What percent would you like to tip: "))

    def calculations(self):
        total = round(self.bill * (1 + self.tip / 100), 2)
        share = round(total / self.party, 2)
        print(f"Each person owes ${share: .2f}. Total due with tip ${total: .2f}")
