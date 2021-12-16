from Tkinter import *

class MinhaAplicacao:
      def __init__(self, myparent, titulo):
          self.meucontener = Frame(myparent)
          self.meucontener.pack() 
          self.parent = myparent

          self.botao1 = Button(self.meucontener, command=self.button1Click)
          self.botao1.bind("<Return>", self.button1Click_a)
          self.botao1.configure(text="OK", background="gray")
          self.botao1.pack(side=LEFT)
          self.botao1.focus_force()

          self.botao2 = Button(self.meucontener, command=self.button2Click)
          self.botao2.bind("<Return>", self.button2Click_a)
          self.botao2.configure(text="Cancelar", background="gray")
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
 
      def button1Click_a(self,event):
          self.button1Click()

      def button2Click_a(self,event):
          self.button2Click() 
          



root = Tk()
app = MinhaAplicacao(root,"Minha Aplicacao 5")
root.mainloop()

