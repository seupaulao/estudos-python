def mul(x,n):
    p = 1
    c = 1
    while (c <= n):
          p = p * x
          c = c + 1

    return p

base = int(raw_input("base : "))
potencia = int(raw_input("potencia : "))

print "Resultado = ",mul(base,potencia)


    
