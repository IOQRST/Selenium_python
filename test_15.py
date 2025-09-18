from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("http://parsinger.ru/selenium/6/6.html")
    browser.maximize_window()

    number = ((12434107696 * 3) * 2) + 1

    # element = browser.find_element(By.XPATH, f'//option[contains(), {str(number)}]')
    select = browser.find_element(By.ID, "selectId")
    btn = browser.find_element(By.CLASS_NAME, "btn")

    select.send_keys(str(number))

    btn.click()

    print(browser.find_element(By.ID, "result").text)
