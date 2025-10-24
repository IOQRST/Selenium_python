from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.7.1/index.html"


def order(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)

            spinner = browser.find_element(By.ID, "spinner")
            modal = browser.find_element(By.ID, "modal")

            browser.find_element(By.ID, "address").send_keys("Устьзалупинск")
            select = Select(browser.find_element(By.ID, "payment"))
            select.select_by_value("card")
            browser.find_element(By.ID, "submit-order").click()

            WDW(browser, 20).until(EC.invisibility_of_element(spinner))

            browser.find_element(By.ID, "confirm-address").click()
            WDW(browser, 20).until(EC.invisibility_of_element(modal))

            browser.find_element(By.ID, "get-code").click()

            result = browser.find_element(By.ID, "result").text
        finally:
            if result == "":
                print("Error")
            else:
                print(result)


order(URL)
