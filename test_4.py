from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("https://parsinger.ru/selenium/3/3.2.4/index.html")
    btn_1 = browser.find_element(By.ID, "secret-key-button")
    btn_1.click()
    text = btn_1.get_attribute("data")
    print(text)
    browser.quit()
