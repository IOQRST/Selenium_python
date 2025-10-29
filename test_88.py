from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.7.2/index.html"


def fungle(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    with webdriver.Firefox(options=opt) as browser:
        browser.get(url)
        try:
            browser.find_element(By.CLASS_NAME, "search-box").send_keys("test")
            browser.find_element(By.ID, "search-button").click()
            old_result = browser.find_element(By.ID, "old-result")
            WDW(browser, 20).until(EC.staleness_of(old_result))
            browser.find_element(By.ID, "secret-button").click()
            result = browser.find_element(By.ID, "result").text
        finally:
            if result == "":
                print("Error")
            else:
                print(result)


fungle(URL)
