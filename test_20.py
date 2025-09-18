import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://2ip.ru/"
proxy = "8.210.83.33:80"

opt = webdriver.Firefox()
opt.add_argument("--proxy-server=%s" % proxy)

with webdriver.Firefox() as browser:
    browser.get(url)
    print(
        browser.find_element(By.ID, "d_clip_button")
        .find_element(By.TAG_NAME, "span")
        .text
    )
    time.sleep(5)
