from selenium import webdriver
from selenium.webdriver.common.by import By
import re

opt = webdriver.FirefoxOptions()
opt.add_argument('--headless')

url = "https://parsinger.ru/selenium/8/8.4.1/"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    iframe = browser.find_element(By.CSS_SELECTOR, 'iframe')
    browser.switch_to.frame(iframe)
    source = browser.page_source

    letters = re.findall('\*([a-zA-Z])', source)

    print(''.join(letters))