from traceback import print_tb

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("http://parsinger.ru/selenium/7/7.html")
    browser.maximize_window()
    quotes = browser.find_elements(By.TAG_NAME, "option")
    rs = browser.find_element(By.ID, "input_result")
    btn = browser.find_element(By.CLASS_NAME, "btn")

    result = 0

    for item in quotes:
        result += int(item.text)

    rs.send_keys(result)
    btn.click()
    print(browser.find_element(By.ID, "result").text)
