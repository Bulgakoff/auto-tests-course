import time
from selenium import webdriver
import os

link = 'http://suninjuly.github.io/file_input.html'

# filee = os.path(os.getcwd())


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('Алексей')
    # time.sleep(1)
    browser.find_element_by_css_selector\
        ('[placeholder="Enter last name"]').send_keys('Булгаков')
    # time.sleep(1)
    browser.find_element_by_xpath('//input[@name="email"]').send_keys("qwesd@ya.com")
    # time.sleep(1)
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    # print(cur_dir)
    # file_path_for_add = os.path.join(cur_dir, 'file_1.py')
    file_path_for_add = os.getcwd() + '/' + 'file_1.py'
    print(type(file_path_for_add),file_path_for_add)
    # time.sleep(2)
    el_file = browser.find_element_by_css_selector('[type="file"]')
    el_file.send_keys(file_path_for_add)
    # time.sleep(2)

    browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(6)
    browser.quit()
