from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/3/3.3.1/index.html")
    driver.find_element(By.ID, "parent_id").find_element(
        By.CLASS_NAME, "child_class"
    ).click()
    print(
        driver.find_element(By.ID, "parent_id")
        .find_element(By.CLASS_NAME, "child_class")
        .get_attribute("password")
    )
    driver.quit()
