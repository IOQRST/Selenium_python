from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/scroll/2/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")

    for i in checkboxes:
        i.click()

    numbers = browser.find_elements(By.TAG_NAME, "span")

    result = 0
    for i in numbers:
        if i.text.isdigit():
            result += int(i.text)

    print(result)
