from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/5.9/6/index.html"


def mystery_checkbox(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()
            WDW(browser, 20).until(
                EC.element_to_be_selected(browser.find_element(By.ID, "myCheckbox"))
            )
            browser.find_element(By.TAG_NAME, "button").click()

            result = browser.find_element(By.ID, "result").text

        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


mystery_checkbox(URL)
