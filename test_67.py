from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/window_size/1/"

with webdriver.Firefox() as browser:
    browser.get(url)
    browser.set_window_size(555 + (555 - 539), 555 + (555 - 462))
    print(browser.find_element(By.ID, 'result').text)