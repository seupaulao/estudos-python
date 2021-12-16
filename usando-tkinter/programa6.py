from Tkinter import *

class MinhaAplicacao:
      def __init__(self, myparent, titulo):
          self.meucontener = Frame(myparent)
          self.meucontener.pack() 

          botao1 = Button(self.meucontener)
          botao1["text"] = "Oi Mundo com classes!"
          botao1["background"] = "blue"
          botao1.pack(side=LEFT)

          botao2 = Button(self.meucontener)
          botao2.configure(text="Of to join the circus")
          botao2.configure(background="tan")
          botao2.pack(side=LEFT)
 
          botao3 = Button(self.meucontener)
          botao3.configure(text="Um dia bonito", background="cyan")
          botao3.pack(side=LEFT)

          botao4 = Button(self.meucontener, text="Quarto botao", background="yellow")
          botao4.pack(side=LEFT) 


root = Tk()
app = MinhaAplicacao(root,"Minha Aplicacao 5")
root.mainloop()

