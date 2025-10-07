from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.8/5/index.html"


def introduction_to_frames(url):
    browser = webdriver.Firefox()

    try:
        browser.get(url)

        all_frames = browser.find_elements(By.TAG_NAME, "iframe")
        guess = browser.find_element(By.ID, "guessInput")
        check = browser.find_element(By.ID, "checkBtn")

        for frame in all_frames:
            browser.switch_to.frame(frame)
            browser.find_element(By.TAG_NAME, "button").click()
            potential_key = browser.find_element(By.ID, "numberDisplay").text

            browser.switch_to.default_content()

            guess.clear()
            guess.send_keys(potential_key)
            check.click()

            try:
                alert = browser.switch_to.alert
                return alert.text
            except:  # noqa: E722
                print("Alert is not opened.")

    finally:
        browser.quit()


print(introduction_to_frames(URL))
