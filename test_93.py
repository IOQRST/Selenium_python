from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/5.9/2/index.html"


def hiding_block(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            WDW(browser, 30).until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click()
            alert = browser.switch_to.alert
            result = alert.text
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


hiding_block(URL)
