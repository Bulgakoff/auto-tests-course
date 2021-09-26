import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
try:
     browser = webdriver.Chrome()
     browser.get(link)
     time.sleep(4)
     # browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
     browser.find_element_by_css_selector('[type="submit"]').click()
     lst_win = browser.window_handles
     current_win = lst_win[1]
     browser.switch_to.window(current_win)
     print(browser.current_url)
     x = browser.find_element_by_id('input_value')
     print(x.text)

     browser.find_element_by_id('answer').send_keys(calc(x.text))
     browser.find_element_by_css_selector("[type='submit']").click()
     print(browser.switch_to.alert.text)
     time.sleep(2)
     browser.switch_to.alert.accept()

finally:
     browser.quit()



