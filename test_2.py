import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("https://parsinger.ru/selenium/3/3.2.2/index.html")
    inp = browser.find_element(By.ID, "codeInput")
    btn = browser.find_element(By.ID, "clickButton")
    inp.send_keys("Дрогон")
    btn.click()
    time.sleep(10)
