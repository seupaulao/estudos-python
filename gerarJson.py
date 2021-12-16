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

saida='{' 
linhas = pegar('blv1line.txt')
for linha in linhas:
    livro = linha[0,2]
    capitulo = linha[4:linha.index(':')]
    versiculo = linha[linha.index(':'): linha[linha.index(':'):].find(' ')]
    texto = linha[linha.index(':'):].find(' '):]
salvar('web1line.txt',todos)
