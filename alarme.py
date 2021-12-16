#!/usr/bin/python

import sched, time
import sys
import os
s = sched.scheduler(time.time, time.sleep)

valor=0
item="s"

try:
    valor=int(sys.argv[1])
    item = sys.argv[2]
except:
    valor=10
    
def print_time(): 
    os.system("firefox --new-window https://siscop.portalcorporativo.serpro")
    print "\n\nTchau\n"

def calculartempo(vl, it):
    if (it=="h"):
       return 3600 * vl
    elif (it=="m"):
       return 60 * vl
    else:
       return vl

def print_some_times():
    try: 
       print "Iniciando alarme..."
       tempo = calculartempo(valor, item)
       s.enter(tempo, 1, print_time, ())
       s.run()
    except KeyboardInterrupt:
       print "\n\nInterrompendo Aplicacao. Tchau\n"
       sys.exit(0)
       

print_some_times()
