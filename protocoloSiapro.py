#!/usr/bin/python
import random

protocoloSiapro = str(random.getrandbits(64))[0:15]

pesoInicial = 16
pesoInicial2 = 17

acumulado=0
for i in range(15):
    acumulado += int(protocoloSiapro[i:i+1]) * pesoInicial
    pesoInicial -= 1

digito1 = (11 - (acumulado % 11)) % 10
protocoloSiapro = protocoloSiapro + str(digito1)

acumulado=0
for i in range(16):
    acumulado += int(protocoloSiapro[i:i+1]) * pesoInicial2
    pesoInicial2 -= 1

digito2 = (11 - (acumulado % 11)) % 10
protocoloSiapro = protocoloSiapro + str(digito2)

print "Protocolo Siapro: ", protocoloSiapro
