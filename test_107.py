from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/draganddrop/4/index.html"


# Опять, непонятно почему, но работает только в этом долбанном хроме.
def wonder_word(url: str):
    opt = webdriver.ChromeOptions()
    # И без headless режима, потому что не получится увидеть этот окаянный парль.
    # opt.add_argument("--headless")

    result = ""

    with webdriver.Chrome(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()

            action = ActionChains(browser)

            passw = browser.find_element(By.ID, "password")
            word = browser.find_element(By.ID, "target-word").text.strip()
            letter_slots = browser.find_elements(
                By.XPATH, "//div[@id='letter-slots']/div"
            )
            alphabet = browser.find_elements(By.XPATH, "//div[@id='alphabet']/div")

            for i in range(len(word)):
                for letter in alphabet:
                    if word[i] == letter.text.strip():
                        action.click_and_hold(letter).move_to_element(
                            letter_slots[i]
                        ).release().perform()

            WDW(browser, 20).until(EC.visibility_of(passw))
            result = passw.text.strip()
        finally:
            if result == "":
                print("ERROR")
            else:
                print(result)


wonder_word(URL)
