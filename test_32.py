import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()

url = "https://parsinger.ru/selenium/5.5/2/1.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)

    field_list = driver.find_elements(By.CLASS_NAME, "text-field")
    button = driver.find_element(By.ID, "checkButton")

    for i in field_list:
        if i.get_attribute("disabled"):
            continue
        i.clear()

    button.click()

    time.sleep(1)

    alert = driver.switch_to.alert

    print(alert.text)

    alert.accept()
