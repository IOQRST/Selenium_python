from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/5.9/3/index.html"


def display_attribute(url: str) -> str:
    opt = webdriver.FirefoxOptions()

    result = ""
    ids_to_find = [
        "xhkVEkgm",
        "QCg2vOX7",
        "8KvuO5ja",
        "CFoCZ3Ze",
        "8CiPCnNB",
        "XuEMunrz",
        "vmlzQ3gH",
        "axhUiw2I",
        "jolHZqD1",
        "ZM6Ms3tw",
        "25a2X14r",
        "aOSMX9tb",
        "YySk7Ze3",
        "QQK13iyY",
        "j7kD7uIR",
    ]
    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            for i in ids_to_find:
                WDW(browser, 60).until(EC.visibility_of_element_located((By.ID, i))).click()
            alert = browser.switch_to.alert
            result = alert.text
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


display_attribute(URL)
