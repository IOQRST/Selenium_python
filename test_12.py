from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/4/4.html")
    driver.maximize_window()
    all_checkboxes = driver.find_elements(By.CLASS_NAME, "check")
    btn = driver.find_element(By.XPATH, "//div/input[@class='btn']")
    result_element = driver.find_element(By.XPATH, "//div/p[@id='result']")

    for checkbox in all_checkboxes:
        checkbox.click()

    btn.click()

    print(result_element.text)
    driver.quit()