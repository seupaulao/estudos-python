import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# abordagem bem arrumada, mas a historia requerida vai ficar dentro de um teste por classe
# porque a execucao nao eh disparada na ordem do topo para baixo e nem inversa
# e para cada teste dispara um novo cenario, com nova sessao e novo login
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        caps = webdriver.DesiredCapabilities.CHROME.copy() 
        caps['acceptInsecureCerts'] = True
        self.driver = webdriver.Chrome(desired_capabilities=caps)

    def login(self, driver):
        driver.get("https://desenv.sigepe.csd.serpro/")
        #self.assertIn("Sigac", driver.title)
        cpf = driver.find_element(by=By.XPATH, value='//input[contains(@name,"cpfUsuario")]')
        cpf.send_keys("03361709806")
        pas = driver.find_element(by=By.XPATH, value='//input[contains(@name,"password")]')
        pas.send_keys("1234567nova")
        ace = driver.find_element(by=By.XPATH, value="//button[contains(.,'Acessar')]")
        ace.click()

    def alterarPerfil(self, driver):    
        aper = driver.find_element(by=By.XPATH, value="//a[contains(.,'GESTOR - ÓRGÃO:MAPA')]")
        aper.click()
        nper = driver.find_element(by=By.XPATH, value="//a[contains(.,'GESTOR - ÓRGÃO:IBAMA')]")
        nper.click()

    #def test_logar_sigepe(self):
    #    driver = self.driver
    #    self.login(driver)

    #def test_alterar_perfil(self):
    #    driver = self.driver
    #    self.login(driver)
    #    self.alterarPerfil(driver)


    def test_entrar_ad(self):
        driver = self.driver
        self.login(driver)
        self.alterarPerfil(driver)
        # driver.implicitly_wait(10)
        driver.get("https://desenv.sigepe.csd.serpro/sigepe-ad-web/private/index.jsf")
        wait = WebDriverWait(driver, 25)
        menu = wait.until(EC.title_contains("Avaliação"))
        self.assertIn("Minhas",driver.title)

        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
