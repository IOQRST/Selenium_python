from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("http://parsinger.ru/selenium/4/4.html")
    browser.maximize_window()
    all_checkboxes = browser.find_elements(By.CLASS_NAME, "check")
    btn = browser.find_element(By.XPATH, "//div/input[@class='btn']")
    result_element = browser.find_element(By.XPATH, "//div/p[@id='result']")

    for checkbox in all_checkboxes:
        checkbox.click()

    btn.click()

    print(result_element.text)
    browser.quit()
