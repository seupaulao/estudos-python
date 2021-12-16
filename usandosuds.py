from suds import client

url="https://10.139.52.152/sci/vistos?wsdl"

soap=client.Client(url)
nome=raw_input("Insira um nome: ")

print soap

resposta=soap.service.consultarPorNome(nome, 0)
print resposta
