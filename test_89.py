from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.7.3/index.html"


def catch_the_moment(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.find_element(By.ID, "summonBtn").click()
            WDW(browser, 30).until(EC.number_of_windows_to_be(5))
            browser.find_element(By.ID, "passwordBtn").click()
            WDW(browser, 30).until(EC.alert_is_present())
            alert = browser.switch_to.alert
            result = alert.text
        finally:
            if result == "":
                print("Error")
            else:
                print(result)


catch_the_moment(URL)
