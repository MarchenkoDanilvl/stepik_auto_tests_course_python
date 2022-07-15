from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text)
    y = calc(x)

    TextArea = browser.find_element_by_xpath("//input[@id='answer']")
    TextArea.send_keys(y)
    
    button = browser.find_element_by_xpath("//button[@type='submit']")
    browser.execute_script("window.scrollBy(0, 150);")
    
    CheckInput = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    CheckInput.click()
    
    RadioInput = browser.find_element_by_xpath("//input[@id='robotsRule']")
    RadioInput.click()
    
    button.click()

finally:
    time.sleep(10)
    browser.quit()