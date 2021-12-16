#!/usr/bin/python

from Tkinter import *

class Janela:
   def __init__(self, root):
       self.fr1 = Frame(root)
       self.fr1.pack()
       self.botao1 = Button(self.fr1, text='Ola!')
       self.botao1['bg']='green'
       self.botao1['font']=('Verdana','12','italic','bold')  
       self.botao1['height']=3
       self.botao1.pack()

       self.botao2 = Button(self.fr1, font=('Arial',16),bg='red')
       self.botao2['text'] = 'Bye!!'
       self.botao2['fg'] = 'yellow'
       self.botao2['width'] = 12
       self.botao2.pack()

       self.botao3 = Button(self.fr1, font=('Courier',14),width=22,text='Mexendo')
       self.botao3['bg']='blue'
       self.botao3['fg']='pink'
       self.botao3['height']='2'
       self.botao3.pack() 

raiz=Tk()
Janela(raiz)
raiz.mainloop()
