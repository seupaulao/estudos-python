from termcolor import colored
import time

#
# pyTimesTrade
# hora   quantidade    preco    comprador  vendedor  agressor 
#

def carregartt():
    return [{"hora":"12:00:01","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:01","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:02","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:03","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:03","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:03","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:03","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:04","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:05","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:06","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:07","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:08","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:09","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:11","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:11","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},]

vetor = carregartt()

h = 12
m = 0
s = 0

def zeros(n):
    return '0'*(2-len(str(n))) + str(n)

def formaChave(h,m,s):
   return zeros(h) + ':' + zeros(m) + ':' + zeros(s)   

def atualizaChave(h,m,s):
    if s % 60 > 59:
       m = m + 1
    if m > 59:
       h = h + 1
       m = 0
    return h, m   
 
for i in range(0, 12):
    h,m = atualizaChave(h,m,i)
    chave = formaChave(h,m,i)
    #print(chave)
    nvetor = [item for item in vetor if item["hora"]==chave]
    for item in nvetor:
        if item['agressor']=='C':
            print colored('{}  {}  {}  {}  {}  {}'.format(item['hora'], item['qte'],item['valor'],item['comprador'],item['vendedor'],item['agressor']),'green',attrs=['bold'])
        else:
            print colored('{}  {}  {}  {}  {}  {}'.format(item['hora'], item['qte'],item['valor'],item['comprador'],item['vendedor'],item['agressor']),'red',attrs=['bold'])
    time.sleep(1)
