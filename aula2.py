from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

nav = webdriver.Chrome()
nav.get('https://www.demoqa.com/checkbox')

home ='rct-title' #class
btnView = '.rct-collapse' #selector
Downloads = 'li.rct-node:nth-child(3) > span:nth-child(1) > label:nth-child(2) > span:nth-child(4)' #xpath

homeElement = nav.find_element_by_class_name(home).click()
btnViewElement = nav.find_element_by_css_selector(btnView).click()
sleep(2)
downloadsElement = nav.find_element_by_css_selector(Downloads).click() #Nao vai selecionar o download