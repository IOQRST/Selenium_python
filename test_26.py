from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/6/6.3.2/index.html"

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    driver.delete_all_cookies()
    driver.implicitly_wait(1)
    print(driver.find_element(By.ID, "password").text)
