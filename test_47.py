import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
# opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/7/7.4.1/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)

    ActionChains(browser).scroll_by_amount(0, 500).perform()
    time.sleep(4)
    code = browser.find_element(By.CLASS_NAME, "countdown")
    ActionChains(browser).scroll_from_origin(
        ScrollOrigin.from_element(code), 0, 1500
    ).perform()
    time.sleep(4)
    browser.find_element(By.TAG_NAME, "input").send_keys(code.text[5:])
    browser.find_element(By.TAG_NAME, "button").click()
    print(browser.find_element(By.ID, "final-key").text)
