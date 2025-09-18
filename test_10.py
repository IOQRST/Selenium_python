from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("http://parsinger.ru/selenium/3/3.html")
    p_text = browser.find_elements(By.TAG_NAME, "p")

    result = 0

    for item in p_text:
        result += int(item.text)

    print(result)
    browser.quit()
