arquivo = "server.py" 
farq = open(arquivo,'r')
conjunto = farq.readlines()
for linha in conjunto:
    print linha 
