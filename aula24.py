import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.nav = webdriver.Chrome()
    
    def test_clickDireito(self):
        self.nav.get('https://www.google.com')
        time.sleep(2)
        clickDireito = self.nav.find_element_by_name('q')
        actions = ActionChains(self.nav)
        actions.context_click(clickDireito).perform()
        time.sleep(3)
        
    def tearDown(self):
        self.nav.quit()
        
if __name__=='__main__':
    unittest.main() 