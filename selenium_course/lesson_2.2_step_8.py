from selenium import webdriver
import time
import math
import pylint
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('/html/body/div/form/div/input[1]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('/html/body/div/form/div/input[2]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('/html/body/div/form/div/input[3]')
    input3.send_keys("asd@asd.asd")

    uploadfile = browser.find_element_by_xpath('//*[@id="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '123.txt') 
    uploadfile.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()