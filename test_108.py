from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/stealth/1/index.html"


def get_code(url: str):
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")

    with webdriver.Chrome(options=opt) as browser:
        browser.get(url)
        return browser.find_element(By.ID, "verification-code").text.strip()


def hiding(url: str, code: str):
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    # Ну, короче движок. Опять работает только в хроме.
    opt.add_argument("--disable-blink-features=AutomationControlled")

    result = ""

    with webdriver.Chrome(options=opt) as browser:
        try:
            browser.get(url)
            secret = browser.find_element(By.ID, "secret")
            browser.find_element(By.ID, "verification-input").send_keys(code)
            browser.find_element(By.ID, "check-button").click()

            result = WDW(browser, 20).until(EC.visibility_of(secret)).text.strip()
        finally:
            if result == "":
                print("Error")
            else:
                print(result)


hiding(URL, get_code(URL))
