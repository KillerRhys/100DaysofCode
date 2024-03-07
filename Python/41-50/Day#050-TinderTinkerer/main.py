""" Tinder Tinkerer
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.02.27(1700) """

# Imports.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time
import os

# Constants.
URL = "https://tinder.com/"
USER = os.environ.get("USER")
PW = os.environ.get("PW")
DEFAULT_SLEEP = 1
SWIPES = 100

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.maximize_window()
# frame_1 = driver.find_element(By.CSS_SELECTOR, 'iframe[title="Tinder | Dating, Make Friends & Meet New People"')
time.sleep(DEFAULT_SLEEP)

cookies_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[2]/div"
                                                     "/div/div[1]/div[1]/button/div[2]/div[2]")
cookies_button.click()
time.sleep(DEFAULT_SLEEP)

login_button = driver.find_element(By.LINK_TEXT, value="Log in")
login_button.click()
time.sleep(DEFAULT_SLEEP)

frame_2 = driver.find_element(By.CSS_SELECTOR, 'iframe[title="Sign in with Google Button"')
driver.switch_to.frame(frame_2)
time.sleep(DEFAULT_SLEEP)
google_button = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[2]/span[1]')
google_button.click()
time.sleep(DEFAULT_SLEEP)

driver.switch_to.window(driver.window_handles[1])
time.sleep(DEFAULT_SLEEP)

# Login with Google
email = driver.find_element(By.XPATH, value='//*[@id="identifierId"]')
email.send_keys(USER)
email.send_keys(Keys.ENTER)
time.sleep(DEFAULT_SLEEP)
password = driver.find_element(By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(PW)
password.send_keys(Keys.ENTER)
time.sleep(DEFAULT_SLEEP)

# Accept Location.
driver.switch_to.window(driver.window_handles[0])
allow_button = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div/div/div/div[3]'
                                                   '/button[1]/div[2]/div[2]')
allow_button.click()
time.sleep(1)
notifications_button = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div/div/div/'
                                                           'div[3]/button[2]/div[2]/div[2]')
notifications_button.click()
time.sleep(3)

# Like & dismiss button! # TODO add dismiss button for add tinder to home screen.
like_button = driver.find_element(By.XPATH, value='//*[@id="s1524772468"]/div/div[1]/div/main/div[2]/div'
                                                  '/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span'
                                                  '/span/svg/path')

match_dismiss = driver.find_element(By.XPATH, value='//*[@id="s981240275"]/main/div/div[1]/div/div[4]'
          
                                                    '/button/svg/path')

# Loop for matches
while SWIPES > 0:
    time.sleep(1)

    try:
        like_button.click()
        SWIPES -= 1

    except ElementClickInterceptedException:
        try:
            match_dismiss.click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()
