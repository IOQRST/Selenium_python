import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("https://2ip.ru/")
    time.sleep(3)
    print(
        browser.find_element(By.ID, "d_clip_button")
        .find_element(By.TAG_NAME, "span")
        .text
    )
    time.sleep(5)
