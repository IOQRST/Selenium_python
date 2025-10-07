from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
# opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/8/8.4.3/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)

    for _ in range(4):
        iframe = browser.find_element(By.TAG_NAME, "iframe")
        browser.switch_to.frame(iframe)
        button = browser.find_element(By.TAG_NAME, "button")
        # FF не всегда хорошо обрабатывает нажатие по кнопке, по этому можно использовать вот это -
        browser.execute_script("arguments[0].click();", button)
        sleep(3)

    print(browser.find_element(By.CLASS_NAME, "password-container").text)
