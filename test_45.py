from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/7/7.3.4/index.html"


with webdriver.Firefox(options=opt) as browser:
    browser.get(url)
    context_area = browser.find_element(By.ID, "context-area")

    action = ActionChains(browser)
    action.context_click(context_area)
    action.perform()

    get_pass = browser.find_element(By.CSS_SELECTOR, '[data-action="get_password"]')
    action.click(get_pass)
    action.perform()

    print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
