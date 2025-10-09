from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.4.4/index.html"


def changing_url(url: str):
    with webdriver.Firefox() as browser:
        browser.get(url)
        browser.find_element(By.CLASS_NAME, "btn").click()
        current_url = browser.current_url
        if WDW(browser, 30).until(EC.url_changes(current_url)):
            print(browser.find_element(By.ID, "password").text)


changing_url(URL)
