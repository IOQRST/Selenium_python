from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
# opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/6/6.3.3/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    browser.add_cookie({"name": "secretKey", "value": "selenium123"})
    browser.refresh()
    browser.implicitly_wait(15)
    print(browser.find_element(By.ID, "password").text)
