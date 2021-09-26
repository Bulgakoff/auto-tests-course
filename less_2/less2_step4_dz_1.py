import math
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc_ln(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.implicitly_wait(5)
    price = WebDriverWait(browser,12).\
        until(
        EC.text_to_be_present_in_element((By.ID,'price'),'100')
    )
    # butt = WebDriverWait(browser,5).\
    #     until(EC.element_to_be_clickable((By.ID,"book")))
    # butt.click()
    browser.find_element_by_id('book').click()
    el_num = browser.find_element_by_id('input_value')
    print(el_num.text)

    browser.find_element_by_id('answer').send_keys(calc_ln(el_num.text))
    browser.find_element_by_id('solve').click()
    print(browser.switch_to.alert.text)


    # button = WebDriverWait(browser,5).until(
    #     EC.element_to_be_clickable((By.ID,'book'))
    # )
    # print(button.text)
    # button.click()


    # el_price = browser.find_element(By.ID,'price')
    # print(el_price.text)

    # assert '100' >= el_price.text


finally:
    time.sleep(5)
    browser.quit()
