from selenium import webdriver
from selenium.webdriver.common.keys import Keys

nav = webdriver.Chrome()
nav.get('https://www.demoqa.com/upload-download')


inputFile = '#uploadFile'

nav.find_element_by_css_selector(inputFile).send_keys('C:/Users/Victor/Desktop/Aprendendo/Python/arquivo.txt')

