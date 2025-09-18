from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/infiniti_scroll_2/"

with webdriver.Firefox() as browser:
    browser.get(url)
    action = ActionChains(browser)

    total = 0
    scroll = browser.find_element(By.XPATH, "//div[@id='scroll-container']/div")

    for i in range(9):
        action.move_to_element(scroll).scroll_by_amount(0, 500).perform()

    list_of_all_numbers = browser.find_elements(
        By.XPATH, "//div[@id='scroll-container']/p"
    )

    for i in list_of_all_numbers:
        total += int(i.text)

    print(total)
