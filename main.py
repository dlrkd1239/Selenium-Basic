from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_driver_path = 'C:/Users/dlrkd/Desktop/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome()

driver.get("https://python.org")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")#By.ID, NAME, TAG_NAME, CSS_SELECTOR
# #driver.find_element(By.CSS_SELECTOR, ".CLASSNAME a") # By.XPATH wolud be come in handy.

menu_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
menu_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
event_dict = {}

for i in range(len(menu_events)):
    event_dict[i]= {
        "time": menu_times[i].text,
        "name": menu_events[i].text
    }

pprint(event_dict)