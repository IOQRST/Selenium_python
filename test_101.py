from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.10/2/index.html"


def moving_green_squares(url: str):
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            action = ActionChains(browser)

            drag_blocks = browser.find_elements(By.CLASS_NAME, "draganddrop")
            drop_area = browser.find_element(By.CLASS_NAME, "draganddrop_end")

            for block in drag_blocks:
                action.drag_and_drop(block, drop_area).perform()

            result = browser.find_element(By.ID, "message").text.strip()
        finally:
            if result == "":
                print("Error")
            else:
                print(result)


moving_green_squares(URL)
