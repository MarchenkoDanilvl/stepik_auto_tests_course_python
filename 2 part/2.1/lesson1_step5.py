from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    
    Robot_Check = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    Robot_Check.click()
    
    Robot_Radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
    Robot_Radio.click()
    
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    

finally:
    time.sleep(5)
    browser.quit()