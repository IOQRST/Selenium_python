from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.5.2/index.html"


def ghost_button(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        browser.get(url)
        find_pattern = (By.ID, "ghost-button")
        try:
            WDW(browser, 10).until(
                EC.all_of(
                    EC.presence_of_element_located((find_pattern)),
                    EC.visibility_of_element_located((find_pattern)),
                )
            )

            browser.find_element(By.ID, "ghost-button").click()
            result = browser.find_element(By.ID, "password-display").text
        finally:
            if result == "":
                print("Код не найден!")
            else:
                print(f"Ваш код {result}")


ghost_button(URL)
