from selenium import webdriver
import time
import math
import pylint


try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ввести ответ в текcтовое поле 
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    # отметить checkbox "I'm the robot"
    checkbox = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    checkbox.click()
    # выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    radiobutton.click()

    # нажать на кнопку Submit
    button = browser.find_element_by_xpath('/html/body/div/form/div/div/button')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()