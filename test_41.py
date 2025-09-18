from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://parsinger.ru/selenium/7/7.2/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)

    list_of_elements = []

    for i in range(100):
        tag_inputs = browser.find_elements(By.TAG_NAME, "input")
        for current in tag_inputs:
            if current not in list_of_elements:
                current.send_keys("Row")
                current.send_keys(Keys.ENTER)
                current.send_keys(Keys.DOWN)
                list_of_elements.append(current)

    print(browser.find_element(By.ID, "hidden-password").text)
