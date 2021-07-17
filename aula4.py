from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

nav = webdriver.Chrome()
nav.get('https://www.demoqa.com/alerts')

btnAlert='#alertButton'
confirmBtn ='#confirmButton'
prompBtn='#promtButton'

btnAlertElement = nav.find_element_by_css_selector(btnAlert)

btnAlertElement.click()

alerta = nav.switch_to_alert()

print(alerta.text)
sleep(2)

alerta.accept()
sleep(2)
btnConfirmBtnElement = nav.find_element_by_css_selector(confirmBtn)

btnConfirmBtnElement.click()

alerta2 = nav.switch_to_alert()
sleep(2)
alerta2.accept()
#alerta2.dismiss()


btnPromptElement = nav.find_element_by_css_selector(prompBtn)

btnPromptElement.click()

alerta3 = nav.switch_to_alert()

alerta3.send_keys('Victor Alexandre')
sleep(2)
alerta3.accept()