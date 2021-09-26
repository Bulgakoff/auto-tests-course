from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
prompt = browser.switch_to.alert
prompt.send_keys('qweqwe_qwe')
time.sleep(4)
prompt.accept()
