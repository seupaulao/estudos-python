blow_end_comprimento=9.8
blow_end_largura=8.5
buracos=[10,11,9.2,8.6,11.2,7]

quenag=[338,303,280,244,218,188]
tamg = 400
buraco_reverso_g=170

quenac=[]
tamc = 600

for i in quenag:
    quenac.append((i * tamc) / tamg)

buraco_reverso_c = buraco_reverso_g * tamc / tamg

print quenac, "Para tamanho da flauta em C = ", tamc, "mm e buraco reverso igual a ", buraco_reverso_c, "mm"
