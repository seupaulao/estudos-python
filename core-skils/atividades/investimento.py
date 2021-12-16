def investimento(capital, taxa, limite):
    periodo = 0
    valor = capital
    while valor < limite:
         valor = valor * ( 1 + taxa/100 )
         periodo += 1
    print("\nI ${} * {} % = {:.2f} em {} t.\nDeve superar o limite de ${:.2f} em ${:.2f}".format(capital, taxa, valor, periodo, limite, (valor-limite)))     
    return periodo 

investimento(100, 20, 170)
investimento(100, 5, 250)
investimento(100, 6.11, 300)
investimento(15, 6.11, 850)

