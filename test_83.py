from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.6.1/index.html"


def dollar_course(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")
    result = ""

    with webdriver.Firefox(options=opt) as browser:
        browser.get(url)

        try:
            WDW(browser, 30).until(
                EC.text_to_be_present_in_element((By.ID, "usd-rate"), "75.50 ₽")
            )
            result = browser.find_element(By.ID, "secret-code").text
        finally:
            if result == "":
                print("Что-то пошло не так.")
            else:
                print(f"Код найден! - {result}")


dollar_course(URL)
