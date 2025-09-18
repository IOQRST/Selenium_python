from selenium import webdriver

opt = webdriver.FirefoxOptions()

url = "https://parsinger.ru/methods/3/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    cookies_values = [int(x["value"]) for x in browser.get_cookies()]
    print(sum(cookies_values))
