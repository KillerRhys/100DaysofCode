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
        self.connection = postman.SMTP("smtp.gmail.com")
        self.connection.starttls()

        # Datetime variables.
        self.today = dt.datetime.now()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.day_of_the_week = self.today.weekday()

        # Quote Variables.
        self.quote = quotes.daily_motivation()

        # Birthday variables.
        self.birthday = nameday.get_nameday()

        # Weather Variables.
        self.area = "Dayton, US"
        self.weather = weather.daily_weather(self.area)

    # Gathers news based on area.
    def daily_news(self):
        # TODO fetch local news
        pass

    # Checks today's date against list of birthdays and e-mails a card if matched.
    def birthdays_today(self):
        today = str(self.today)
        for key, value in self.birthday.items():
            if value[5:7] == today[5:7]:
                if value[9:10] == today[9:10]:
                    age = int(self.year) - int(value[0:4])
                    # Select birthday message. Insert age and e-mail!
