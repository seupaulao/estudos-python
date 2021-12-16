def inverso(numero):
    b = str(numero)
    a = b[::-1]
    return int(a)

def capicua(numero):
    cont = 0
    num = numero
    inv = inverso(num)
    while (inv != num):
          num = num + inv
          cont = cont + 1
          inv = inverso(num)

    print 'Numero Inverso: ',num 
    print 'Iteracoes     : ',cont



n = int(raw_input('Numero : '))
capicua(n)  
    
