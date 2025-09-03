from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/7/7.3.5/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)

    containers = driver.find_elements(By.CLASS_NAME, "scroll-container")
    action = ActionChains(driver)

    for i in containers:
        action.click(i)
        action.key_down(Keys.END)
        action.perform()
        action.key_up(Keys.END)
        action.perform()

    print(driver.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
