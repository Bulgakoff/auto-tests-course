import time
import math
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answer = math.log(int(time.time()))
print(answer)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    composite_text = ''
    lst_addr = ['https://stepik.org/lesson/236895/step/1',
                'https://stepik.org/lesson/236896/step/1',
                'https://stepik.org/lesson/236897/step/1',
                'https://stepik.org/lesson/236898/step/1',
                'https://stepik.org/lesson/236899/step/1',
                'https://stepik.org/lesson/236903/step/1',
                'https://stepik.org/lesson/236904/step/1',
                'https://stepik.org/lesson/236905/step/1']

    @pytest.mark.parametrize('lst_addr', lst_addr)
    def test_guest_should_see_login_link(self, browser, lst_addr):
        link = f'{lst_addr}'
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector \
            ('[placeholder="Напишите ваш ответ здесь..."]'). \
            send_keys(str(math.log(int(time.time()))))
        # browser.find_element_by_class_name('submit-submission').\
        #     click()
        WebDriverWait(browser, 6) \
            .until(EC.element_to_be_clickable
                   ((By.CLASS_NAME, 'submit-submission'))) \
            .click()
        # time.sleep(1)

        el_anawer_text = WebDriverWait(browser, 5). \
            until(EC.visibility_of_element_located
                  ((By.CLASS_NAME, "smart-hints__hint"))).text
        # class ="smart-hints__hint"
        print(el_anawer_text)

        if el_anawer_text != 'Correct!':
            self.composite_text += el_anawer_text
            # print(self.composite_text)
        else:
            pass

        print(self.composite_text)
        assert el_anawer_text == 'Correct!'


print(TestMainPage1().composite_text)


# if __name__ == '__main__':
#     unittest.main()
