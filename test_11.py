from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    result = 0

    browser.get("http://parsinger.ru/selenium/3/3.html")
    every_second = browser.find_elements(By.XPATH, "//div/p[2]")

    for num in every_second:
        result += int(num.text)

    print(result)
    browser.quit()
