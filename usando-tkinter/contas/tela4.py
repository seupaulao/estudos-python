from Tkinter import *
class Basica:
      def __init__(self,parent):
          self.p = parent
          f = Frame(self.p)
          f.grid(row=0)
 
          b1 = Button(f, text="         janela 2         ", command=self.janela2)
          b1.grid(row=1)
          b2 = Button(f, text="         janela 3         ", command=self.janela3)
          b2.grid(row=2)
     
      def janela2(self):
          r1 = Tk()
          f = Frame(r1)
          f.grid(row=0)
          l = Label(f, text="Janela 2                 ")
          l.grid(row=1)
          r1.mainloop()  
 
      def janela3(self):
          r1 = Tk()
          f = Frame(r1)
          f.grid(row=0)
          l = Label(f, text="Janela 3                   ")
          l.grid(row=1)
          r1.mainloop()  
 
r = Tk()
ap = Basica(r)
r.mainloop()

