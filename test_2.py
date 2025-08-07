import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    inp = driver.find_element(By.ID, 'codeInput')
    btn = driver.find_element(By.ID, 'clickButton')
    inp.send_keys('Дрогон')
    btn.click()
    time.sleep(10)