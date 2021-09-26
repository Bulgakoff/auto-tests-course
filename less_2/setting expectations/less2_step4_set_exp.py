import math
from selenium import webdriver
import time

link = ' http://suninjuly.github.io/cats.html'

try:

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    print(browser.current_url)
    browser.find_element_by_id('button')
finally:
    time.sleep(5)

    browser.quit()
