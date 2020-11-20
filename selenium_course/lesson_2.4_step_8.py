from selenium import webdriver
import time
import math
import pylint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    
    browser = webdriver.Chrome()
    browser.get(link)


    elementPrice = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "$100"))
    button = browser.find_element_by_xpath('//*[@id="book"]')
    button.click()


    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    button = browser.find_element_by_xpath('//*[@id="solve"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

