from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color

URL = "https://parsinger.ru/selenium/5.10/4/index.html"


def automatic_ball_sort(url: str):
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()

            action = ActionChains(browser)

            balls = browser.find_elements(By.CLASS_NAME, "ball_color")
            boxes = browser.find_elements(By.CLASS_NAME, "basket_color")

            for ball in balls:
                for box in boxes:
                    ball_color = Color.from_string(
                        ball.value_of_css_property("background-color")
                    ).rgb
                    box_color = Color.from_string(
                        box.value_of_css_property("background-color")
                    ).rgb

                    if ball_color == box_color:
                        action.drag_and_drop(ball, box).perform()

            result = browser.find_element(By.CLASS_NAME, "message").text.strip()

        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


automatic_ball_sort(URL)
