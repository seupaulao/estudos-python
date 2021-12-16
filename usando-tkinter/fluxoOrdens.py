from Tkinter import *
#
#+-------------+---------------+----------------+
#|             |               |                |
#+             |   book ordens |                |
#|             |     original  |     historico  |
#|  book       +---------------+   de           |
#|    de       |               |    negocios    |
#|     ofertas |               |                |
#|             |     book      +----------------+
#|             |     precos    |    posicao     |
#|             +---------------+----------------+
#|             |  C  E   X  V  |  hist ordens   |
#+-------------+---------------+----------------+
#

class FluxoOrdens:
      def __init__(self, myparent, titulo):
          self.meucontener = Frame(myparent)
          self.frame = Frame(self.meucontener, borderwidth=5, relief="sunken",width=800, height=600)
          self.parent = myparent

          self.botao1 = Button(self.meucontener, command=self.button1Click)
          self.botao1.configure(text="Book de Ofertas", background="gray")

          self.botao2 = Button(self.meucontener, command=self.button2Click)
          self.botao2.configure(text="Historico Ordens Original", background="gray")

          self.botao3 = Button(self.meucontener)
          self.botao3.configure(text="Book de Precos", background="gray")

          self.panel2 = Frame(self.meucontener)
          self.botaoc = Button(self.panel2)
          self.botaoc.configure(text="Buy", background="gray")
          self.botaoe = Button(self.panel2)
          self.botaoe.configure(text="Edit", background="gray")
          self.botaox = Button(self.panel2)
          self.botaox.configure(text="Execute", background="gray")
          self.botaov = Button(self.panel2, command=self.buttonSellClick)
          self.botaov.configure(text="Sell", background="gray")
          self.botaoc.pack(side=LEFT)  
          self.botaoe.pack(side=LEFT)  
          self.botaox.pack(side=LEFT)  
          self.botaov.pack(side=LEFT)  
          
          self.botao4 = Button(self.meucontener)
          self.botao4.configure(text="Times & Trades", background="gray")

          self.meucontener.grid(column=0, row=0)
          self.frame.grid(column=0, row=0, columnspan=9, rowspan=8)
	  self.botao1.grid(column=0, row=1, columnspan=2, rowspan=6)
	  self.botao2.grid(column=4, row=0, columnspan=3, rowspan=3)
	  self.botao3.grid(column=4, row=3, columnspan=3, rowspan=3)
	  self.panel2.grid(column=4, row=6, columnspan=3, rowspan=2)
	  self.botao4.grid(column=7, row=1, columnspan=3, rowspan=6)
          

      def button1Click(self):
          print "Event handler Botao 1"
          if self.botao1["background"] == "blue":
             self.botao1["background"] = "yellow"
          else:
             self.botao1["background"] = "blue"
 
      def button2Click(self):
          print "Event handler Botao 2"
 
      def buttonSellClick(self):
          print "Acao Vender"
          



root = Tk()
app = FluxoOrdens(root,"Tape Reading e Fluxo de Ordens")
root.mainloop()
