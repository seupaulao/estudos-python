def getHex(num):
    vh=['0','1','2','3','4','5','6','7','8','9', 'A', 'B', 'C', 'D', 'E', 'F']
    if (num > 15):
       return num
    else:
       return vh[num]

numero=int(raw_input('Numero: '))

vetor=[]

dividendo=numero
divisor=2

quociente = 0
resto = 0
while dividendo > 1:
    quociente = dividendo / divisor
    resto = dividendo % divisor
    vetor.append(resto)
    dividendo = quociente

vetor.append(dividendo)
a=vetor[::-1]
s=""
for i in range(len(a)):
    s = s + str(a[i])  

ll = len(s)
while (ll % 4 <> 0):
    s = '0' + s
    ll = len(s) 
#
#
#

dividendo=numero
divisor=16
h=''
nh='999'
while dividendo > divisor-1:
      quociente = dividendo / divisor
      resto = dividendo % divisor
      t=getHex(resto)
      dividendo=quociente
      if nh==999:
         h = t
         nh = h
      else:
         h = t + h
         nh = h

t=getHex(dividendo)
h = t + h





# g=[]
# r=[]
# c=0
# for i in range(len(a)):
#    g.append(a[i])
#    c=c+1
#    if c==4:
#       c=0
#       r.append(g)
#       g=[]
 




print "BINARIO:      ", s
print "HEXADECIMAL:  ", h
