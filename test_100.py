from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/draganddrop/3/index.html"


def sqare_traveller(url: str):
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            action = ActionChains(browser)
            blue_sqaure = browser.find_element(By.ID, "block1")
            points = browser.find_elements(By.CLASS_NAME, "controlPoint")

            for point in points:
                action.drag_and_drop(blue_sqaure, point).perform()

            result = browser.find_element(By.ID, "message").text.strip()
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


sqare_traveller(URL)
