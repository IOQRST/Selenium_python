from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/5.5/4/1.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    gray_fields = browser.find_elements(By.XPATH, "//textarea[@color='gray']")
    blue_fields = browser.find_elements(By.XPATH, "//textarea[@color='blue']")
    button_list = browser.find_elements(
        By.XPATH, "//button[contains(text(), 'Проверить')]"
    )

    for i in range(len(gray_fields)):
        blue_fields[i].send_keys(gray_fields[i].get_attribute("value"))
        gray_fields[i].clear()
        button_list[i].click()

    button_list[-1].click()

    print(browser.find_element(By.ID, "congrats").text)
