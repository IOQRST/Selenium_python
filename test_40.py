import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()

url = "https://parsinger.ru/selenium/7/7.1/index.html"

with webdriver.Firefox(options=options) as browser:
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    print(browser.find_element(By.ID, "secret-container").text)
