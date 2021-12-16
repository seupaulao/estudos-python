from Tkinter import *

class MinhaAplicacao:
      def __init__(self, myparent, titulo):
          self.meucontener = Frame(myparent)
          self.meucontener.pack() 
          self.parent = myparent

          self.botao1 = Button(self.meucontener, command=self.button1Click)
          self.botao1["text"] = "OK"
          self.botao1["background"] = "gray"
          self.botao1.pack(side=LEFT)

          self.botao2 = Button(self.meucontener, command=self.button2Click)
          self.botao2.configure(text="Cancelar")
          self.botao2.configure(background="gray")
          self.botao2.pack(side=RIGHT)
     
      def button1Click(self):
          print "Event handler Botao 1"
          if self.botao1["background"] == "blue":
             self.botao1["background"] = "yellow"
          else:
             self.botao1["background"] = "blue"
 
      def button2Click(self):
          print "Event handler Botao 2"
          self.parent.destroy()
 
          



root = Tk()
app = MinhaAplicacao(root,"Minha Aplicacao 5")
root.mainloop()

