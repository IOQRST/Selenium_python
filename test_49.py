from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "http://parsinger.ru/infiniti_scroll_1/"

with webdriver.Firefox() as browser:
    browser.get(url)
    browser.implicitly_wait(2)
    scroll_area = browser.find_element(By.XPATH, '//div[@id="scroll-container"]')

    elements_list = []
    total = []

    while True:
        elements = browser.find_elements(By.XPATH, '//div[@id="scroll-container"]/span')
        for i in elements:
            if i not in elements_list:
                elements_list.append(i)
                if int(i.text) not in total:
                    total.append(int(i.text))
                i.click()
        ActionChains(browser).move_to_element(scroll_area).click().key_down(
            Keys.DOWN
        ).perform()
        if elements_list[-1].get_attribute("class") == "last-of-list":
            break
    print(sum(total))
