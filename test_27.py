from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
# opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/6/6.3.3/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    driver.add_cookie({"name": "secretKey", "value": "selenium123"})
    driver.refresh()
    driver.implicitly_wait(15)
    print(driver.find_element(By.ID, "password").text)
