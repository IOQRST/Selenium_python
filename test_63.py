from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.8/1/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    result = browser.find_element(By.ID, 'result')
    
    for btn in buttons:
        btn.click()
        browser.switch_to.alert.accept()

        if result.text != "":
            print(result.text)
            break
        