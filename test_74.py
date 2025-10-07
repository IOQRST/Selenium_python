from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.2.1/index.html"


def access_scan(url):
    browser = webdriver.Firefox()

    try:
        browser.get(url)
        browser.find_element(By.ID, "startScan").click()
        WDW(browser, 20).until(EC.title_is("Access Granted"))
        print(browser.find_element(By.ID, "password").text)

    finally:
        browser.quit()


access_scan(URL)
