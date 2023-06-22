# from selenium import webdriver

# chrome_path = r"C:\Users\innat\OneDrive\Desktop\chromedriver.exe"
# options = webdriver.ChromeOptions()
# options.add_argument("--no-sandbox")  # Add any additional options you need
# options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to Chrome browser executable

# driver = webdriver.Chrome(options=options)

# driver.get("https://www.amazon.com")

import time

from selenium import webdriver



driver = webdriver.Chrome(r"C:\Users\innat\OneDrive\Desktop\chromedriver.exe")  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

# time.sleep(5) # Let the user actually see something!

# search_box = driver.find_element_by_name('q')

# search_box.send_keys('ChromeDriver')

# search_box.submit()

# time.sleep(5) # Let the user actually see something!

# driver.quit()
