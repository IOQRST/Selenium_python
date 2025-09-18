from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/7/7.3.5/index.html"

with webdriver.Firefox(options=opt) as browser:
    browser.get(url)

    containers = browser.find_elements(By.CLASS_NAME, "scroll-container")
    action = ActionChains(browser)

    for i in containers:
        action.click(i)
        action.key_down(Keys.END)
        action.perform()
        action.key_up(Keys.END)
        action.perform()

    print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
