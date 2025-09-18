import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://parsinger.ru/selenium/3/3.2.1/index.html")

start_button = browser.find_element(By.TAG_NAME, "button")
start_button.click()

time.sleep(10)

browser.quit()
