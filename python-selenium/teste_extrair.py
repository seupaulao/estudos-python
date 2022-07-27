from selenium import webdriver
from selenium.webdriver.common.by import By

# iniciar webdriver
caps = webdriver.DesiredCapabilities.CHROME.copy() 
caps['acceptInsecureCerts'] = True
caps['pageLoadStrategy'] = 'normal'
driver = webdriver.Chrome(desired_capabilities=caps)

# acessar a pagina da string a ser extraida
driver.get('http://localhost:8000/mensagem.html')

# extrair string do especifica do componente visual
texto = driver.find_element(by=By.XPATH, value="//span[@id='msg']").text
quero = ''
for p in texto.split(' '):
    if len(p)>4 and p[0:4]=='0000':
        quero = p

# salvar string no arquivo
f = open("/tmp/recurso.txt", "w")
f.write(quero)
f.close()

#print(quero)

# acessar a outra página
driver.get('http://localhost:8000/formulario.html')

# buscar recurso temporario e armazenar em variavel temporaria
f = open("/tmp/recurso.txt", "r")
temp = f.read()
f.close()

# aplicar recurso no componente visual
driver.find_element(by=By.XPATH, value="//input[@type='text']").send_keys(temp)



