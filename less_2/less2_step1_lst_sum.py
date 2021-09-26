from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time


def calc_sum(x, y):
    return int(x) + int(y)


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    a = browser.find_element_by_id('num1')
    a = a.text
    b = browser.find_element_by_id('num2')
    b = b.text

    res = str(calc_sum(a, b))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(res)
    browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(3)

finally:
    time.sleep(6)
    # закрываем браузер после всех манипуляций 28.910906120065466 execute_script
    browser.quit()
