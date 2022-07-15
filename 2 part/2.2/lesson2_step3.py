from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    #browser.get("http://suninjuly.github.io/selects2.html") #Сайт с другим видом выпадающего списка
    
    FirstNumberLoc = browser.find_element_by_xpath("//span[@id='num1']")
    FirstNumber = int(FirstNumberLoc.text)
    
    SecondNumberLoc = browser.find_element_by_xpath("//span[@id='num2']")
    SecondNumber = int(SecondNumberLoc.text)
    
    FinalNumber = FirstNumber + SecondNumber
    
    select = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))
    select.select_by_value(str(FinalNumber))
    
    browser.find_element_by_xpath("//button[@type='submit']").click()
    
finally:
    time.sleep(10)
    browser.quit()