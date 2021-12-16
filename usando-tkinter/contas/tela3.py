from Tkinter import *
class TresJanelas:
      def __init__(self, parent):
          self.myParent = parent
          self.minhaJanela = Frame(parent)
          self.minhaJanela.pack()
        
          self.button1 = Button(self.minhaJanela, text="Janela 1", command=self.evJanela1)
          self.button1.pack(side=LEFT)
          self.button2 = Button(self.minhaJanela, text="Janela 2", command=self.evJanela2)
          self.button2.pack(side=LEFT)

      def evJanela1(self):    
          root1=Tk()
          f1 = Frame(root1)
          f1.pack()
          Label(f1, text="Janela 1", background="#FF0000").pack() 
          Button(f1, text="Mata Janela 1",command=root1.quit).pack()
          root1.mainloop()
 

      def evJanela2(self): 
          root2 = Tk()
          menub = Menu(root2)
          menub.add_command(label="Quit", command=root2.quit)
          root2.config(menu=menub)
          root2.mainloop()


root = Tk()
app = TresJanelas(root)
root.mainloop()   

