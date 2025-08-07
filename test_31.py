from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/methods/3/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    cookies = driver.get_cookies()

    cookies_list = []

    for i in cookies:
        number = "".join(c if c.isdigit() else " " for c in i["name"].split("_"))
        if int(number) % 2 == 0:
            cookies_list.append(int(i["value"]))

    print(sum(cookies_list))
