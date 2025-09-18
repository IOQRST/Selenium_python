from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/8/8.2.1/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)
    browser.set_window_size(1200, 700)
    browser.find_element(By.ID, "checkSizeBtn").click()
    print(browser.find_element(By.ID, "secret").text)
