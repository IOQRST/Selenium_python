from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.7/4/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)


    for i in range(10):
        last_element = browser.find_element(By.XPATH, "//div[@id='main_container']/div[last()]")
        action.move_to_element(last_element).scroll_by_amount(0, 500).perform()

    all_inputs = browser.find_elements(By.TAG_NAME, 'input')

    for current_input in all_inputs:
        if int(current_input.get_attribute('value')) % 2 == 0:
            current_input.click()

    browser.find_element(By.CLASS_NAME, 'alert_button').click()

    alert = browser.switch_to.alert
    print(alert.text)