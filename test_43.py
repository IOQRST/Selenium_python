from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opt = webdriver.ChromeOptions()
url = "https://parsinger.ru/selenium/7/7.3.2/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    click_area = driver.find_element(By.ID, "dblclick-area")

    ActionChains(driver)\
        .move_to_element(click_area)\
        .double_click(click_area)\
        .perform()

    print(driver.find_element(By.ID, "password").text)
