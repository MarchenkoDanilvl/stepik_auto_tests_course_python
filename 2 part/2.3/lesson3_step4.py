from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    
    browser.find_element_by_xpath("//button[@type='submit']").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    y = calc(x)
    
    InputAnswer = browser.find_element_by_xpath("//input[@id='answer']")
    InputAnswer.send_keys(y)
    
    AnswerButton = browser.find_element_by_xpath("//button[@type='submit']")
    AnswerButton.click()
    
finally:
    time.sleep(10)
    browser.quit()