from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://parsinger.ru/selenium/7/7.5/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)
    cards = []
    container = browser.find_element(By.ID, "container")
    total = 0

    while True:
        action.move_to_element(container).click().key_down(Keys.END).perform()

        current_cards = browser.find_elements(By.CLASS_NAME, "card")

        for i in current_cards:
            if i not in cards:
                cards.append(i)

        if len(cards) == 100:
            break

    for card in cards:
        card.find_element(By.CLASS_NAME, "like-btn").click()
        total += int(card.find_element(By.CLASS_NAME, "big-number").text)

    print(total)
