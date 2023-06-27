from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import environ
import time

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/feed/")


def login():
    driver.find_element(By.CLASS_NAME, "main__sign-in-link").click()
    driver.find_element(By.ID, "username").send_keys(environ.get("user_name"))
    driver.find_element(By.ID, "password").send_keys(environ.get("password"))
    driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button").click()


login()
time.sleep(5)
search_bar = driver.find_element(By.CSS_SELECTOR, "#global-nav-typeahead input")
search_bar.send_keys("python")
search_bar.send_keys(Keys.ENTER)
time.sleep(5)


def save_and_follow():
    save = driver.find_elements(By.CSS_SELECTOR,
                                ".entity-result__title-text a")
    links = [item.get_attribute("href") for item in save[:3]]

    for link in links:
        time.sleep(2)
        driver.get(link)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "jobs-save-button").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "follow").send_keys(Keys.ENTER)


save_and_follow()

while True:
    pass
