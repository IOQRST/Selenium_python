from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/expectations/6/index.html"


def fast_tags(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            WDW(browser, 5).until(EC.element_to_be_clickable((By.ID, "btn")))
            browser.find_element(By.ID, "btn").click()
            WDW(browser, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "BMH21YY"))
            )
            result = browser.find_element(By.CLASS_NAME, "BMH21YY").text
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


fast_tags(URL)
