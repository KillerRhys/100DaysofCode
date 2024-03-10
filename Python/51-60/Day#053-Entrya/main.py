""" Entrya-Housing Data Entry
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.03.08(1747) """


# Imports.
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from time import sleep

# Constants.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7",
}

ADDRESSES = []
PRICES = []
LINKS = []

DOCUMENT_LINK = os.environ.get('FORM_LINK')
ZILLOW_URL = ('https://www.zillow.com/tn/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22'
              'north%22%3A40.69259158075672%2C%22south%22%3A30.660925320858446%2C%22east%22%3A-81.01827185156249%2'
              'C%22west%22%3A-90.93892614843749%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globa'
              'lrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22max%22%3A100000%7D%2'
              'C%22mp%22%3A%7B%22max%22%3A498%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22ac%22%3A%7B%22value%22%3A'
              'true%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22sche%22%3A%7B%22value%22%3Afalse%7D%2C%22schm%22%3'
              'A%7B%22value%22%3Afalse%7D%2C%22schh%22%3A%7B%22value%22%3Afalse%7D%2C%22schp%22%3A%7B%22value%22%3'
              'Afalse%7D%2C%22schr%22%3A%7B%22value%22%3Afalse%7D%2C%22schc%22%3A%7B%22value%22%3Afalse%7D%2C%22sc'
              'hu%22%3A%7B%22value%22%3Afalse%7D%2C%22pnd%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3'
              'Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A53%2C%22regionType%22%3A2%7D%5D%2C%22paginat'
              'ion%22%3A%7B%7D%2C%22mapZoom%22%3A7%7D')


# Fetches data from Pre-configured Zillow search and scrapes targeted info.
response = requests.get(ZILLOW_URL, headers=HEADERS)
response.raise_for_status()
html = response.text.encode('ascii', 'ignore')

soup = BeautifulSoup(html, 'lxml')
addresses = soup.find_all("address")
for item in addresses:
    ADDRESSES.append(item.get_text())

prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine-srp-8-100-1__sc-16e8gqd-1 keDkae")
for item in prices:
    PRICES.append(item.get_text())


links = soup.find_all(class_='StyledPropertyCardDataArea-c11n-8-100-1__sc-10i1r6-0 duMycf property-card-link')
for link in links:
    LINKS.append(link.get("href"))


# Setup selenium.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(DOCUMENT_LINK)
sleep(3)

# Fills out each form until lists are cleared.
reports_to_file = len(ADDRESSES)
while reports_to_file > 0:
    address_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/'
                                                        'div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/'
                                                      'div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/'
                                                     'div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address_field.send_keys(ADDRESSES[0])
    price_field.send_keys(PRICES[0])
    link_field.send_keys(LINKS[0])
    submit_button.click()
    sleep(1)
    another_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_button.click()
    ADDRESSES.pop(0)
    PRICES.pop(0)
    LINKS.pop(0)
    sleep(1)
    reports_to_file -= 1


print('finished!')
driver.quit()
