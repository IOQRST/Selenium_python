from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "http://parsinger.ru/infiniti_scroll_3/"

with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)
    total = 0
    
    scrolls_areas = browser.find_elements(By.XPATH, "//div[@class='main']/div/div[1]/div[1]")

    for area in scrolls_areas:
        for i in range(10):
            action.move_to_element(area).scroll_by_amount(0, 500).perform()

    all_spans = browser.find_elements(By.XPATH, "//div[@class='main']/div/div[1]/span")

    for span in all_spans:
        total += int(span.text)

    print(total)