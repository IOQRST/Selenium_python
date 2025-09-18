from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()

# url = "https://parsinger.ru/selenium/5.5/5/test/test.html"
url = "https://parsinger.ru/selenium/5.5/5/1.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)

    color_codes = [x.text for x in browser.find_elements(By.TAG_NAME, "span")]
    selects = browser.find_elements(By.TAG_NAME, "select")
    checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
    input_fields = browser.find_elements(By.XPATH, "//input[@type='text']")
    buttons = browser.find_elements(By.XPATH, "//button[contains(text(), 'Проверить')]")
    data_hex_buttons = []

    for i in range(len(color_codes)):
        data_hex_buttons.append(
            browser.find_element(
                By.XPATH,
                f"//div[{1}]/div[{i+1}]/div/button[@data-hex='{color_codes[i]}']",
            )
        )

    for i in range(len(color_codes)):
        selects[i].send_keys(color_codes[i])
        data_hex_buttons[i].click()
        checkboxes[i].click()
        input_fields[i].send_keys(color_codes[i])
        buttons[i].click()

    buttons[-1].click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
