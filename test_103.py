from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains


URL = "https://parsinger.ru/selenium/5.10/3/index.html"


def find_pair(url: str):
    opt = webdriver.FirefoxOptions()
    # opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()

            action = ActionChains(browser)

            squares = browser.find_elements(By.CLASS_NAME, "draganddrop")
            ends = browser.find_elements(By.CLASS_NAME, "draganddrop_end")

            for square in squares:
                for end in ends:
                    square_color = Color.from_string(
                        square.value_of_css_property("background-color")
                    ).rgb
                    end_color = Color.from_string(
                        end.value_of_css_property("border-color")
                    ).rgb

                    if square_color == end_color:
                        action.drag_and_drop(square, end).perform()

            result = browser.find_element(By.ID, "message").text.strip()
        finally:
            if result == "":
                print("Error")
            else:
                print(result)


find_pair(URL)
