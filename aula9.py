import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class usando_inittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_buscar(self):
        nav = self.driver
        nav.get('https://www.google.com')
        #Abrindo uma nova aba
        nav.execute_script('window.open("");')
        time.sleep(3)
        nav.switch_to_window(nav.window_handles[0])
        nav.get('https://stackoverflow.com')
        time.sleep(3)
        nav.switch_to_window(nav.window_handles[1])
        time.sleep(3)
        nav.get('https://www.google.com')
        inputElement = nav.find_element_by_css_selector('.gLFyf')
        inputElement.send_keys('selenium')
        inputElement.send_keys(Keys.ENTER)

        
    def desligando(self):
        self.nav.close()
    
    
if __name__ == '__main__':
    unittest.main()
    

