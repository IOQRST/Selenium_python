from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/3/3.html")
    p_text = driver.find_elements(By.TAG_NAME, "p")

    result = 0

    for item in p_text:
        result += int(item.text)

    print(result)
    driver.quit()