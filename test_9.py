from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("http://parsinger.ru/selenium/2/2.html")
    link = browser.find_element(By.PARTIAL_LINK_TEXT, "16243162441624")
    link.click()
    print(browser.find_element(By.ID, "result").text)
    browser.quit()
