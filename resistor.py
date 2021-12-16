import sys

cores=['prata','ouro','preto','marrom','vermelho','laranja','amarelo','verde','azul','violeta','cinza','branco']

anel1=['','','0','1','2','3','4','5','6','7','8','9']
anel2=['','','0','1','2','3','4','5','6','7','8','9']
anel3=[0.01,0.1,1,10,100,1000,10000,100000,1000000,10000000,None,None]
anel4=[0.1,0.05,None,0.01,0.02,0.03,0.04,None,None,None,None,None]

r = ''
saida = 0
rsaida = ''

if len(sys.argv)<2:
    print("Modo de usar:")
    print("python resistor.py cor1 cor2 cor3 cor4")
    print("\nCores disponiveis: prata, ouro, preto, marrom, vermelho, laranja, amarelo, verde,azul, violeta,cinza, e branco") 
else:
    entrada1 = sys.argv[1]
    entrada2 = sys.argv[2]
    entrada3 = sys.argv[3]
    entrada4 = sys.argv[4]
    if entrada1 in cores:
        i = cores.index(entrada1)
        r += anel1[i]
    if entrada2 in cores:
        i = cores.index(entrada2)
        r += anel2[i]
    if entrada3 in cores:
        i = cores.index(entrada3)
        if anel3[i] != None:
           saida = int(r) * anel3[i]
        else:
           saida = int(r) 
    if entrada4 in cores:
        i = cores.index(entrada4)
        if anel4[i] != None:
            rsaida = "Valor = {:,.2f} a {:,.2f} ohms".format(saida*(1-anel4[i]), saida*(1+anel4[i]))
        else:
            rsaida = "Valor = {:,.2f} ohms".format(saida) 

print(rsaida)
    

    
