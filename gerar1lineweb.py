import os
import sys
# -- coding: UTF-8 --
def pegar(caminho):
   fo = open(caminho,'r')
   linhas = fo.readlines()
   fo.close()
   return linhas

def salvar(caminho, texto):
   fo = open(caminho,'w')
   fo.write(texto)
   fo.close()

def tratarNotas(texto):
    ntexto = texto
    ntexto = ntexto.replace("/wj*","</span>") 
    ntexto = ntexto.replace("/wj","<span class='w3-color'>") 
    ntexto = ntexto.replace('\n','')
    while ntexto.find('/f') >= 0:
        p2 = ntexto.find('/f*')
        p1 = ntexto.find('/f') 
        t3 = ntexto[p1+2:p2]
        t3 = t3.replace('/fqa','')  
        t3 = t3.replace('/ft','')  
        t3 = t3.replace('/fr','')
        t3 = t3[t3[5:].find(' ')+5:] 
        t3 = "[" + t3.strip() + "]"  
        t1 = ntexto[0:p1]
        t2 = ntexto[p2+3:] 
        ntexto = t1.strip() + t3 + t2.strip()
    while ntexto.find('/x') >= 0:
        p2 = ntexto.find('/x*')
        p1 = ntexto.find('/x')   
        t3 = ntexto[p1+2:p2]
        t3 = t3.replace('/xo','')  
        t3 = t3.replace('/xt','')
        t3 = t3[t3[5:].find(' ')+5:] 
        t3 = "[" + t3.strip() + "]"  
        t1 = ntexto[0:p1]
        t2 = ntexto[p2+3:] 
        ntexto = t1.strip() +t3+ t2.strip()
    return ntexto   


todos='' 
for i in range(68):
    if i > 1 :
       caminho = 'fontes/'+str(i)+'.usfm'
       linhas = pegar(caminho)
       fixo=''
       saida=''
       cap=''
       for item in linhas:
            item = item.replace('\\','/')
            if item.find('/toc3') >= 0:
               fixo=item[5:].strip()          
            if item.find('/c') >= 0:
               cap=item[3:5].strip() 
            if item.find('/v') >= 0:
               saida+='\n' + fixo + ' ' + cap + ":" + item[3:5].strip() + ' '+ tratarNotas( item[5:].strip() )   
            if item.find('/q1') >= 0:
               saida += tratarNotas( item[4:] )
            if item.find('/q2') >= 0:
               saida += tratarNotas( item[4:] )
            if item.find('/q3') >= 0:
               saida += tratarNotas( item[4:] )
       todos+=saida
salvar('web1line.txt',todos)
