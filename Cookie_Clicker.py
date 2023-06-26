from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from multiprocessing import Process

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")

button_cookie = driver.find_element(By.ID, "cookie")



def get_upgrade():
    store = driver.find_elements(By.CSS_SELECTOR, "body #game #rightPanel #store div")
    store.pop(-1)

    for item in store[::-1]:
        if item.get_attribute("class") != "grayed":
            item.click()
            break

def get_cookie():
    end = time.time() + 5
    while end > time.time():
        button_cookie.click()

end_time = time.time() + (60)

while end_time > time.time():
    get_cookie()
    get_upgrade()

cps = driver.find_element(By.ID, "cps")
print(cps.text)
