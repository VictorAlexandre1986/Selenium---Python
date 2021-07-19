import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_pagina_seguinte_e_anterior(self):
        nav = self.driver
        nav.get('https://www.google.com')
        sleep(3)
        nav.get('https://www.gmail.com')
        sleep(3)
        nav.get('https://www.youtube.com')
        sleep(3)
        nav.back()
        sleep(3)
        nav.back()
        sleep(3)
        nav.forward()
        
if __name__=='__main__':
    unittest.main()