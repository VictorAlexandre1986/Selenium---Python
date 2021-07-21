from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

nav = webdriver.Chrome()
nav.get('https://olhardigital.com.br/')
time.sleep(2)

botao='#body > main > section.featured > a:nth-child(1)'
btnElement = nav.find_elements_by_css_selector(botao)

print(btnElement[0].is_displayed())
print(btnElement[0].is_enabled())
#for elemento in btnElement:
#    print(elemento.click())

nav.close()
