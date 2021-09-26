from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Alexei")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Bulgakov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Bali")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Indonesia")
    spam = '//button[text()="Submit"]'

    button = browser.find_element_by_xpath(spam)
    button.click() # 25.25621666579341



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
