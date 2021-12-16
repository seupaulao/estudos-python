#!/usr/bin/python
import random
import sys
def gerarDigito(numero):
    vet=[6,5,4,3,2,9,8,7,6,5,4,3,2] 

    b=0
    for i in range(12):
        b = b + vet[i+1] * int(numero[i])
    dig1=0
    b = b % 11
    if (b >= 2):
       dig1 = 11 - b
    numero = numero + str(dig1)

    b=0
    for i in range(13):
        b = b + vet[i] * int(numero[i])
    dig2=0
    b = b % 11
    if (b >= 2):
       dig2=11-b
    numero=numero+str(dig2)
    return numero

def gerarRandomCnpj(qte):
    for i in range(qte):
        print str(i+1).zfill(len(str(qte))+1) + " " + gerarDigito(str(random.randint(10001000,99999999)) + str(random.randint(1000,9000)))

def gerarCnpjLimit(radical,limi,limf):
    i = int(limi)
    while i <= int(limf):
       
       p = str(i).zfill(4)
       x = radical + str(p)
       print gerarDigito(x) 
       i = i + 1
    
if (len(sys.argv) == 4):
    r = sys.argv[1]
    i = sys.argv[2]
    f = sys.argv[3]
    print(r,i,f)
    gerarCnpjLimit(r,i,f)
elif (len(sys.argv) == 2):    
    x = sys.argv[1]
    if (len(x) > 12 or len(x) < 12):
       print("Entrada INVALIDA")
    else:
       print("\nCNPJ= " + gerarDigito(x))   
elif (len(sys.argv) == 3):
    x = int(sys.argv[2])
    gerarRandomCnpj(x)
