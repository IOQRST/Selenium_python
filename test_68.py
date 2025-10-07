from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/window_size/2/index.html"

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Firefox() as browser:
    browser.get(url)
    for i in range(len(window_size_x)):
        for j in range(len(window_size_y)):
            browser.set_window_size(window_size_x[i] + 16, window_size_y[j] + 93)
            result = browser.find_element(By.ID, 'result')

            if result.text != "":
                print(result.text)
                break