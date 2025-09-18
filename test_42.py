from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()

url = "http://parsinger.ru/selenium/7/7.3.1/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)

    grab = browser.find_element(By.ID, "draggable")

    action = ActionChains(browser)

    action.drag_and_drop_by_offset(grab, 0, -150).perform()

    print(browser.find_element(By.ID, "password").text)
