from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.8/2/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)

    buttons = browser.find_elements(By.CLASS_NAME, "buttons")
    check_field = browser.find_element(By.ID, "input")
    check_button = browser.find_element(By.ID, "check")
    result = browser.find_element(By.ID, "result")

    for btn in buttons:
        btn.click()
        alert = browser.switch_to.alert
        pin = alert.text
        alert.accept()
        check_field.send_keys(pin)
        check_button.click()

        if result.text != "Неверный пин-код":
            print(result.text)
            break

    browser.quit()
