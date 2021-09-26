import math
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/wait1.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element_by_id('verify').click()
    message = browser.find_element_by_id('verify_message')
    print(message.text)
    print(browser.current_url)
    assert 'successful' in message.text
    assert "Verification was successful!" == message.text

finally:
    browser.quit()
