import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

opt = webdriver.ChromeOptions()
# opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/7/7.4.1/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)

    ActionChains(driver).scroll_by_amount(0, 500).perform()
    time.sleep(4)
    code = driver.find_element(By.CLASS_NAME, "countdown")
    ActionChains(driver).scroll_from_origin(
        ScrollOrigin.from_element(code), 0, 1500
    ).perform()
    time.sleep(4)
    driver.find_element(By.TAG_NAME, "input").send_keys(code.text[5:])
    driver.find_element(By.TAG_NAME, "button").click()
    print(driver.find_element(By.ID, "final-key").text)
