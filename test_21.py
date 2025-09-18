import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("https://parsinger.ru/selenium/6/6.2/index.html")
    btn_1 = browser.find_element(By.TAG_NAME, "a")
    btn_1.click()
    btn_2 = browser.find_element(By.TAG_NAME, "a")
    btn_2.click()

    browser.back()
    browser.back()

    btn_3 = browser.find_element(By.TAG_NAME, "button")
    btn_3.click()

    time.sleep(20)  # import time
