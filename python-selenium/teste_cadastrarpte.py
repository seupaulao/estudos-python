from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from utils import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from sqlalchemy import true


caps = webdriver.DesiredCapabilities.CHROME.copy() 
caps['acceptInsecureCerts'] = True
driver = webdriver.Chrome(desired_capabilities=caps)

# driver = webdriver.Chrome()
driver.get('https://desenv.sigepe.csd.serpro/')

cpf = driver.find_element(by=By.XPATH, value='//input[contains(@name,"cpfUsuario")]')
cpf.send_keys("03361709806")
pas = driver.find_element(by=By.XPATH, value='//input[contains(@name,"password")]')
pas.send_keys("1234567nova")
ace = driver.find_element(by=By.XPATH, value="//button[contains(.,'Acessar')]")
ace.click()
aper = driver.find_element(by=By.XPATH, value="//a[contains(.,'GESTOR - ÓRGÃO:MAPA')]")
aper.click()
nper = driver.find_element(by=By.XPATH, value="//a[contains(.,'GESTOR - ÓRGÃO:IBAMA')]")
nper.click()

stale = True
while stale:
    try:
        driver.find_element(by=By.XPATH, value="//div[@class='menu-button']").click()
        stale = False
    except:    
        stale= True 

msub1 = driver.find_element(by=By.XPATH, value="//a[contains(.,'Gestão de Pessoas')]")
hover = ActionChains(driver).move_to_element(msub1)
hover.perform()

driver.find_element(by=By.XPATH, value="[//a[contains(.,'Avaliação de Desempenho')]").click()


# wait = WebDriverWait(driver, 10)
# elm = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Avaliação de Desempenho')]")))
# elm.click()

# driver.find_element(by=By.XPATH, value="//a[contains(.,'Avaliação de Desempenho')]").click()


#driver.get("https://desenv.sigepe.csd.serpro/sigepe-ad-web/private/index.jsf")
#wait = WebDriverWait(driver, 25)
#menu = wait.until(EC.title_contains("Avaliação"))
# assertIn("Minhas",driver.title)


# testeIn("Python", driver.title)
#elemento = driver.find_element(by=By.NAME, value='q')
#elemento.clear()
#elemento.send_keys("pycon")
#elemento.send_keys(Keys.RETURN)
#testeNotIn("No results found.", driver.page_source)