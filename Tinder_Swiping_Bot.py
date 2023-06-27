from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import environ
import time

driver = webdriver.Chrome()

driver.get("https://tinder.com/ko")
time.sleep(3)

def login():
    driver.find_elements(By.CLASS_NAME, "w1u9t036")[1].click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="q1595321969"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.NAME, "email").send_keys(environ.get("username"))
    driver.find_element(By.NAME, "pass").send_keys(environ.get("password") + Keys.ENTER)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)

login()
driver.find_element(By.XPATH, '//*[@id="q1595321969"]/main/div[1]/div/div/div[3]/button[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="q1595321969"]/main/div[1]/div/div/div[3]/button[1]').click()
time.sleep(10)

while True:
    #driver.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)