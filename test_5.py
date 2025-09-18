from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as browser:
    browser.get("https://parsinger.ru/selenium/3/3.3.3/index.html")
    links = browser.find_elements(By.TAG_NAME, "a")
    inp = browser.find_element(By.TAG_NAME, "input")
    checker = browser.find_element(By.XPATH, '//button[contains(text(), "Проверить")]')
    list_of_values = []
    for i in links:
        if i.get_attribute("stormtrooper").isdigit():
            list_of_values.append(int(i.get_attribute("stormtrooper")))
    sum_of_stormtroopers = sum(list_of_values)
    inp.send_keys(str(sum_of_stormtroopers))
    checker.click()
    print(browser.find_element(By.ID, "feedbackMessage").text)
    browser.quit()
