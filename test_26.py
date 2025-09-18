from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/6/6.3.2/index.html"

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    browser.delete_all_cookies()
    browser.implicitly_wait(1)
    print(browser.find_element(By.ID, "password").text)
