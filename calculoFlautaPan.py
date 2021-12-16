#!/usr/bin/python

import sys
medida=[1, 24/25.0, 25/27.0, 8/9.0, 74/76.0,5/6.0, 4/5.0, 3/4.0, 18/25.0, 25/36.0, 2/3.0, 16/25.0, 5/8.0, 3/5.0, 72/152.0,5/9.0, 8/15.0, 0.5]
nota=['C','C#','Db','D','D#','Eb','E','F','F#','Gb','G','G#','Ab','A','A#','Bb','B','C']
inicial=32.5
try:
   inicial = float(sys.argv[1])
except:
   inicial=32.5

print './calculoFlautaPan.py tamanho_primeiro_tubo_em_cm'

bvar=map(lambda x: inicial * x, medida) 

tubo=0

for i in range(len(medida)):
    if i>=1 and i<len(medida) and bvar[i]>bvar[i-1]:
       print nota[i],'------>',bvar[i]
    else:
       print nota[i],'===>',bvar[i] 
    tubo += bvar[i]

print "Tamanho do tubo :", tubo
 

