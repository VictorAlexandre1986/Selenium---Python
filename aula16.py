from selenium import webdriver
import time
nav = webdriver.Chrome()
nav.get('https://www.w3schools.com/html/html_tables.asp')
time.sleep(4)


for i in range(2,8):
    compania = nav.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[3]/div/table/tbody/tr['+str(i)+']/td[1]').text
    nome = nav.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[3]/div/table/tbody/tr['+str(i)+']/td[2]').text
    pais = nav.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[3]/div/table/tbody/tr['+str(i)+']/td[3]').text
    print(f'{compania} | {nome} | {pais}')

nav.close()









