from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/draganddrop/2/index.html"


def orange_circle_movement(url: str):
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            action = ActionChains(browser)

            circle = browser.find_element(By.ID, "draggable")
            blocks = browser.find_elements(By.CLASS_NAME, "box")

            for block in blocks:
                action.drag_and_drop(circle, block).perform()

            result = browser.find_element(By.ID, "message").text.strip()

        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


orange_circle_movement(URL)
