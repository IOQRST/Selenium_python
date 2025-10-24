from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.6.4/index.html"


def protect_success(url: str) -> str:
    opt = webdriver.FirefoxOptions()

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            WDW(browser, 30).until(
                EC.element_attribute_to_include((By.ID, "booking-number"), "confirmed")
            )
            browser.find_element(By.ID, "booking-input").send_keys(
                browser.find_element(By.ID, "booking-number").text
            )
            browser.find_element(By.ID, "check-button").click()
            result = browser.find_element(By.CLASS_NAME, "password-value").text
        finally:
            if result == "":
                print("Error")
            else:
                print(result)


protect_success(URL)
