import math

from selenium import webdriver
import time


def calc_ln(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    comfirm = browser.switch_to.alert
    print(comfirm.text)
    comfirm.accept()
    time.sleep(1)
    x = browser.find_element_by_id('input_value').text
    print(type(x),x)
    browser.find_element_by_id('answer').send_keys(calc_ln(x))
    browser.find_element_by_xpath\
        ('//button[@type="submit"]').click()


    time.sleep(2)
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()
finally:
    browser.quit()
