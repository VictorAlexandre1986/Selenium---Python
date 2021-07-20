from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

nav = webdriver.Chrome()
nav.get('https://www.w3schools.com/howto/howto_custom_select.asp')
time.sleep(2)

select = nav.find_element_by_css_selector('#main > div:nth-child(8) > div:nth-child(1) > select:nth-child(2)')
options = select.find_elements_by_tag_name('option')
time.sleep(2)

for option in options:
    print(f'Valores {option.get_attribute("value")}')
    option.click()
    time.sleep(1)
selecionar = Select(nav.find_element_by_css_selector('#main > div:nth-child(8) > div:nth-child(1) > select:nth-child(2)'))
selecionar.select_by_value('10')
