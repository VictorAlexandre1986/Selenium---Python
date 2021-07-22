from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opcoes = Options()

opcoes.add_experimental_option('prefs', {
    'profile.default_content_setting_values.notifications':2
})

nav = webdriver.Chrome(chrome_options=opcoes)