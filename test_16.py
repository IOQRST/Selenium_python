import time

from selenium import webdriver

options_chrome = webdriver.FirefoxOptions()
options_chrome.add_argument("--disable-features=DisableLoadExtensionCommandLineSwitch")
options_chrome.add_extension("Mouse Coordinates\\1.0.0_0.crx")

with webdriver.Firefox(options=options_chrome) as browser:
    browser.get("https://stepik.org/course/104774")
    time.sleep(20)
    time.sleep(20)
