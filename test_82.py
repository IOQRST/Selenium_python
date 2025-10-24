from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

URL = "https://parsinger.ru/selenium/9/9.5.3/index.html"


def waiting_products(url: str) -> str:
    opt = webdriver.FirefoxOptions()
    result = ""
    sum_of_purchase = 0

    with webdriver.Firefox(options=opt) as browser:
        browser.get(url)
        try:
            # Получаем список нужных элементов
            load_products = browser.find_element(By.ID, "showProducts")
            check_sum_field = browser.find_element(By.ID, "sumInput")
            check_sum_btn = browser.find_element(By.ID, "checkSum")

            # Запускаем загрузку продуктов
            load_products.click()

            # Ждем загрузку всех карточек
            WDW(browser, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "product"))
            )

            # Достаем из каждой карточки цену и считаем сумму
            cards = browser.find_elements(By.CLASS_NAME, "price")
            for cars in cards:
                sum_of_purchase += int(cars.text.replace("$", ""))

            # Записываем полученную сумму в поле проверки и проверяем
            check_sum_field.send_keys(sum_of_purchase)
            check_sum_btn.click()

            # Получаем код
            WDW(browser, 3).until(
                EC.visibility_of_element_located((By.ID, "secretMessage"))
            )
            result = browser.find_element(By.ID, "secretMessage").text
        finally:
            if result == "":
                print("Ошибка! Код не был найден!")
            else:
                print(f"Код получен! - {result}")


waiting_products(url=URL)
