from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


nav = webdriver.Chrome()

nav.get('https://www.w3schools.com/')
time.sleep(2)

all_cookies = nav.get_cookies()

print(all_cookies)

nav.close()

