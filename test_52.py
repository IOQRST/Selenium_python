from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.7/1/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)

    buttons = browser.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    alert = browser.switch_to.alert
    print(alert.text)
