from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()

url = "http://parsinger.ru/scroll/4/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)

    elements = driver.find_elements(By.CLASS_NAME, "btn")
    plain_text = driver.find_element(By.ID, "result")

    values = []

    for item in elements:
        driver.execute_script("return arguments[0].scrollIntoView(true);", item)
        item.click()
        values.append(int(plain_text.text))

    print(len(values))
    print(sum(values))
