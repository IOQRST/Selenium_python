from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "http://parsinger.ru/expectations/3/index.html"


def waiting_title(url: str) -> str:
    opt = webdriver.FirefoxOptions()

    result = ""
    try:
        with webdriver.Firefox(options=opt) as browser:
            browser.get(url)
            btn_locator = browser.find_element(By.ID, "btn")
            WDW(browser, 5).until(EC.element_to_be_clickable((By.ID, "btn")))
            btn_locator.click()
            WDW(browser, 30).until(EC.title_contains("345FDG3245SFD"))

            result = browser.find_element(By.ID, "result").text
    finally:
        if result == "":
            print("Error")
        else:
            print(result)


waiting_title(URL)
