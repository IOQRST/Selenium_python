from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/5.9/7/index.html"


def many_checkboxes(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""
    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()

            checkboxes = browser.find_elements(By.TAG_NAME, "input")
            buttons = browser.find_elements(By.TAG_NAME, "button")

            for i in range(len(checkboxes)):
                WDW(browser, 30).until(EC.element_to_be_selected(checkboxes[i]))
                buttons[i].click()

            result = browser.find_element(By.ID, "result").text.strip()
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


many_checkboxes(URL)
