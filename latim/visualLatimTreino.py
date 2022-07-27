from latim import Latim
from Tkinter import *
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
          instrucao = ''
          instrucao = instrucao +  '------------- Treino de Latim: --------------\n'
  	  instrucao = instrucao +  '\n'
          instrucao = instrucao +  'Instrucao : Se a frase ou palavra vier em Portugues traduza ao Latim e vice-versa\n'
          instrucao = instrucao +  'Instrucao : O padrao das frases e palavras eh minusculo\n'
          instrucao = instrucao +  '\n'
	  instrucao = instrucao +  '0 - Treino Sequencial\n'
	  instrucao = instrucao +  '1 - Treino Aleatorio\n'
	  instrucao = instrucao +  '2 - Treino Frases\n'
	  instrucao = instrucao +  '3 - Sair\n'
          instrucao = instrucao +  '\n'
          instrucao = instrucao +  '---------------------------------------------\n'
          return instrucao

      def imprime(self):
          return '\nResultado, Acertos :' +  str(self.getAcertos()) +  '   Erros:' +  str(self.getErros())

      def corrigir(self, respUsuario, listaRespostaCorreta):
          listaRUsuario = respUsuario.split() 
          contadorErro = 0;
          if(respUsuario in listaRespostaCorreta):
             self.addAcerto()
             return 'CERTO!!'
          else:
             self.addErro()
             return 'ERRADO =====>' + str(listaRespostaCorreta) 


