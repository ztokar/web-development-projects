import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


os.environ['PATH']+= r"C/Development"
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('https://www.python.org/')
# message = driver.find_element(By.CLASS_NAME, value="a-price-whole")

# print(driver)
# driver.maximize_window()
# print(f"The price is {message.text}")

# output_message = driver.find_element(By.ID, 'display')
# assert 'I AM EXTRA COOOOL' in output_message.text
# medium-widget event-widget last
calendar=driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
for event in calendar:   #otherwise you're getting just an object
    print(event.text)

events=driver.find_elements(By.CSS_SELECTOR,'.event-widge li a')
for happening in events:
    print(happening.text)