""" Stock Stalker
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.01.30-2208 """

# Imports.
import requests
import os

# Statics.
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API Parameters.
stock_parameters = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK_NAME,
    "apikey": os.environ.get('STOCK_API_KEY'),
}

# Grab data from API.
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()['Time Series (Daily)']

data_set = [value for (key, value) in data.items()]

# Get yesterdays closing value.
yesterday_closing_value = data_set[0]['4. close']

# Get day before closing value.
day_before_closing_value = data_set[1]["4. close"]

# Calculate difference in day before / yesterday / percentage.
difference = (float(yesterday_closing_value) - float(day_before_closing_value))
percentage = round((difference / float(yesterday_closing_value)) * 100)
up_down = None
if difference > 0:
    up_down = "^"
else:
    up_down = "x"

# If difference is 5 or greater fetch news.
if abs(difference) > 0.5:
    news_parameters = {
        "q": STOCK_NAME,
        "apikey": os.environ.get('NEWS_API_KEY'),
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()['articles'][:3]
    print(articles)
    news = [f"{STOCK_NAME}: {up_down} {difference} \nHeadline: {article['title']}. \nStory: {article['description']}"
            for article in articles]
    for item in news:
        print(item)

# TODO 9. - configure with twilio to send messages or smtplib.
