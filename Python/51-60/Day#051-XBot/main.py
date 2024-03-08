""" X-Bot Speed Enforcer
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.03.07(1700) """

# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

# Constants
PROMISED_DOWN = 750
PROMISED_UP = 40
TWITTER_USER = os.environ.get('USER')
TWITTER_PW = os.environ.get('PW')
SPEEDTEST_URL = 'http://www.speedtest.net'
TWITTER_URL = 'http://www.twitter.com'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


# TODO create class InternetSpeedTwitWhit():
class InternetSpeedTwitWhit:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

# TODO internet_speed() & tweet_at_provider()
    def internet_speed(self):
        sleep(2)
        self.driver.get(SPEEDTEST_URL)
        start_test = self.driver.find_element(By.CLASS_NAME, value='start-text')
        start_test.click()
        sleep(60)
        close_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                                'div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        close_button.click()
        sleep(2)
        down_speed_path = ('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                           'div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up_speed_path = ('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/'
                         'div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = float(self.driver.find_element(By.XPATH, value=down_speed_path).text)
        self.up = float(self.driver.find_element(By.XPATH, value=up_speed_path).text)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        sleep(1)
        sign_in = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                           'div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()
        sleep(2)

        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                         'div/div/div[2]/div[2]/div/div/'
                                                         'div/div[5]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                            'div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/'
                                                            'div/label/div/div[2]/div[1]/input')

        email.send_keys(TWITTER_USER)
        sleep(2)
        email.send_keys(Keys.ENTER)
        sleep(2)

        password.send_keys(TWITTER_PW)
        sleep(1)
        password.send_keys(Keys.ENTER)
        sleep(4)

        tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/'
                                                                 'header/div/div/div/div[1]/div[3]/a/div')

        tweet = (f"Hey @Spectrum, Why is my internet speed {self.down} down / {self.up} / up "
                 f"when I pay for {PROMISED_DOWN} / {PROMISED_UP}?!")
        tweet_compose.send_keys(tweet)
        sleep(2)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                                'div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/'
                                                                'div[2]/div[2]/div/div/div/div/div/span/span')
        tweet_button.click()

        sleep(3)
        self.driver.quit()


Twit = InternetSpeedTwitWhit()
Twit.internet_speed()
Twit.tweet_at_provider()
