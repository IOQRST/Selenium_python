from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/draganddrop/1/index.html"


def move_red_block(url: str):
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            action = ActionChains(browser)
            red_block = browser.find_element(By.ID, "draggable")
            target = browser.find_element(By.ID, "field2")

            action.drag_and_drop(red_block, target).perform()
            result = browser.find_element(By.ID, "result").text.strip()
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


move_red_block(URL)
