from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from utils import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from sqlalchemy import true

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

# --------- Tela de Cadastrar Ato ------------

#    Então vou para a tela "Cadastrar Ato para Publicacao"
driver.get('https://teste.sigepe.csd.serpro/sigepe-bgp-web-intranet/pages/publicacao/cadastrar.jsf')

#    E visualizo parte do texto "Cadastrar Ato" no "Título da página"
#    E seleciono o tema
#    E clico em "Lupa Assunto"
#    E clico em "Opcao 1 Assunto"
#    E clico em "Botão Selecionar Assunto"
#    Quando informo uma data de publicação posterior a data atual
#    E rolo a tela para baixo
#    Então rolo a tela e clico em "Botão Incluir Orgaos Elaboradores"
#    E clico em "Campo CPF"
#    Entao informo o valor "385.608.791-53" no campo "Campo CPF"
#    E clico em "Botao Pesquisar"
#    Quando seleciono o radio "Elemento 1"
#    Então clico no botão selecionar do componente
#    Entao informo o valor "alguma coisa" no conteudo do ato
#    E rolo a tela e clico em "Botao Enviar Para Analise"
#    E clico no botao sim
#    Dado que estou na tela "Tarefas"
#    Entao visualizo parte do texto "Envio do ato" no "Mensagem da Página"

