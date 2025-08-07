import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--disable-features=DisableLoadExtensionCommandLineSwitch")
options_chrome.add_extension('Mouse Coordinates\\1.0.0_0.crx')

with webdriver.Chrome(options=options_chrome) as driver:
    driver.get("https://stepik.org/course/104774")
    time.sleep(20)