from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/methods/1/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)

    target = driver.find_element(By.ID, "result")

    while not target.text.isdigit():
        driver.refresh()
        target = driver.find_element(By.ID, "result")

    print(target.text)
