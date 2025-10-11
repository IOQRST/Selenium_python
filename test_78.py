from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html"


def abu_and_bananas(url):
    with webdriver.Firefox() as browser:
        browser.get(url)

        while True:
            browser.find_element(By.ID, "searchLink").click()
            current_url = browser.current_url

            if "qLChv49" in current_url:
                break

        browser.find_element(By.ID, "checkButton").click()

        print(browser.find_element(By.ID, "result").text)


abu_and_bananas(URL)
