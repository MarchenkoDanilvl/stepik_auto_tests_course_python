from selenium import webdriver
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    FirstNameImput = browser.find_element_by_xpath("//input[@name='firstname']")
    FirstNameImput.send_keys('Name')
    
    LastNameImput = browser.find_element_by_xpath("//input[@name='lastname']")
    LastNameImput.send_keys('LastName')
    
    EmailImput = browser.find_element_by_xpath("//input[@name='email']")
    EmailImput.send_keys('Email')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    InputFile = browser.find_element_by_xpath("//input[@id='file']")
    InputFile.send_keys(file_path)
    
    browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()