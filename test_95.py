from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/5.9/4/index.html"


def advisement_conspiracy(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()

            WDW(browser, 5).until(
                EC.element_to_be_clickable((By.ID, "closeBtn"))
            ).click()
            WDW(browser, 20).until(
                EC.invisibility_of_element(browser.find_element(By.ID, "ad"))
            )
            browser.find_element(By.TAG_NAME, "button").click()
            result = browser.find_element(By.ID, "message").text
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


advisement_conspiracy(URL)
