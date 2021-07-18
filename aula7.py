from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('start-maximized')
#options.add_argument('start-minimized')

#Definindo user-agent qualquer
options.add_argument('user-agent=Firefox versao Victor')

#Usando um perfil no navegador
options.add_argument('--user-data-dir=C:/Users/Victor/AppData/Local/Google/Chrome/User Data')
#Default é o usuario padrao, caso queira outro usuario vá até o caminho acima crie uma pasta com o 
# nome que deseja e subistitua o default pelo nome definido 
options.add_argument('--profile-directory=Default')

#Utiliza uma extensao de auto recaptcha
options.add_extension('reCAPTCHA.crx')



nav = webdriver.Chrome(chrome_options=options)

