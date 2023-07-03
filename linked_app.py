
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url="https://www.linkedin.com/jobs/search/?currentJobId=3584593409&f_AL=true&f_WT=2&geoId=101620260&keywords=python%20developer&refresh=true"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)
time.sleep(6)
login_button=driver.find_element(By.LINK_TEXT,"Sign in")
login_button.click()
time.sleep(6)

login_button1=driver.find_element(By.ID,"username")
time.sleep(6)
# login_button2=driver.find_element(By.LINK_TEXT,"Email or Phone")
login_button1.send_keys("zack.tokar@gmail.com")
time.sleep(6)
login_button2=driver.find_element(By.ID,"password")
time.sleep(6)
login_button2.send_keys("Wrong")
time.sleep(6)
