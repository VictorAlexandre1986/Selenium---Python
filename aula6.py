from selenium import webdriver
from time import sleep

nav = webdriver.Chrome()
nav.get('https://www.demoqa.com/browser-windows')

btnTab = '#tabButton'
btnWindow = '#windowButton'

btnTabElement = nav.find_element_by_css_selector(btnTab)
btnWindowElement = nav.find_element_by_css_selector(btnWindow)

#Pegando o id da janela
print(nav.current_window_handle)

#Pegando todas as ids
print(nav.window_handles)

sleep(1.5)
nav.switch_to_window(
    nav.window_handles[0]
)

sleep(2)
btnWindowElement.click()
#Mostrando um novo id de janela na lista
print(nav.window_handles)