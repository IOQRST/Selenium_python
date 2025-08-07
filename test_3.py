import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    start = driver.find_element(By.XPATH, '//button[contains(text(), "Начать миссию")]')
    check = driver.find_element(By.ID, 'checkBtn')
    start.click()
    text = driver.find_element(By.ID, "text1").text
    inp = driver.find_element(By.ID, "userInput")
    inp.send_keys(text)
    check.click()
    time.sleep(10)