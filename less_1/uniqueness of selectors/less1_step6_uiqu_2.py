from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # обязательные поля
    # //div[@class=’buttons’ and contains(text(),’Save’)]

    # //div[text()=’Тема’]/preceding-sibling::input
    input1 = browser.find_element_by_xpath\
        ('//input[contains(@placeholder,"first name")]')
        # ('//input[contains(@class,"first")]')
    input1.send_keys("Ivan")
    time.sleep(2)
    input2 = browser.find_element_by_xpath\
        ('//input[contains(@placeholder,"last name")]')
        # ('//input[contains(@class,"second")]')
    input2.send_keys("Petrov")
    time.sleep(2)
    input3 = browser.find_element_by_xpath\
        ('//input[contains(@placeholder,"your email")]')
        # ('//input[contains(@class,"third")]')
    input3.send_keys("asd@maysdd.ru")
    time.sleep(2)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    print(welcome_text)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()