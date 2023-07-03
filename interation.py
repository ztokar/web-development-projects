from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

url="https://orteil.dashnet.org/experiments/cookie/"
os.environ['PATH']+= r"C/Development"

driver=webdriver.Chrome()
driver.get(url)

# wiki_num=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# wiki_num.click()
# time.sleep(10)
# print(wiki_num.text)
# all_portals=driver.find_element(By.LINK_TEXT,"View history")
# all_portals.click()

# search=driver.find_element(By.NAME,"search")
# search.send_keys("python")
# search bar is changing element after search input

selector='#cookie'
search2=driver.find_element(By.CSS_SELECTOR,selector)
time.sleep(3)
x=0
while x<1000:
    search2.click()
    search2.click()
    x+=1
time.sleep(3)