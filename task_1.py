import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

URL_1 = "https://www.google.com/"
URL_2 = "https://the-internet.herokuapp.com/login"
URL_3 = "https://the-internet.herokuapp.com/dropdown"


def simple_scenario(url):
    opt = webdriver.FirefoxOptions()

    with webdriver.Firefox(options=opt) as browser:
        try:
            action = ActionChains(browser)
            browser.get(url)
            search = browser.find_element(By.ID, "APjFqb")
            action.move_to_element(search).send_keys("Selenium Python").key_down(
                Keys.ENTER
            ).perform()
            time.sleep(3)
        finally:
            browser.quit()


def work_with_elements(url):
    opt = webdriver.FirefoxOptions()

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            username = browser.find_element(By.ID, "username")
            passwd = browser.find_element(By.ID, "password")
            login = browser.find_element(By.TAG_NAME, "button")

            username.send_keys("tomsmith")
            passwd.send_keys("SuperSecretPassword")
            login.click()
        finally:
            browser.quit()


def explicit_waits(url):
    opt = webdriver.FirefoxOptions()

    with webdriver.Firefox(options=opt) as browser:
        wait = WebDriverWait(browser, timeout=3)
        try:
            browser.get(url)
            username = browser.find_element(By.ID, "username")
            wait.until(lambda _: username.is_displayed())
            passwd = browser.find_element(By.ID, "password")
            wait.until(lambda _: passwd.is_displayed())
            login = browser.find_element(By.TAG_NAME, "button")
            wait.until(lambda _: login.is_displayed())

            username.send_keys("tomsmith")
            passwd.send_keys("SuperSecretPassword")
            login.click()
        finally:
            browser.quit()


def dropdown_lists(url):
    opt = webdriver.FirefoxOptions()

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            dropdown = Select(browser.find_element(By.ID, "dropdown"))
            options_list = dropdown.options
            dropdown.select_by_visible_text('Option 1')
            if 

        finally:
            browser.quit()


# simple_scenario(URL_1)
# work_with_elements(URL_2)
# explicit_waits(URL_2)
dropdown_lists(URL_3)