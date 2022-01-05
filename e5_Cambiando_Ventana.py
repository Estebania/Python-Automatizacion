import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
    
    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get('https://www.google.com/')
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])#Va a cambiar a la segunda ventana
        driver.get('https://stackoverflow.com/')
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])#Va a cambiar a la primera ventana ventana
        time.sleep(3)

if __name__== '__main__':
    unittest.main()

        

