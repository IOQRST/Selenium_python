import json
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

"""
Скрипт для извлечения JSON-данных с веб-страниц с использованием CDP
- Автоматически фильтрует только JSON-ответы
- Декодирует данные и преобразует их в Python-объекты
- Сохраняет каждый найденный JSON в отдельный файл
"""

options = Options()
options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

lst = []


# Функция для фильтрации JSON-ответов
def log_filter(log_):
    return (
        log_["method"] == "Network.responseReceived"
        and "json" in log_["params"]["response"]["mimeType"]
    )


with webdriver.Chrome(options=options) as browser:
    browser.get("http://31.130.149.237/json_extraction")
    time.sleep(2)

    # Если нужно — можно инициировать события тут, например клик или ввод
    # browser.find_element(...).click()

    # Получаем "сырые" логи производительности (Performance logs)
    logs_raw = browser.get_log("performance")

    # Фильтруем и вытаскиваем полезные JSON-сообщения
    logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

    # Счетчик найденных JSON
    json_count = 0

    # Перебираем отфильтрованные логи (только JSON-ответы)
    for log in filter(log_filter, logs):
        try:
            request_id = log["params"]["requestId"]
            resp_url = log["params"]["response"]["url"]

            json_count += 1
            # print("\n" + "=" * 80)
            # print(f"JSON #{json_count}")
            # print(f"URL: {resp_url}")

            body = browser.execute_cdp_cmd(
                "Network.getResponseBody", {"requestId": request_id}
            )
            json_data = json.loads(body["body"])
            all_datas = json_data["data"]

            for i in all_datas:
                lst.append(i["id"])
                lst.append(i["year"])
                lst.append(i["price"])

            print(sum(lst))
        except WebDriverException:
            print("Нет Body для данного запроса")
            continue
