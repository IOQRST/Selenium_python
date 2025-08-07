from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    result = 0

    driver.get("http://parsinger.ru/selenium/3/3.html")
    every_second = driver.find_elements(By.XPATH, "//div/p[2]")

    for num in every_second:
        result += int(num.text)

    print(result)
    driver.quit()