from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("http://parsinger.ru/selenium/1/1.html")
    input_list = browser.find_elements(By.CLASS_NAME, "form")
    button = browser.find_element(By.ID, "btn")

    for item in input_list:
        item.send_keys("Текст")
    button.click()
    result = browser.find_element(By.ID, "result").text
    print(result)
    browser.quit()
