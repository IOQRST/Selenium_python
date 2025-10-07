from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
opt.add_argument('--headless')

url = "https://parsinger.ru/selenium/8/8.2.2/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    answer = browser.find_element(By.ID, "answer")
    checkBtn = browser.find_element(By.ID, "checkBtn")

    scales = browser.get_window_size()
    answer.send_keys(scales["width"] + scales["height"])
    checkBtn.click()

    print(browser.find_element(By.ID, 'resultMessage').text)
    browser.quit()
