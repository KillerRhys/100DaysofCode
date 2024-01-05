""" Quote Grabber
    Coded by TechGYQ
    www.mythosworks.com
    2023.11.13-1804 """

import random


def daily_motivation():
    # Imports quotes.dat into list Needs failsafe.
    quotes = open("resources/quotes.dat", 'r').readlines()

    # Selects today's quote.
    quote_today = random.choice(quotes)
    quote = quote_today[: quote_today.index('",') + 1]

    # return quote_today for update!
    return quote
