from Tkinter import *

class MinhaAplicacao:
      def __init__(self, myparent, titulo):
          self.meucontener = Frame(myparent)
          self.meucontener.pack() 
          self.parent = myparent

          self.botao1 = Button(self.meucontener)
          self.botao1["text"] = "Oi Mundo com classes!"
          self.botao1["background"] = "blue"
          self.botao1.pack(side=LEFT)
          self.botao1.bind("<Button-1>", self.button1Click)

          self.botao2 = Button(self.meucontener)
          self.botao2.configure(text="Of to join the circus")
          self.botao2.configure(background="tan")
          self.botao2.pack(side=LEFT)
          self.botao2.bind("<Button-1>", self.button2Click)
     
      def button1Click(self, event):
          if self.botao1["background"] == "blue":
             self.botao1["background"] = "yellow"
          else:
             self.botao1["background"] = "blue"
 
      def button2Click(self, event):
          self.parent.destroy()
 
          



root = Tk()
app = MinhaAplicacao(root,"Minha Aplicacao 5")
root.mainloop()

