from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/6/6.5/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    element = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.click()
    print(browser.find_element(By.ID, "secret-key").text)
