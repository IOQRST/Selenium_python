from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.5.1/index.html"


def DOM_checker(url: str):
    result = ""
    with webdriver.Firefox() as browser:
        browser.get(url)
        try:
            WDW(browser, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success-checkmark"))
            )
            result = browser.find_element(By.ID, "order-number").text
        finally:
            if result == "":
                print("Код не найден!")
            else:
                print(f"Ваш код {result}")


DOM_checker(URL)
