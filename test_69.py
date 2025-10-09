from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

url = "http://parsinger.ru/window_size/2/index.html"

def find_window_size(url):
    with webdriver.Chrome() as driver:
        driver.get(url)
        
        # Устанавливаем начальный размер для расчета рамок
        driver.set_window_size(1000, 1000)
        time.sleep(1)  # Даем время на применение размера
        
        # Более точный способ получить размеры рабочей области
        viewport_width = driver.execute_script("return document.documentElement.clientWidth")
        viewport_height = driver.execute_script("return document.documentElement.clientHeight")
        outer_width = driver.execute_script("return window.outerWidth")
        outer_height = driver.execute_script("return window.outerHeight")
        
        frame_width = outer_width - viewport_width
        frame_height = outer_height - viewport_height
        
        print(f"Размеры рамок: {frame_width}x{frame_height}")
        
        result_value = None
        
        # Перебираем комбинации
        for width in window_size_x:
            for height in window_size_y:
                total_width = width + frame_width
                total_height = height + frame_height
                
                driver.set_window_size(total_width, total_height)
                time.sleep(0.1)  # Короткая пауза для применения размера
                
                try:
                    # Используем явное ожидание вместо неявного
                    result_element = WebDriverWait(driver, 0.5).until(
                        EC.presence_of_element_located((By.ID, "result"))
                    )
                    result_text = result_element.text.strip()
                    
                    # Проверяем, является ли содержимое числом
                    if result_text and result_text.isdigit():
                        print(f"Найдено при размере: {width}x{height}, результат: {result_text}")
                        result_value = {'width': width, 'height': height, 'code': result_text}
                        break  # Выходим из внутреннего цикла
                        
                except Exception as e:
                    # Игнорируем исключения при поиске и продолжаем
                    continue
            
            if result_value:
                break  # Выходим из внешнего цикла если нашли результат
        
        return result_value

# Запускаем поиск
result = find_window_size(url)
if result:
    print(f"Успех! Найден размер: {result['width']}x{result['height']}")
    print(f"Код: {result.get('code', 'не найден')}")
else:
    print("Подходящий размер окна не найден")