from Tkinter import *

class MinhaAplicacao:
      def __init__(self, myparent):
          self.meucontener1 = Frame(myparent)
          self.meucontener1.pack() 

          botao1 = Button(self.meucontener1)
          botao1["text"] = "Oi Mundo com classes!"
          botao1["background"] = "blue"
          botao1.pack()

root = Tk()
app = MinhaAplicacao(root)
root.mainloop()

