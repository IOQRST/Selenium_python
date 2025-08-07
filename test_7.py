from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/3/3.3.2/index.html")
    block_list = driver.find_elements(By.XPATH, "//div[@class=\"block\"]/button")

    for item in block_list:
        item.click()

    passwd = driver.find_element(By.TAG_NAME, "password").text
    print(passwd)
    driver.quit()