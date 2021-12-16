#!/usr/bin/python

from Tkinter import *

class Janela:
    def __init__(self, root):

        self.fr1 = Frame(root)
        self.fr1.pack()

        self.b1 = Button(self.fr1, text='BT1', command=self.click_bt1)
        self.b1['bg']='red'
        self.b1['width']=20
        self.b1['fg']='pink'
        self.b1.pack(side=LEFT)

        self.b2= Button(self.fr1)
        self.b2['width'], self.b2['bg'], self.b2['fg'] = 20, 'red', 'brown'
        self.b2.bind("<Button-1>", self.click_bt2) 
        self.b2.bind("<ButtonRelease>",self.release_bt2)
        self.b2.pack(side=LEFT)

        self.b3 = Button(self.fr1)
        self.b3['width'], self.b3['bg'], self.b3['fg'] = 20, 'red', 'green'
        self.b3.pack(side=LEFT)

    def click_bt2(self, event):
        self.b1['text'] = ''
        self.b2['text'] = 'Botao 2 clicado'
        self.b3['text'] = ''
    def release_bt2(self, event):
        self.b1['text'] = ''
        self.b2['text'] = 'Botao 2 release'
        self.b3['text'] = ''
    def click_bt1(self):
        self.b1['text'] = 'Botao 1 clicado'
        self.b2['text'] = ''
        self.b3['text'] = ''

       
        

raiz=Tk()
Janela(raiz)
raiz.mainloop()
