from traceback import print_tb

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/selenium/7/7.html')
    driver.maximize_window()
    quotes = driver.find_elements(By.TAG_NAME, 'option')
    rs = driver.find_element(By.ID, 'input_result')
    btn = driver.find_element(By.CLASS_NAME, 'btn')

    result = 0

    for item in quotes:
        result += int(item.text)

    rs.send_keys(result)
    btn.click()
    print(driver.find_element(By.ID, 'result').text)