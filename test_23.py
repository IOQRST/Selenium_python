from pprint import pprint

from selenium import webdriver

url = "https://ya.ru/"

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    pprint(cookies)
    pprint(cookies)
