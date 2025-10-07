import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/8/8.3.1/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)
    alert = browser.find_element(By.ID, "alertButton")
    prompt = browser.find_element(By.ID, "promptButton")
    confirm = browser.find_element(By.ID, "confirmButton")

    alert.click()
    alert_window = browser.switch_to.alert
    alert_window.accept()

    prompt.click()
    prompt_window = browser.switch_to.alert
    prompt_window.send_keys("Alert")
    prompt_window.accept()

    confirm.click()
    confirm_window = browser.switch_to.alert
    confirm_window.accept()

    time.sleep(2)

    print(browser.find_element(By.ID, "secretKey").text)

