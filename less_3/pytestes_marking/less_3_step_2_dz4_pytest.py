import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClassName(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_t1(self):
        # Тест успешно проходит на странице
        # http://suninjuly.github.io/registration1.html

        # Тест падает с ошибкой NoSuchElementException:
        # http://suninjuly.github.io/registration2.html

        link = "http://suninjuly.github.io/registration2.html"
        # browser = webdriver.Chrome()
        browser = self.driver
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        # обязательные поля
        input1 = browser.find_element_by_xpath \
            ('//input[contains(@placeholder,"first name")]')
        # ('//input[contains(@class,"first")]')
        input1.send_keys("Ivan")
        time.sleep(1)
        input2 = browser.find_element_by_xpath \
            ('//input[contains(@placeholder,"last name")]')
        # ('//input[contains(@class,"second")]')
        input2.send_keys("Petrov")
        time.sleep(1)
        input3 = browser.find_element_by_xpath \
            ('//input[contains(@placeholder,"your email")]')
        # ('//input[contains(@class,"third")]')
        input3.send_keys("asd@maysdd.ru")
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        print(f'==================>{welcome_text}')

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong TEXT!!!!!!!!")
        # "Congratulations! You have successfully registered!" == welcome_text

    # def tearDown(self) -> None:
    #     self.driver.quit()

    def test_t2(self):
        # Тест успешно проходит на странице
        # http://suninjuly.github.io/registration1.html

        # Тест падает с ошибкой NoSuchElementException:
        # http://suninjuly.github.io/registration2.html

        link = "http://suninjuly.github.io/registration1.html"
        # browser = webdriver.Chrome()
        browser = self.driver
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        # обязательные поля
        input1 = browser.find_element_by_xpath \
            ('//input[contains(@placeholder,"first name")]')
        # ('//input[contains(@class,"first")]')
        input1.send_keys("Ivan")
        time.sleep(1)
        input2 = browser.find_element_by_xpath \
            ('//input[contains(@placeholder,"last name")]')
        # ('//input[contains(@class,"second")]')
        input2.send_keys("Petrov")
        time.sleep(1)
        input3 = browser.find_element_by_xpath \
            ('//input[contains(@placeholder,"your email")]')
        # ('//input[contains(@class,"third")]')
        input3.send_keys("asd@maysdd.ru")
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        print(f'==================>{welcome_text}')

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # self.assertEqual('expected_res', 'actual_res', 'Текст о несовпадении')

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong TEXT!!!!!!!!")


if __name__ == '__main__':
    unittest.main()
    