import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
# opt.add_argument('--headless')

url = "https://parsinger.ru/selenium/5.5/1/1.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    inputs_list = driver.find_elements(By.CSS_SELECTOR, ".text-field")
    btn = driver.find_element(By.TAG_NAME, "button")

    for i in inputs_list:
        i.clear()

    btn.click()

    time.sleep(1)
    
    alert = driver.switch_to.alert

    print(alert.text)

    alert.accept()