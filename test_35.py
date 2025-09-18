from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()

url = "https://parsinger.ru/selenium/5.5/3/1.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    all_text_areas = browser.find_elements(By.TAG_NAME, "textarea")
    all_checkboxes = browser.find_elements(By.CLASS_NAME, "checkbox")

    checked = []

    for i in range(len(all_checkboxes)):
        if all_checkboxes[i].is_selected():
            checked.append(int(all_text_areas[i].get_attribute("value")))

    print(sum(checked))
