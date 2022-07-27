from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# ----------- Entrando na tela do BGP - Publicacao -------------
caps = webdriver.DesiredCapabilities.CHROME.copy() 
caps['acceptInsecureCerts'] = True

# essa estrategia de carga é mais rapida, os outros valores possiveis : normal, eager, e none
caps['pageLoadStrategy'] = 'eager'
driver = webdriver.Chrome(desired_capabilities=caps)

# dado que entro na tela de login
driver.get('https://teste.sigepe.csd.serpro/')

# e informo o usuario a senha e clico em acessar
cpf = driver.find_element(by=By.XPATH, value='//input[contains(@name,"cpfUsuario")]')
cpf.send_keys("38560879153")
pas = driver.find_element(by=By.XPATH, value='//input[contains(@name,"password")]')
pas.send_keys("sigepe123")
ace = driver.find_element(by=By.XPATH, value="//button[contains(.,'Acessar')]")
ace.click()


wait = WebDriverWait(driver, 10)

# e clico em alterar perfil
aper = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'GESTOR - ÓRGÃO:MAPA')]")))
aper.click()

# entao altero o perfil para GESTOR - ÓRGÃO:ME
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='GESTOR - ÓRGÃO:ME']"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='GESTOR - GERAL:ME']"))).click()

# quando clico no menu sanduiche
stale = True
while stale:
    try:
        driver.find_element(by=By.XPATH, value="//div[@class='menu-button']").click()
        stale = False
    except:    
        stale= True 

# e movo o mouse sobre o menu 'Gestão de Pessoas'
msub1 = driver.find_element(by=By.XPATH, value="//a[contains(.,'Gestão de Pessoas')]")
hover = ActionChains(driver).move_to_element(msub1)
hover.perform()

# entao clico no sub menu 'Publicação'
wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Publicação']"))).click()

# --------- Tela de tarefas ------------
# Dado que estou na tela "Tarefas"
# Quando informo a chave gerada no elemento identificador e teclo ENTER 
chave = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id=\"idFormDataTable:tarefasPendentesTableID:j_idt356:filter\"]")))

f = open("/tmp/recurso.txt", "r")
temp = f.read()
f.close()

chave.send_keys(temp)
chave.send_keys(Keys.RETURN)

# 000000000000000032632022
# Entao acesso o link   
el1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'000000000000000032632022')]")))
driver.execute_script('arguments[0].click();',el1)

