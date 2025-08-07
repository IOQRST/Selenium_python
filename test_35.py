from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()

url = "https://parsinger.ru/selenium/5.5/3/1.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    all_textareas = driver.find_elements(By.TAG_NAME, "textarea")
    all_checkboxes = driver.find_elements(By.CLASS_NAME, "checkbox")

    checked = []

    for i in range(len(all_checkboxes)):
        if all_checkboxes[i].is_selected():
            checked.append(int(all_textareas[i].get_attribute("value")))

    print(sum(checked))
