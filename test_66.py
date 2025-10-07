from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.8/3/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)
    pins_codes = browser.find_elements(
        By.XPATH, "//div[@class='pins-container']/span[@class='pin']"
    )
    check_button = browser.find_element(By.ID, "check")
    result = browser.find_element(By.ID, "result")
    
    for pin in pins_codes:
        extracted_text = pin.text
        check_button.click()
        alert = browser.switch_to.alert
        alert.send_keys(extracted_text)
        alert.accept()

        if result.text != "Неверный пин-код":
            print(result.text)
            break

