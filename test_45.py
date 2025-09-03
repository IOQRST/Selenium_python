from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

url = 'https://parsinger.ru/selenium/7/7.3.4/index.html'


with webdriver.Chrome(options=opt) as driver:
    driver.get(url)
    context_area = driver.find_element(By.ID, 'context-area')

    action = ActionChains(driver)
    action.context_click(context_area)
    action.perform()

    get_pass = driver.find_element(
        By.CSS_SELECTOR, '[data-action="get_password"]')
    action.click(get_pass)
    action.perform()

    print(driver.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
