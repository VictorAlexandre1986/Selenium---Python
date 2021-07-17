from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from time import sleep

nav = webdriver.Chrome()
nav.get('https://www.demoqa.com/alerts')

alerta = Alert(nav)

prompBtn='#promtButton'


btnPromptElement = nav.find_element_by_css_selector(prompBtn)

btnPromptElement.click()

alerta.send_keys('Victor Alexandre')

sleep(2)

alerta.accept()