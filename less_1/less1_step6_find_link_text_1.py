import math
import time

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(link_text) # 224592


from selenium import webdriver
from selenium.webdriver.common.by import By
#
link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
#находим ссылку по тексту ссылки
    link = browser.find_element_by_link_text(link_text) # "224592"
    link.click()
    # button = browser.find_element(By.ID, "submit_button")
    # button.click()
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Alexei")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Bulgakov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Bali")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Indonesia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click() #25.202135658949715


finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()