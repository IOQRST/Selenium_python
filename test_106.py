from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.10/6/index.html"


def sliders(url: str):
    opt = webdriver.FirefoxOptions()
    # opt.add_argument("--headless")

    result = ""

    with webdriver.Firefox(options=opt) as browser:
        try:
            browser.get(url)
            browser.maximize_window()

            actiont = ActionChains(browser)

            currents = browser.find_elements(By.CLASS_NAME, "current-value")
            targets = browser.find_elements(By.CLASS_NAME, "target-value")
            volumes = browser.find_elements(By.CLASS_NAME, "volume-slider")

            for i in range(len(volumes)):
                target_numebr = int(targets[i].text.strip())
                current_numebr = int(currents[i].text.strip())
                volume_value = int(volumes[i].get_attribute("value"))
                tick = 0

                while volume_value != target_numebr:
                    if target_numebr < current_numebr:
                        actiont.drag_and_drop_by_offset(volumes[i], tick, 0).perform()
                        tick -= 3
                        volume_value = int(volumes[i].get_attribute("value"))
                    else:
                        actiont.drag_and_drop_by_offset(volumes[i], tick, 0).perform()
                        tick += 3
                        volume_value = int(volumes[i].get_attribute("value"))

            result = browser.find_element(By.ID, "message").text.strip()

        finally:
            if result == "":
                print("Error")
            else:
                print(result)


sliders(URL)
