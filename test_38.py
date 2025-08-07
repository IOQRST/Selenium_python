from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()

url = "https://parsinger.ru/methods/3/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    cookies_values = [int(x["value"]) for x in driver.get_cookies()]
    print(sum(cookies_values))
