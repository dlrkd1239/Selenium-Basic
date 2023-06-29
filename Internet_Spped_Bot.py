from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import environ
from time import sleep
from datetime import datetime

PROMISED_DOWN = 150
PROMISED_UP = 100
TWIT_USERNAME = environ.get("twit_username")
TWIT_PASSWORD = environ.get("twit_password")


class InternetSpeedTwitterBot:
    def __init__(self, PROMISED_DOWN, PROMISED_UP):
        self.driver = webdriver.Chrome()
        self.down = None
        self.up = None

    def get_internet_speed(self):
        SPEED_CHECKER_URL = "https://www.speedtest.net/"
        self.driver.get(SPEED_CHECKER_URL)
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
            self.twit_at_provider()

    def twit_at_provider(self):
        TWITTER_URL = "https://twitter.com/i/flow/login"
        self.driver.get(TWITTER_URL)
        sleep(10)
        self.driver.find_element(By.NAME, "text").send_keys(TWIT_USERNAME + Keys.ENTER)
        sleep(5)
        try:
            self.driver.find_element(By.NAME, "text").send_keys("dlrkd1239" + Keys.ENTER)
            sleep(5)
        finally:
            self.driver.find_element(By.NAME, "password").send_keys(TWIT_PASSWORD + Keys.ENTER)
            sleep(5)
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div').click()
        except:
            pass
        finally:
            self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr').send_keys(
                f"This is Internet Speed Twitter Bot."
                f"\nDownload : {self.down} Mbps."
                f"\nUpload : {self.up} Mbps."
                f"\n{datetime.now()}")
            self.driver.find_element(By.XPATH,
                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]').click()
        pass


istb = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)

istb.get_internet_speed()
