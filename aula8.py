from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

nav = Chrome()
nav.get('https://www.demoqa.com/dynamic-properties')

btnWaitElement='#enableAfter'

#Vai esperar por 15 segundos até o elemento ser clicavel
btn = WebDriverWait(nav,timeout=15).until(
    EC.element_to_be_clickable((By.ID,'enableAfter'))
)

btn.click()

sleep(2)

visivel = WebDriverWait(nav,timeout=15).until(
    EC.invisibility_of_element_located(By.ID,'visibleAfter')
)