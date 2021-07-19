from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


nav = webdriver.Chrome()
nav.get('https://www.w3schools.com/howto/howto_css_switch.asp')

switchElement = nav.find_element_by_css_selector('label.switch:nth-child(12) > div:nth-child(2)')
sleep(3)
switchElement.click()