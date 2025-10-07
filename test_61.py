import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
# opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/8/8.4.2/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    for count in range(1, 5):
        iframe = browser.find_element(By.ID, f"frame{count}")
        browser.switch_to.frame(iframe)
        if iframe.get_attribute("id") == "frame4":
            print(browser.find_element(By.TAG_NAME, "h2").text)
        else:
            browser.find_element(By.TAG_NAME, "button").click()
            time.sleep(2)
            browser.switch_to.default_content()
