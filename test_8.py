from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/1/1.html")
    input_list = driver.find_elements(By.CLASS_NAME, "form")
    button = driver.find_element(By.ID, "btn")

    for item in input_list:
        item.send_keys("Текст")
    button.click()
    result = driver.find_element(By.ID, "result").text
    print(result)
    driver.quit()