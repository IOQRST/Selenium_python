from selenium import webdriver
from selenium.webdriver.common.by import By

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

url = "http://parsinger.ru/window_size/2/index.html"

# Эта шляпа работает только с хромом .. хз почему
def find_window_size(url):
    driver = webdriver.Chrome()
    
    try:
        driver.get(url)
        
        # Устанавливаем начальный размер для расчета рамок
        driver.set_window_size(1000, 1000)
        
        # Более точный способ получить размеры рабочей области
        viewport_width = driver.execute_script("return document.documentElement.clientWidth")
        viewport_height = driver.execute_script("return document.documentElement.clientHeight")
        outer_width = driver.execute_script("return window.outerWidth")
        outer_height = driver.execute_script("return window.outerHeight")
        
        frame_width = outer_width - viewport_width
        frame_height = outer_height - viewport_height
        
        print(f"Размеры рамок: {frame_width}x{frame_height}")
        
        # Перебираем комбинации
        for width in window_size_x:
            for height in window_size_y:
                total_width = width + frame_width
                total_height = height + frame_height
                
                driver.set_window_size(total_width, total_height)
                
                # Даем время на обновление страницы
                driver.implicitly_wait(0.5)
                
                result_element = driver.find_element(By.ID, "result")
                result_text = result_element.text.strip()
                
                # Проверяем, является ли содержимое числом
                if result_text and result_text.isdigit():
                    print(f"Найдено при размере: {width}x{height}")
                    return {'width': width, 'height': height}
        
        return None
        
    finally:
        driver.quit()

# Запускаем поиск
result = find_window_size(url)
print(f"Результат: {result}")