from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/5.5/4/1.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    gray_fields = driver.find_elements(By.XPATH, "//textarea[@color='gray']")
    blue_fields = driver.find_elements(By.XPATH, "//textarea[@color='blue']")
    button_list = driver.find_elements(
        By.XPATH, "//button[contains(text(), 'Проверить')]"
    )

    for i in range(len(gray_fields)):
        blue_fields[i].send_keys(gray_fields[i].get_attribute("value"))
        gray_fields[i].clear()
        button_list[i].click()

    button_list[-1].click()

    print(driver.find_element(By.ID, "congrats").text)
