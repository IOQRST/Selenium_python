from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://parsinger.ru/blank/3/index.html"


def magical_number_hunter(url):
    with webdriver.Firefox() as browser:
        title_sum = 0
        browser.get(url)
        for page in range(1, 11):
            current_button = browser.find_element(
                By.XPATH, f"//div[@class='main']/input[@value='{page}']"
            )
            current_button.click()
            browser.switch_to.window(browser.window_handles[-1])
            browser.implicitly_wait(0.5)
            title_sum += int(browser.title)
            browser.close()
            browser.switch_to.window(browser.window_handles[0])

    return title_sum


print(magical_number_hunter(URL))
