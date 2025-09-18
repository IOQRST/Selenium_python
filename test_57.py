import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/8/8.1.2/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)
    links = [
        l.get_attribute("href")
        for l in browser.find_elements(By.XPATH, "//div[@class='code-links']/a")
    ]

    numbers = []

    for link in links:
        browser.switch_to.new_window("tab")
        browser.get(link)

        time.sleep(3)

        nums = browser.find_elements(By.CLASS_NAME, "number")
        for num in nums:
            numbers.append(int(num.text))

    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.ID, "sumInput").send_keys(sum(numbers))
    browser.find_element(By.ID, "checkButton").click()

    print(browser.find_element(By.ID, "passwordDisplay").text)
