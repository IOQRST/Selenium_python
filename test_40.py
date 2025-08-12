import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

url = "https://parsinger.ru/selenium/7/7.1/index.html"

with webdriver.Chrome(options=options) as driver:
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    print(driver.find_element(By.ID, "secret-container").text)
