from selenium import webdriver
import time

nav = webdriver.Chrome()
nav.get('https://www.amazon.com.br/')
time.sleep(2)
nav.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
nav.close()