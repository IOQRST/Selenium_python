import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=chrome')
chrome_options.add_extension('Mouse Coordinates\\1.0.0_0.crx')

with webdriver.Chrome(options=chrome_options) as driver:
    driver.get('https://yandex.ru/')
    time.sleep(15)
    a = driver.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))