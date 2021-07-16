from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

nav = webdriver.Chrome()
nav.get('https://www.demoqa.com/text-box')

#Elementos
xpath = '//*[@id="userName"]'
id = 'userEmail'
adress = 'currentAddress'

#Econtrar elementos
inputNameElement = nav.find_element_by_xpath(xpath)
inputEmailElement = nav.find_element_by_id(id)
inputAdressElement = nav.find_element_by_id(adress)

#função click
inputNameElement.click() #Clicando no textobox nome
sleep(3)
inputEmailElement.click() #Clicando no textbox email
sleep(3)

#Digitando elementos
inputNameElement.send_keys('Victor Alexandre')
inputEmailElement.send_keys('oi@oi.com.br')
inputAdressElement.send_keys('Digitando um endereço')
for i in range(5):
    inputAdressElement.send_keys(Keys.ENTER)
sleep(3)
    
for i in range(4):
    inputAdressElement.send_keys(Keys.BACKSPACE)