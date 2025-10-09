from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.1.1/index.html"


def explicit_waits(url: str):
    with webdriver.Firefox() as browser:
        browser.get(url)
        buttons = browser.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            WDW(browser, 12).until(EC.element_to_be_clickable((button))).click()
        print(browser.find_element(By.ID, "message").text)
        print(browser.find_element(By.ID, "message2").text)


explicit_waits(URL)
