import sys
def investir(tempo, valor, taxa, inicial=0, exibir=False):
        v = inicial
        for i in range(tempo):
            v += valor
            v *= (1 + taxa/100)
            if exibir:
               print("Mes {} = {:,.2f}".format(i,v))
        print("{} x {} meses a {:.2f} por mes = {:,.2f}".format(valor,tempo,taxa,v))


if len(sys.argv) < 2:
    print ("Modo de usar:\npython investir.py TEMPO VALOR TAXA [INICIAL] [EXIBIR]")
    print ("TEMPO - em meses\nVALOR do investimento\nTAXA de juros")
    print ("Valor INICIAL, o default é 0 - zero.")
    print ("EXIBIR o periodo em meses - opcional, valor: True/False")
elif len(sys.argv) == 4:
    te = int(sys.argv[1])
    vl = float(sys.argv[2])
    tx = float(sys.argv[3])
    investir(te,vl,tx)
elif len(sys.argv) == 5:
    te = int(sys.argv[1])
    vl = float(sys.argv[2])
    tx = float(sys.argv[3])
    ini = float(sys.argv[4])
    investir(te,vl,tx,ini)
else:
    te = int(sys.argv[1])
    vl = float(sys.argv[2])
    tx = float(sys.argv[3])
    ini = float(sys.argv[4])
    ex = bool(sys.argv[5])
    investir(te,vl,tx,ini,ex)


