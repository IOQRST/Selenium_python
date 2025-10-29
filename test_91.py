from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "http://parsinger.ru/expectations/4/index.html"


def secret_header(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""
    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            WDW(browser, 5).until(EC.element_to_be_clickable((By.ID, "btn")))
            browser.find_element(By.ID, "btn").click()
            WDW(browser, 20).until(EC.title_contains("JK8HQ"))
            result = browser.title
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


secret_header(URL)
