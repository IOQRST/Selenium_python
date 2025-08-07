from selenium import webdriver
from selenium.webdriver.common.by import By


opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/6/6.5/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    element = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.click()
    print(driver.find_element(By.ID, "secret-key").text)
