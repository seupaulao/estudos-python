import sys
def fat(n):
     p = 1
     while (n > 1):
        p = p * n
        n = n - 1
     return p


x = long(sys.argv[1])
r =  fat(x)
print 'Resultado : ', r
   
