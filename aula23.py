import unittest
from selenium import webdriver
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.nav = webdriver.Chrome()
    
    def test_assertNotEqual(self):
        nav = self.nav
        nav.get('https://www.google.com')
        titulo_de_pagina = nav.title
        time.sleep(2)
        self.assertNotEqual('Google', titulo_de_pagina,'O título da pagina é igual')
        
    def tearDown(self):
        self.nav.quit() 
        
if __name__=='__main__':
    unittest.main()