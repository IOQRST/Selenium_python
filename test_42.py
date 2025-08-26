from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opt = webdriver.ChromeOptions()

url = "http://parsinger.ru/selenium/7/7.3.1/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)

    grab = driver.find_element(By.ID, "draggable")

    action = ActionChains(driver)

    action.drag_and_drop_by_offset(grab, 0, -150).perform()


    print(driver.find_element(By.ID, 'password').text)