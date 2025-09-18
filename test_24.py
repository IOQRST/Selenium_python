from selenium import webdriver

url = "https://parsinger.ru/selenium/6/6.3.1/index.html"

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    token = browser.get_cookie("token_22")
    print(token["value"])
