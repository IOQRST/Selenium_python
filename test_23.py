from selenium import webdriver
from pprint import pprint

url = "https://ya.ru/"

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    cookies = driver.get_cookies()
    pprint(cookies)
