from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

# до рефакторинга
   # x_element = browser.find_element_by_xpath('//*[@id="num1"]')
   # y_element = browser.find_element_by_xpath('//*[@id="num2"]')

   # x = x_element.text
   # y = y_element.text
   # summ = int(x) + int(y)

# после рефакторинга
    summ = int(browser.find_element_by_xpath('//*[@id="num1"]').text) + int(browser.find_element_by_xpath('//*[@id="num2"]').text)

    select = Select(browser.find_element_by_xpath('//*[@id="dropdown"]'))
    select.select_by_value(str(summ))
    

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()