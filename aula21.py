import unittest
from selenium import webdriver
import time

class suite(unittest.TestCase):
    def setUp(self):
        self.nav=webdriver.Chrome()    
    
    def test_procurar(self):
        self.nav.get('https://www.google.com/')
        self.procura = self.nav.find_element_by_name('q')
        self.procura.send_keys('selenium')
        self.procura.submit()
        time.sleep(3)
    
    def tearDown(self):
        self.nav.quit()

if __name__=='__main__':
    unittest.main()





