import json
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

"""
Скрипт для извлечения JSON-данных с веб-страниц с использованием CDP
- Автоматически фильтрует только JSON-ответы
- Декодирует данные и преобразует их в Python-объекты
- Сохраняет каждый найденный JSON в отдельный файл
"""

options = Options()
options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
passw = []


# Функция для фильтрации JSON-ответов
def log_filter(log_):
    return (
        log_["method"] == "Network.responseReceived"
        and "json" in log_["params"]["response"]["mimeType"]
    )


with webdriver.Chrome(options=options) as browser:
    browser.get("http://31.130.149.237/json_extraction")
    action = ActionChains(browser)
    time.sleep(3)

    # Если нужно — можно инициировать события тут, например клик или ввод
    # browser.find_element(...).click()
    header = browser.find_element(By.ID, "booksContainer")
    for _ in range(25):
        action.move_to_element(header).scroll_by_amount(1, 500).perform()
    # Получаем "сырые" логи производительности (Performance logs)
    logs_raw = browser.get_log("performance")

    # Фильтруем и вытаскиваем полезные JSON-сообщения
    logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

    # Счетчик найденных JSON
    json_count = 0

    print("\n" + "=" * 80)
    print("НАЧАЛО СБОРА JSON-ДАННЫХ")
    print("=" * 80 + "\n")

    # Перебираем отфильтрованные логи (только JSON-ответы)
    for log in filter(log_filter, logs):
        try:
            request_id = log["params"]["requestId"]
            resp_url = log["params"]["response"]["url"]

            json_count += 1
            print("\n" + "=" * 80)
            print(f"JSON #{json_count}")
            print(f"URL: {resp_url}")

            body = browser.execute_cdp_cmd(
                "Network.getResponseBody", {"requestId": request_id}
            )
            json_data = json.loads(body["body"])
            all_datas = json_data["data"]

            for i in all_datas:
                if "password" in i:
                    passw.append(i["password"])
            print("-".join(passw))

        except WebDriverException:
            print("Нет Body для данного запроса")
            continue
