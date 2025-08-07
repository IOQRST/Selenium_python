from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/selenium/6/6.html')
    driver.maximize_window()

    number = ((12434107696 * 3) * 2) + 1

    # element = driver.find_element(By.XPATH, f'//option[contains(), {str(number)}]')
    select = driver.find_element(By.ID, 'selectId')
    btn = driver.find_element(By.CLASS_NAME, 'btn')

    select.send_keys(str(number))

    btn.click()

    print(driver.find_element(By.ID, 'result').text)