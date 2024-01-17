""" Postmaster Birthday Automate
    www.mythosworks.com
    OC:2023.07.12-2211 """

import datetime as dt
import smtplib as postman
import sys
from addons import quotes
from addons import weather
# from addons import news
from addons import nameday

sys.path.insert(0, 'addons/')


# The brain of the operations, houses all class variables.
class Brain:

    def __init__(self):
        # SMTP vars
        self.email = ""
        self.password = ""
        self.inbox = ""
        self.connection = postman.SMTP("smtp.gmail.com")

        # Datetime variables.
        self.today = dt.datetime.now()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.day_of_the_week = self.today.weekday()

        # Quote Variables.
        self.quote = quotes.daily_motivation()

        # Birthday variables.
        self.birthday_cards, self.birthday_list, self.birthday_addresses = nameday.get_nameday()

        # Weather Variables.
        self.area = "Dayton, US"
        self.weather = weather.daily_weather(self.area)

    def get_daily_notifications(self):
        self.quote = quotes.daily_motivation()
        self.weather = weather.daily_weather(self.area)
        self.birthday_cards, self.birthday_list, self.birthday_addresses = nameday.get_nameday()
        self.connection.starttls()
        self.connection.login(user=self.email, password=self.password)
        self.connection.sendmail(from_addr=self.email,
                                 to_addrs=self.inbox,
                                 msg=f"Subject: Good Morning!\n\nToday's Quote: "
                                     f"{self.quote}\nToday's Weather{self.weather}!")
        for _ in self.birthday_cards:

            self.connection.sendmail(from_addr=self.email,
                                     to_addrs=self.birthday_addresses[0],
                                     msg=f"Subject: Happy Birthday!\n\n{self.birthday_cards[0]}")
            self.birthday_cards.pop(0)
            self.birthday_addresses.pop(0)

        self.connection.close()

        if len(self.birthday_cards) == 0:
            print("No birthday's today, but some this month: ")
            for item in self.birthday_list:
                print(item)

        else:
            print("Birthday's today: ")
            for item in self.birthday_list:
                print(item)

    # Gathers news based on area.
    def daily_news(self):
        # TODO fetch local news future task!
        pass
