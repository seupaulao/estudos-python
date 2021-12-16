from Tkinter import *

class MinhaAplicacao:
      def __init__(self, myparent, titulo):
          self.meucontener = Frame(myparent)
          self.meucontener.pack() 
          self.parent = myparent

          self.botao1 = Button(self.meucontener)
          self.botao1["text"] = "OOK"
          self.botao1["background"] = "blue"
          self.botao1.pack(side=LEFT)
          self.botao1.bind("<Button-1>", self.button1Click)
          self.botao1.focus_force()
          self.botao1.bind("<Return>", self.button1Click) 
          self.botao1.bind("<Return>", self.button1Click) 

          self.botao2 = Button(self.meucontener)
          self.botao2.configure(text="CCancelar")
          self.botao2.configure(background="red")
          self.botao2.pack(side=RIGHT)
          self.botao2.bind("<Return>", self.button2Click) 
          self.botao2.bind("<Return>", self.button2Click) 
     
      def button1Click(self, event):
          if self.botao1["background"] == "blue":
             self.botao1["background"] = "yellow"
          else:
             self.botao1["background"] = "blue"
 
      def button2Click(self, event):
          self.report_event(event)
          self.parent.destroy()
 
      def report_event(self, event):
          """Imprime a descricao de um evento baseado em seus atributos
          """
          event_name={"2":"Keypressed" , "4":"ButtonPressed"}
          print "Time: ", str(event.time)
          print "EventType=" + str(event.type), \
                event_name[str(event.type)], \
                "EventWidgetId=" + str(event.widget), \
                "EventKeySymbol=" + str(event.keysym)
          



root = Tk()
app = MinhaAplicacao(root,"Minha Aplicacao 5")
root.mainloop()

