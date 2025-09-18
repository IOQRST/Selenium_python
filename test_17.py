from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.FirefoxOptions()
chrome_options.add_argument("--headless")

with webdriver.Firefox(options=chrome_options) as browser:
    browser.get("https://stepik.org/course/104774")
    a = browser.find_element(By.TAG_NAME, "a")
    print(a.get_attribute("href"))
