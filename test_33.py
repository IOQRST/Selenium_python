from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()

url = "https://parsinger.ru/methods/5/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    links = browser.find_elements(By.CLASS_NAME, "urls")

    cookie_list = []
    values = []

    for i in links:
        i.click()
        current_cookie = browser.get_cookies()
        number = browser.find_element(By.ID, "result").text
        number_plus_expire = {str(number): current_cookie[0]["expiry"]}
        values.append(current_cookie[0]["expiry"])
        cookie_list.append(number_plus_expire)
        browser.back()

    max_val = max(values)

    for i in cookie_list:
        for _, v in i.items():
            if v == max_val:
                print(i)
