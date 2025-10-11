import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URl = "https://parsinger.ru/selenium/9/9.4.2/index.html"


def hunting_numbers(url: str) -> str:
    list_nums = []
    pattern = r"\/ok\/ok"
    result = ""
    sums = 0
    with webdriver.Firefox() as browser:
        try:
            # Открываем ссылку
            browser.get(url)
            # Получаем текущий URL
            current_url = browser.current_url
            # нажимаем СТАРТ
            browser.find_element(By.ID, "startButton").click()
            # Основной цикл
            while True:
                # Начинаем проверку URL
                if WDW(browser, 20).until(EC.url_changes(current_url)):
                    purl = browser.current_url
                    # Проверяем есть ли neok в ссылке
                    if re.search(pattern, purl):
                        list_nums.append(
                            browser.find_element(By.CLASS_NAME, "number").text
                        )
                current_url = browser.current_url
                # Как только в адресе появляется index_2 прерываем цикл
                if "index_2" in current_url:
                    break
            # Считаем сумму элементов
            for i in list_nums:
                sums += int(i)

            browser.find_element(By.ID, "sumInput").send_keys(sums)
            browser.find_element(By.ID, "checkButton").click()
            result = browser.find_element(By.ID, "result").text
        finally:
            return result


print(hunting_numbers(URl))
