from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    element_picture = browser.find_element_by_id("treasure")
    chest_valuex=element_picture.get_attribute("valuex")
    print(f'=======> {chest_valuex}')
    y = calc(chest_valuex)
    input_text = browser.find_element_by_id("answer")
    input_text.send_keys(y)
    time.sleep(2)

    el_chbox = browser.find_element_by_id("robotCheckbox")
    el_chbox.click()
    time.sleep(2)

    el_radio_rob = browser.find_element_by_id("robotsRule")
    el_radio_rob.click()
    time.sleep(2)

    el_but = browser.find_element_by_css_selector("[type='submit']")
    el_but.click()

finally:
    time.sleep(6)
    # закрываем браузер после всех манипуляций 28.866345122441444
    browser.quit()