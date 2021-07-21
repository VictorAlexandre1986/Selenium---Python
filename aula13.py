from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

nav = webdriver.Chrome()
nav.get('https://olhardigital.com.br/')
time.sleep(2)

encontrarLink='Instagram Stories terá tradução de textos automática para até 90 idiomas'
linkElement = nav.find_elements_by_link_text(encontrarLink)

linkElement[0].click()

nav.close()


