from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.6.3/index.html"


def nano_suit_activate(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    passwd = ""

    with webdriver.Firefox(options=opt) as browser:
        browser.get(url)
        try:
            WDW(browser, 20).until(
                EC.text_to_be_present_in_element_attribute(
                    (By.ID, "main-image"), "src", "iron_success.png"
                )
            )
            browser.find_element(By.ID, "main-image").click()
            passwd = browser.find_element(By.ID, "password").text
        finally:
            if passwd == "":
                print("Some Error")
            else:
                print(f"The password is {passwd}")


nano_suit_activate(URL)
