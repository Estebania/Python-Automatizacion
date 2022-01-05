import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #Para llamar el driver wait para indicar que vamos a esperar cierto tiempo
from selenium.webdriver.support import expected_conditions as EC #Con este declararemos una condicion para continuar con la ejecucion

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_usando_explicit_wait(self):

        driver = self.driver
        driver.get('https://ibighit.com/bts/eng/')
        #Para hacer un ciclo
        try:
            #Cargamos el webdriver y le indcamos la cantidad de intentos en este caso 10
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/main/section/ul/li[1]/button/div/div[1]/img'))#Va a esperar a que se carge el elemento buscado por nombre con By
            )

        finally:
            driver.quit()#otra forma de cerrar el driver
if __name__== '__main__':
    unittest.main()

        