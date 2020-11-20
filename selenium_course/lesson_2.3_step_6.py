from selenium import webdriver
import time
import math
import pylint

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

