from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/scroll/2/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")

    for i in checkboxes:
        i.click()
        
    numbers = driver.find_elements(By.TAG_NAME, "span")

    result = 0
    for i in numbers:
        if i.text.isdigit():
            result += int(i.text)

    print(result)