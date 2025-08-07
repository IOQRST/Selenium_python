from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()

url = "https://parsinger.ru/methods/5/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    links = driver.find_elements(By.CLASS_NAME, "urls")

    cookie_list = []
    values = []

    for i in links:
        i.click()
        current_cookie = driver.get_cookies()
        number = driver.find_element(By.ID, "result").text
        number_plus_expire = {str(number): current_cookie[0]["expiry"]}
        values.append(current_cookie[0]["expiry"])
        cookie_list.append(number_plus_expire)
        driver.back()

    max_val = max(values)

    for i in cookie_list:
        for _, v in i.items():
            if v == max_val:
                print(i)