class VisualLatim:
      def __init__(self, parent):
          self.parente = parent       
          self.ichave = 0
          mArea = Frame(parent)
          mArea.grid(row=0)
          
          self.ditado = Ditado()
          self.listaLatim = Latim()

          b1 = Button(mArea, text="Instrucao", command=self.carregaInstrucao).grid(row=1)
          b2 = Button(mArea, text="Treino Sequencial", command=self.carregaTreinoSeq).grid(row=2)
          b3 = Button(mArea, text="Treino Aleatorio", command=self.carregaTreinoAle).grid(row=3)
          b4 = Button(mArea, text="Treino Frases", command=self.carregaTreinoFra).grid(row=4)


      def carregaInstrucao(self):
          rr1 = Tk()
          f1 = Frame(rr1)
          f1.grid(row=0)
          txt1 = Text(f1)
          txt1.grid(row=1)
          txt1.delete(1.0, END)
           
          txt1.insert(END, self.ditado.apresentacao())
          rr1.mainloop()   


      def carregaTreinoSeq(self):
          self.ichave = 1 
          self.ditado.zeraPlacar()
          # self.nomeChavePergunta = self.listaLatim.getDicionario().keys()[self.ichave]
          self.lisAlfabetica = sorted(self.listaLatim.getDicionario().keys())
          self.nomeChavePergunta = self.lisAlfabetica[self.ichave]

          rr2 = Tk()
          f1 = Frame(rr2)
          f1.grid(row=0)
          Label(f1, text="Treino Sequencial").grid(row=0,column=1)

          self.eacerto = Entry(f1,width=30)
          self.eacerto.grid(row=1,column=0)
          self.eacerto.insert(END, "Acertos:  " + str(self.ditado.getAcertos()))
          self.eerro = Entry(f1,width=30)
          self.eerro.grid(row=1,column=1,sticky=W)
          self.eerro.insert(END, "Erros:  " + str(self.ditado.getErros()))

          Label(f1, text="Palavra  : ").grid(row=2, sticky=W)
          self.e1TS = Entry(f1,width=60)
          self.e1TS.grid(row=2, column=1, sticky=W)
          self.e1TS.insert(END, self.nomeChavePergunta)

          Label(f1, text="Traducao : ").grid(row=3, column=0, sticky=W) 
          self.e2TS = Entry(f1,width=60)
          self.e2TS.grid(row=3, column=1, sticky=W)
          self.e2TS.bind("<Return>", self.validarTreinoSeq_a)
          
          bvalidar = Button(f1,text="Validar", command=self.validarTreinoSeq)
          bvalidar.grid(row=4)
          self.tx1TS = Text(f1)
          self.tx1TS.grid(row=5,columnspan=2)

          rr2.mainloop()

      def validarTreinoSeq_a(self, event):
          self.validarTreinoSeq() 

      def validarTreinoSeq(self):
          lista = self.listaLatim.getDicionario()[self.nomeChavePergunta]
          resposta = self.e2TS.get()
          correcao = self.ditado.corrigir(resposta, lista)
          self.tx1TS.insert(END, correcao + "\n")
          self.eerro.delete(0,END)
          self.eacerto.delete(0,END)
          self.eerro.insert(END, "Erros:  " + str(self.ditado.getErros()) )
          self.eacerto.insert(END, "Acertos:  " + str(self.ditado.getAcertos()) )
 
          # print "Acertos: " + str(self.ditado.getAcertos()) + "   Erros: " + str(self.ditado.getErros())
           
          self.ichave = self.ichave + 1 
          tam = len(self.listaLatim.getDicionario().keys())
          if (self.ichave > tam):
             self.ichave = 1   
          # self.nomeChavePergunta = self.listaLatim.getDicionario().keys()[self.ichave]
          self.nomeChavePergunta = self.lisAlfabetica[self.ichave]
          self.e1TS.delete(0, END)
          self.e2TS.delete(0, END)
          self.e1TS.insert(END, self.nomeChavePergunta)


          
      def carregaTreinoAle(self):
          self.ditado.zeraPlacar()
          tam = len(self.listaLatim.getDicionario().keys())
          chave = random.randint(1,tam)
          self.nomeChavePergunta = self.listaLatim.getDicionario().keys()[chave]

          rr2 = Tk()
          f1 = Frame(rr2)
          f1.grid(row=0)
          Label(f1, text="Treino Aleatorio").grid(row=0,column=1)

          self.eacerto = Entry(f1,width=30)
          self.eacerto.grid(row=1,column=0)
          self.eacerto.insert(END, "Acertos:  " + str(self.ditado.getAcertos()))
          self.eerro = Entry(f1,width=30)
          self.eerro.grid(row=1,column=1,sticky=W)
          self.eerro.insert(END, "Erros:  " + str(self.ditado.getErros()))

          Label(f1, text="Palavra  : ").grid(row=2, sticky=W)
          self.e1TA = Entry(f1,width=60)
          self.e1TA.grid(row=2, column=1, sticky=W)
          self.e1TA.insert(END, self.nomeChavePergunta)

          Label(f1, text="Traducao : ").grid(row=3, column=0, sticky=W) 
          self.e2TA = Entry(f1,width=60)
          self.e2TA.grid(row=3, column=1, sticky=W)
          self.e2TA.bind("<Return>", self.validarTreinoAle_a)
          
          bvalidar = Button(f1,text="Validar", command=self.validarTreinoAle)
          bvalidar.grid(row=4)
          self.tx1TA = Text(f1)
          self.tx1TA.grid(row=5,columnspan=2)

          rr2.mainloop()


      def validarTreinoAle_a(self, event):
          self.validarTreinoAle()

      def validarTreinoAle(self):
          tam = len(self.listaLatim.getDicionario().keys())

          lista = self.listaLatim.getDicionario()[self.nomeChavePergunta]
          resposta = self.e2TA.get()
          correcao = self.ditado.corrigir(resposta, lista)
          self.tx1TA.insert(END, correcao + "\n")
          self.eerro.delete(0,END)
          self.eacerto.delete(0,END)
          self.eerro.insert(END, "Erros:  " + str(self.ditado.getErros()) )
          self.eacerto.insert(END, "Acertos:  " + str(self.ditado.getAcertos()) )
 
          # print "Acertos: " + str(self.ditado.getAcertos()) + "   Erros: " + str(self.ditado.getErros())
          chave = random.randint(1,tam)
          self.nomeChavePergunta = self.listaLatim.getDicionario().keys()[chave]
           
          self.e1TA.delete(0, END)
          self.e2TA.delete(0, END)
          self.e1TA.insert(END, self.nomeChavePergunta)
          
      def carregaTreinoFra(self):
          self.ichave = 1
          self.ditado.zeraPlacar()
          self.nomeChavePergunta = self.listaLatim.getFrases().keys()[self.ichave]

          rr2 = Tk()
          f1 = Frame(rr2)
          f1.grid(row=0)
          Label(f1, text="Treino de Frases").grid(row=0,column=1)

          self.eacerto = Entry(f1,width=30)
          self.eacerto.grid(row=1,column=0)
          self.eacerto.insert(END, "Acertos:  " + str(self.ditado.getAcertos()))
          self.eerro = Entry(f1,width=30)
          self.eerro.grid(row=1,column=1,sticky=W)
          self.eerro.insert(END, "Erros:  " + str(self.ditado.getErros()))

          Label(f1, text="Frase  : ").grid(row=2, sticky=W)
          self.e1TF = Entry(f1,width=60)
          self.e1TF.grid(row=2, column=1, sticky=W)
          self.e1TF.insert(END, self.nomeChavePergunta)

          Label(f1, text="Traducao : ").grid(row=3, column=0, sticky=W) 
          self.e2TF = Entry(f1,width=60)
          self.e2TF.grid(row=3, column=1, sticky=W)
          self.e2TF.bind("<Return>", self.validarTreinoFra_a)
          
          bvalidar = Button(f1,text="Validar", command=self.validarTreinoFra)
          bvalidar.grid(row=4)
          self.tx1TF = Text(f1)
          self.tx1TF.grid(row=5,columnspan=2)

          rr2.mainloop()

      def validarTreinoFra_a(self, event):
          self.validarTreinoFra()

      def validarTreinoFra(self):
          tam = len(self.listaLatim.getFrases().keys())

          lista = self.listaLatim.getFrases()[self.nomeChavePergunta]
          resposta = self.e2TF.get()
          correcao = self.ditado.corrigir(resposta, lista)
          self.tx1TF.insert(END, correcao + "\n")
          self.eerro.delete(0,END)
          self.eacerto.delete(0,END)
          self.eerro.insert(END, "Erros:  " + str(self.ditado.getErros()) )
          self.eacerto.insert(END, "Acertos:  " + str(self.ditado.getAcertos()) )
          self.ichave = self.ichave + 1
          if self.ichave > tam:
             self.ichave = 1 

          # print "Acertos: " + str(self.ditado.getAcertos()) + "   Erros: " + str(self.ditado.getErros())
          self.nomeChavePergunta = self.listaLatim.getFrases().keys()[self.ichave]
          self.e1TF.delete(0, END)
          self.e2TF.delete(0, END)
          self.e1TF.insert(END, self.nomeChavePergunta)
 

          
root = Tk()
app = VisualLatim(root)
root.mainloop()




