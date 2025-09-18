import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless=firefox")

with webdriver.Firefox(options=opt) as browser:
    browser.get("https://yandex.ru/")
    browser.install_addon("Mouse Coordinates\\coords-0.9.6.xpi")
    time.sleep(15)
    a = browser.find_element(By.TAG_NAME, "a")
    print(a.get_attribute("href"))
    print(a.get_attribute("href"))
