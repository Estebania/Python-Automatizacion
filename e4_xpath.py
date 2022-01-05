import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):#Para que el driver sea accequible desde cualquier parte del codigo
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_busca_por_xpath(self):
        driver = self.driver
        driver.get('https://www.google.com/')#va a llamar esta pagina
        time.sleep(5)
        buscar_por_xpath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input")
        time.sleep(4)
        buscar_por_xpath.send_keys("BTS", Keys.ARROW_DOWN)
        time.sleep(6)
        buscar_por_xpath.send_keys(Keys.RETURN)
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
#El xpath es una estructura de objetos (carpetas)
#Tipos de xpath
#Relativo: empieza a buscar desde el nodo que queremos encontrar en todo el arbol
#Absoluto: busca toda la rueta, es decir, desde el nodo padre hasta el drivado, si el nodo
#que deseamos buscar cambio de ruta no sera encontrado con este tipo de xpath