import unittest
from selenium import webdriver
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        PROXY = "<168.47.25.220:80>"
        webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "proxyType": "MANUAL",

        }
        nav = webdriver.Chrome()
        
    def test_proxy(self):
        self.nav.get('https://www.google.com/')  
        
        
        
