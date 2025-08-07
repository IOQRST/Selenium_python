from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://parsinger.ru/selenium/2/2.html")
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "16243162441624")
    link.click()
    print(driver.find_element(By.ID, "result").text)
    driver.quit()