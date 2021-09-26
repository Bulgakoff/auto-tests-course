from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(4)
    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    # print(x)
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    option_ch = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option_ch.click()
    option_r = browser.find_element_by_css_selector("[for='robotsRule']")
    option_r.click()
    time.sleep(2)
    butt = browser.find_element_by_css_selector("[type='submit']")
    butt.click()


finally:
    time.sleep(6)
    # закрываем браузер после всех манипуляций 28.86535520675919
    browser.quit()