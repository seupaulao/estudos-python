#from pyPgSQL import PgSQL
import pyBancoLoad2DB 

#
# problemas encontrados
#       - formato do ARQUIVO ASCII 
#       - contraponto com o formato do banco UNICODE
#       - RESOLUCAO : SET CLIENT_ENCODING=ENCODING DO ARQUIVO CARREGADO
# carga completa
#       - acontece se o banco tambem eh ASCII
#
# fazer as validacoes do arquivo TXT para o BANCO 
# 
#
#

class Estrutura():
      def __init__(self):
          self.estrutura = []

      def imprime(self):
          for reg in self.estrutura:
              print reg

      def trataInt(self,c):
          xlis = c.split(",")
          soma = 0
          for x in xlis:
              soma = soma + int(x)
          return soma

      def carrega(self,arquivoEstrutura):
          f = open(arquivoEstrutura,'r')
          lista =  f.readlines()
          for lis in lista:
              a = lis[0:40].strip()
              b = lis[40:41].strip()
              c = lis[42:46].strip()
              n = self.trataInt(c)
              self.estrutura.append((a,[b,n]))

      def tamanhoRegistro(self):
          soma = 0
          for reg in self.estrutura:
              soma = soma + reg[1][1]
          return soma   

      def getEstrutura(self):
          return self.estrutura

class Carga():
      def __init__(self,dicionario,tamanho):
          self.dados = []
          self.estrutura = dicionario
          self.tamanhoLinha = tamanho


      #essa funcao processa o registro e para cada campo do registro 
      #ele pega o tamanho e o nome na estrutura e insere uma tupla na lista (nomedocampo, valor)
      def processaRegistro(self, registro):
          dd = []
          somador = 0;
          for k in self.estrutura:
              t = k[1][1]
              est = k[0]
              valor = registro[somador:t+somador].strip()
              dd.append((est, valor))
              somador = somador + t
          return dd


      #carrega o arquivo  
      def carrega(self,arquivo):
          f = open(arquivo,'r')
          lista = f.readlines()
          for registro in lista:
              resultado = self.processaRegistro(registro)
              self.dados.append(resultado)
              
      def getDados(self):
          return self.dados    
 
      def imprimeDados(self):
          for i in self.dados:
              print i




