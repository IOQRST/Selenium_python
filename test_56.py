from selenium import webdriver

url1 = "https://parsinger.ru/selenium/8/8.1/site1/"
url2 = "https://parsinger.ru/selenium/8/8.1/site2/"

with webdriver.Firefox() as browser:
    browser.get("about:blank")

    browser.switch_to.new_window("tab")
    browser.get(url1)

    text = browser.title
    num1 = int(text.translate(text.maketrans({"4": "", "3": "", "9": ""})))

    browser.switch_to.new_window("tab")
    browser.get(url2)

    text = browser.title
    num2 = int(text.translate(text.maketrans({"7": "", "8": "", "0": ""})))

    print(num1 + num2)
