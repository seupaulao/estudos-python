import sys


def calcularminutos(p1,p2,p3,p4):
    hr1 = int(sys.argv[p1])
    mn1 = int(sys.argv[p2])
    minutos = hr1*60 + mn1
    hr2 = int(sys.argv[p3])
    mn2 = int(sys.argv[p4])
    minutos -= hr2*60 + mn2
    minutos *= -1
    return minutos

if len(sys.argv) > 1:
   minutos1 = calcularminutos(1,2,3,4)
   faltam = 480 - minutos1
   print ( "Minutos 1o exp : " + str(minutos1) )
   print ( "Faltam minutos : " + str(faltam) )

   minutos2 = calcularminutos(5,6,7,8)
   print ( "Minutos 2o exp : " + str(minutos2) )
   print ( "Expediente     : " + str(minutos1+minutos2))
   print ( "Excesso ou Falta : " + str((minutos1+minutos2)-480))
else:
   print ("Modo de usar: python calcularminutos h1 m1 h2 m2 h3 m3 h4 m4")



