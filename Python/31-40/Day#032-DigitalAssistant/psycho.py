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


# The brain of the operations
class Brain:

    def __init__(self):
        # SMTP vars
        self.email = ""
        self.password = ""
        self.connection = postman.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.today = dt.datetime.now()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.day_of_the_week = self.today.weekday()
        self.quote = quotes.daily_motivation()
        self.birthday = nameday.get_nameday()
        self.area = "Dayton, US"
        self.weather = weather.daily_weather(self.area)

    def daily_news(self):
        # TODO fetch local news
        pass

    def birthdays_today(self):
        # TODO Check & email birthday cards out!
        pass
