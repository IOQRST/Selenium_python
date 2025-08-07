from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/6/6.3/index.html"

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    cookies = driver.get_cookies()

    inp = driver.find_element(By.ID, "phraseInput")
    btn = driver.find_element(By.ID, "checkButton")

    inp.send_keys(cookies[0]["name"])
    btn.click()

    print(driver.find_element(By.ID, "result").text)
