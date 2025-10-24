from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.6.2/index.html"


def forgotten_recept(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    with webdriver.Firefox(options=opt) as browser:
        browser.get(url)
        result = ""

        try:
            browser.find_element(By.ID, "ask-jaskier").click()
            WDW(browser, 30).until(
                EC.text_to_be_present_in_element_value(
                    (By.ID, "recipe_field"), "Селениумий"
                )
            )
            WDW(browser, 30).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            result = browser.find_element(By.ID, "password").text
        finally:
            if result == "":
                print("Задача не была выполнена.")
            else:
                print(f"Задача была выполнена. Код - {result}")


forgotten_recept(URL)
