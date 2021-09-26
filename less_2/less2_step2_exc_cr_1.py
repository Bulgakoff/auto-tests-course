import math
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # time.sleep(2)
    el_butt = browser.find_element_by_id('input_value')
    print(el_butt.text)
    res_val_str = calc(el_butt.text)
    print(type(res_val_str), res_val_str)
    butt = browser.find_element_by_css_selector('[type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', butt)
    # time.sleep(2)

    inpun_field = browser.find_element_by_id('answer')
    inpun_field.send_keys(res_val_str)
    # time.sleep(2)
    browser.execute_script('return arguments[0].scrollIntoView(true);', butt)

    browser.find_element_by_id('robotCheckbox').click()
    # time.sleep(2)
    browser.find_element_by_id('robotsRule').click()
    # time.sleep(4)

    browser.execute_script('return arguments[0].scrollIntoView(true);', butt)

    butt.submit()
    # time.sleep(4)

    # 2.3728685218473275

finally:
    time.sleep(5)
    browser.quit()
