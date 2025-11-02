from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/5.10/8/index.html"


def distant_goal(url: str):
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()

            action = ActionChains(browser)
            message_box = browser.find_element(By.ID, "message")
            distant = 115

            circles = browser.find_elements(By.CLASS_NAME, "piece")

            for circle in circles:
                action.drag_and_drop_by_offset(circle, distant, 0).perform()
                distant += 100

            WDW(browser, 20).until(EC.visibility_of(message_box))
            result = message_box.text.strip()
        finally:
            if result == "":
                print("Error")
            else:
                print(result)


distant_goal(URL)
