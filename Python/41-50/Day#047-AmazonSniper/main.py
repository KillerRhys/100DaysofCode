""" Price Watcher
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.02.23(1407) """

# Imports
from bs4 import BeautifulSoup
import requests
import smtplib
import os

# Request headers.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7",
}

# Constants Lists
ITEMS = []
PRICES = []

with open("items.dat", "r") as file:
    for line in file.readlines():
        line.strip("\n")
        ITEMS.append(line)

with open("prices.dat", "r") as price_file:
    for line in price_file.readlines():
        line.strip("\n")
        PRICES.append(float(line))

# Fetch item prices & email if on sale.
for item in ITEMS:
    response = requests.get(url=item, headers=HEADERS)
    response.raise_for_status()
    raw_html = response.text

    soup = BeautifulSoup(raw_html, "lxml")
    price = soup.find(class_="a-offscreen").get_text()
    price_remove_symbol = price.split("$")[1]
    price_float = float(price_remove_symbol)
    if price_float < PRICES[ITEMS.index(item)]:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=os.environ.get('email'), password=os.environ.get('password'))
        connection.sendmail(from_addr=os.environ.get('email'),
                            to_addrs=os.environ.get('email'),
                            msg=f"Subject: Price Drop!!\n {price_float} for {item}!")
