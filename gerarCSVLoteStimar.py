#!/usr/bin/python
#coding: utf-8
import sys
import random

def gerarNome():
    nomes = random.randint(2,4)
    palavra = random.randint(4,10)
    full=""
    for i in range(nomes):
        partial=""
        for j in range(palavra):
            letra=chr(random.randint(65,90))
            partial = partial + letra
        full = full + partial + " "
    return full
  
def gerarCpf():
    return " "

def completaZero(valor, num):
    vl = str(valor)
    return "0"*(num-len(vl))+vl
     

def gerarDataNasc():
    ano = str(random.randint(1901,2000))
    mes = completaZero(random.randint(1,12),2)
    dia = completaZero(random.randint(1,28),2)
    return dia + "/" + mes + "/" + ano

def gerarSexo():
    valor = random.randint(1,2)
    if (valor==1): 
       return "MASCULINO"
    else:
       return "FEMININO"

def gerarRacaCor():
    valor = random.randint(1,3)
    if (valor==1):
       return "BRANCA"
    elif (valor==2):
       return "PRETA"
    else:
       return "PARDA"

def gerarNacionalidade():
    valor = random.randint(1,4)
    if (valor==1):
       return "BRASIL"
    elif(valor==2):
       return "ARGENTINA"
    elif(valor==3):
       return "ALEMANHA"
    else:
       return "ESTADOS UNIDOS"

def gerarLinha():
    return gerarNome() + "," + gerarCpf() + "," +gerarDataNasc() + "," +gerarSexo() +  "," + gerarRacaCor() + "," + gerarNome() + "," + gerarNome() + "," + gerarNacionalidade()

valor = ""   
try:
   valor = sys.argv[1]
except:
   valor = "0"

if (int(valor) > 0):
  f = open("saida.csv","w")
  f.write("Nome,CPF,Data de Nascimento,Sexo,Raça\/Cor,Nome Pai,Nome Mãe,País de Nacionalidade")
  f.write("\n")
  for x in range(int(valor)):
      linha = gerarLinha()
      # print(linha)
      f.write(linha)
      f.write("\n")
  f.close()



    
