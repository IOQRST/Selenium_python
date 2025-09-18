from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/methods/1/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)

    target = browser.find_element(By.ID, "result")

    while not target.text.isdigit():
        browser.refresh()
        target = browser.find_element(By.ID, "result")

    print(target.text)
