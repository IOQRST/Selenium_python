from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/5/index.html"


def collect_secret_runes(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    # opt.add_argument("--headless")

    result = ""
    fragments = []

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()

            wait = WebDriverWait(browser, 20)

            glyphs = browser.find_elements(By.CLASS_NAME, "box_button")

            for glyph in glyphs:
                glyph.click()
                browser.find_element(By.ID, "close_ad").click()
                wait.until(
                    EC.invisibility_of_element(browser.find_element(By.ID, "ad_window"))
                )
                wait.until(lambda _: glyph.text.strip() != "")
                fragments.append(glyph.text.strip())

            result = "-".join(fragments)
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


collect_secret_runes(URL)
