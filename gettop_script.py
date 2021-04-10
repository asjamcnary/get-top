from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/asjamcnary/Automation/get-top/Chromedriver')
driver.implicitly_wait(4)
driver.maximize_window()

driver.get('https://www.gettop.us/')

#driver.find_element().send_keys()
search_field = driver.find_element()
search_field.send_keys()

#driver.find_element().click()
search_icon = driver.find_element()
search_icon.click()

actual_text = driver.find_element().text
expected_text = ''

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()