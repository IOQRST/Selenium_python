from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
url = "https://parsinger.ru/selenium/7/7.3.2/index.html"

with webdriver.Chrome(options=opt) as browser:
    browser.get(url)
    click_area = browser.find_element(By.ID, "dblclick-area")

    ActionChains(browser).move_to_element(click_area).double_click(click_area).perform()

    print(browser.find_element(By.ID, "password").text)
