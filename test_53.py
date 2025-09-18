from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.7/5/index.html"

with webdriver.Firefox() as browser:
    browser.get(url)
    action = ActionChains(browser)

    buttons = browser.find_elements(By.XPATH, "//div[@id='main_container']/button")

    for button in buttons:
        action.move_to_element(button).click_and_hold(button).pause(
            float(button.get_attribute("value"))
        ).release(button).perform()

    alert = browser.switch_to.alert
    print(alert.text)
