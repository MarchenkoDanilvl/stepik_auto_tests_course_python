from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    TreasureBox = browser.find_element_by_xpath("//img[@id='treasure']")
    x = TreasureBox.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element_by_xpath("//input[@id = 'answer']")
    input1.send_keys(y)
    
    browser.find_element_by_xpath("//input[@id = 'robotCheckbox']").click()
    browser.find_element_by_xpath("//input[@id = 'robotsRule']").click()
    browser.find_element_by_xpath("//button[@type = 'submit']").click()
    
finally:
    time.sleep(10)
    browser.quit()