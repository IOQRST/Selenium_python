from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/6/6.3/index.html"

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    cookies = browser.get_cookies()

    inp = browser.find_element(By.ID, "phraseInput")
    btn = browser.find_element(By.ID, "checkButton")

    inp.send_keys(cookies[0]["name"])
    btn.click()

    print(browser.find_element(By.ID, "result").text)
