from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.4.3/index.html"
a_url = "https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"


def accurate_url(url: str):
    with webdriver.Firefox() as browser:
        browser.get(url)
        buttons = browser.find_elements(By.CLASS_NAME, "btn")
        buttons[-1].click()
        WDW(driver=browser, timeout=20).until(EC.url_to_be(a_url))
        print(browser.find_element(By.ID, "password").text)


accurate_url(URL)
