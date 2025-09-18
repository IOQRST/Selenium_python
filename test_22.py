from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("https://parsinger.ru/selenium/6/6.2.1/index.html")
    img = browser.find_element(By.ID, "this_pic").screenshot(
        "./screenshots/test_22.jpg"
    )
