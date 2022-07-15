from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    wait = WebDriverWait(browser, 15)
    Price = wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_xpath("//button[@id='book']")
    
    if Price is True:
        button.click()
        
    InputValue = browser.find_element_by_xpath("//span[@id='input_value']").text
    AnswerValue = calc(InputValue)
    
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(AnswerValue)
    AnswerButton = browser.find_element_by_xpath("//button[@id='solve']")
    AnswerButton.click()
    
    
finally:
    time.sleep(10)
    browser.quit()
