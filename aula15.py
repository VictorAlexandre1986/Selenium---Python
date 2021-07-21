from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

nav = webdriver.Chrome()
nav.get('https://www.google.com.br/?gws_rd=ssl')
palavra_buscada='seleni'
time.sleep(2)

buscador = nav.find_element_by_name('q')
buscador.send_keys(palavra_buscada)
time.sleep(5)

for i in range(1,11):
    sugestoes = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li['+str(i)+']/div/div[2]/div[1]/span/b'
    elementos = nav.find_element_by_xpath(sugestoes).text
    print(palavra_buscada + elementos)

nav.close()








