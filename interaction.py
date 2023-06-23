from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://en.wikipedia.org")
#
# # num_docs = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # view_history = driver.find_element(By.LINK_TEXT, "View history")
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
# while True:
#     pass

driver.get("https://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

f_name.send_keys("jo")
l_name.send_keys("yigang")
email.send_keys("dlrkd1122@gmail.com")
email.send_keys(Keys.ENTER)

while True:
    pass
