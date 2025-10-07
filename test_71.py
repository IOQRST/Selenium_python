from math import sqrt

from selenium import webdriver
from selenium.webdriver.common.by import By

sites = [
    "http://parsinger.ru/blank/1/1.html",
    "http://parsinger.ru/blank/1/2.html",
    "http://parsinger.ru/blank/1/3.html",
    "http://parsinger.ru/blank/1/4.html",
    "http://parsinger.ru/blank/1/5.html",
    "http://parsinger.ru/blank/1/6.html",
]

opt = webdriver.FirefoxOptions()

numbers = []
total = 0

with webdriver.Firefox(options=opt) as browser:
    for page in sites:
        browser.get(page)
        tabs = browser.window_handles
        browser.switch_to.window(tabs[-1])
        browser.find_element(By.CLASS_NAME, "checkbox_class").click()
        numbers.append(browser.find_element(By.ID, "result").text)
        browser.switch_to.new_window("tab")

for num in numbers:
    total += sqrt(int(num))

print(round(total, 9))
