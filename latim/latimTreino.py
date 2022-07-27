from latim import Latim
import random

class Ditado:
      def __init__(self):
          self.acertos = 0
          self.erros   = 0   
      
      def addErro(self):
          self.erros = self.erros + 1
 
      def addAcerto(self):
          self.acertos = self.acertos + 1

      def getAcertos(self):
          return self.acertos

      def getErros(self):
          return self.erros

      def zeraPlacar(self):
          self.acertos=0
          self.erros=0

      def apresentacao(self):    
          print '------------- Treino de Latim: --------------'
  	  print '\n'
          print 'Instrucao : Se a frase ou palavra vier em Portugues traduza ao Latim e vice-versa'
          print 'Instrucao : O padrao das frases e palavras eh minusculo'
          print '\n'
	  print '0 - Treino Sequencial'
	  print '1 - Treino Aleatorio'
	  print '2 - Treino Frases'
	  print '3 - Sair'
          print '\n'
          print '---------------------------------------------'

      def imprime(self):
          print '\nResultado, Acertos :', self.getAcertos(), '   Erros:', self.getErros()

      def corrigir(self, respUsuario, listaRespostaCorreta):
          listaRUsuario = respUsuario.split() 
          contadorErro = 0;
          #for itemRC in listaRespostaCorreta:
          #    for palavraUsuario in listaRUsuario:
          #        if (not palavraUsuario in itemRC):
          #           contadorErro = contadorErro + 1
          #if (contadorErro < 0):
          if(respUsuario in listaRespostaCorreta):
             self.addAcerto()
             print 'CERTO!!'
          else:
             self.addErro()
             print 'ERRADO =====>', listaRespostaCorreta 

      def trSequencial(self):
          self.zeraPlacar()
          listao = Latim()
          lisAlfabetica = sorted(listao.getDicionario())
          for k in lisAlfabetica:
              print '\nErros: ',self.getErros(),'        Acertos: ',self.getAcertos(), '      Palavra:',k, ':'
              lista = listao.getDicionario()[k]
              r = raw_input('Traducao Portugues:')
              if r==':q': break
              self.corrigir(r, lista)
          self.imprime()

      def trAleatorio(self):
          self.zeraPlacar()
          listao = Latim()
          tam = len(listao.getDicionario().keys())
          op = 'n'
          while True:
              chave = random.randint(1,tam)
              nomechave = listao.getDicionario().keys()[chave]
              print '\nErros: ',self.getErros(),'        Acertos: ',self.getAcertos(), '      Palavra:',nomechave, ':'
              op = raw_input('Traducao Portugues:')
              if op==':q': break
              lista = listao.getDicionario()[nomechave]
              self.corrigir(op, lista)
          self.imprime()
     
      def trFrases(self):
          self.zeraPlacar()
          listao=Latim()
          for k,v in listao.getFrases().iteritems():
              print '\nErros: ',self.getErros(),'        Acertos: ',self.getAcertos(), '      Palavra:',k, ':'
              r = raw_input('Traducao Portugues:')
              self.corrigir(op, lista)
          self.imprime()
         


d = Ditado()
d.apresentacao()
opcao = int(raw_input("Opcao: "))
while True:
   if opcao==0: 
      d.trSequencial()
   elif opcao==1: 
      d.trAleatorio()
   elif opcao==2:
      d.trFrases()
   elif opcao==3:
      break
   else : print 'opcao invalida'
   d.apresentacao()   
   opcao = int(raw_input("Opcao: "))


