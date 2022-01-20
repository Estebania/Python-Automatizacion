from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class prorbandoPaginaWeb(unittest.TestCase):
#En esta clase se encuentra la automtizacion de 
#los casos de prueba creados para la pagina web creada con django
    def setUp(self):#Para que el driver sea accequible desde cualquier parte del codigo
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_CP_001(self):
        """Se probará la respuesta del sistema cuando se intenta editar la información disponible de los cursos."""
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        time.sleep(3)
        buscar_boton_editar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tbody/tr[1]/td[5]/a')
        time.sleep(5)
        buscar_boton_editar.click()
        time.sleep(5)
        self.assertIn('Edicicion de cursos', driver.title)
        buscar_Nombre = driver.find_element_by_xpath('//*[@id="txtNombre"]')
        time.sleep(3)
        buscar_Nombre.clear()
        time.sleep(3)
        buscar_Nombre.send_keys('Programación Avanzada III')
        time.sleep(3)
        busar_Creditos = driver.find_element_by_xpath('//*[@id="numCreditos"]')
        busar_Creditos.clear()
        time.sleep(2)
        busar_Creditos.send_keys('8')
        time.sleep(5)
        buscar_boton_gurdar = driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[4]/button')
        time.sleep(3)
        buscar_boton_gurdar.click()
        time.sleep(3)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
  

        