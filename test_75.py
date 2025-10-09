from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://parsinger.ru/selenium/9/9.3.1/index.html"


# Опять шляпа, которая нормально работает только с хромом.
def implicit_waits(url: str):
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.maximize_window()

    try:
        browser.get(url)
        browser.find_element(By.ID, "startButton").click()

        for _ in range(5):
            browser.find_element(By.ID, "dynamicButton").click()

        print(browser.find_element(By.ID, "secretPassword").text)
    finally:
        browser.quit()


implicit_waits(URL)
