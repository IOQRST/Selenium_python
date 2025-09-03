from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

url = "https://parsinger.ru/selenium/7/7.3.3/index.html"

with webdriver.Chrome(options=opt) as driver:
    driver.get(url)

    act = ActionChains(driver)
    act.key_down(Keys.CONTROL)\
        .key_down(Keys.ALT)\
        .key_down(Keys.SHIFT)\
        .key_down("T")\
        .perform()

    act.key_up(Keys.CONTROL)\
        .key_up(Keys.ALT)\
        .key_up(Keys.SHIFT)\
        .key_up("T")\
        .perform()

    print(driver.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
