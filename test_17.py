from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

with webdriver.Chrome(options=chrome_options) as driver:
    driver.get('https://stepik.org/course/104774')
    a = driver.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))