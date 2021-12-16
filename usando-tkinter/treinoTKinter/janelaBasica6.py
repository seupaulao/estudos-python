#!/usr/bin/python

from Tkinter import *
import os.path


class Janela6:
    def __init__(self, root):

        self.fr1 = Frame(root)
        self.fr1.pack()
        self.fr2 = Frame(root)
        self.fr2.pack() 
        self.fr3 = Frame(root)
        self.fr3.pack() 
        self.raiz=root 

        fonte1 = ('Verdana', 12, 'bold')
        self.l1 = Label(self.fr1,text='Pasta:')
        self.l1.pack(side=LEFT)
        self.e1 = Entry(self.fr1,width=40)
        self.e1.pack(side=LEFT) 
        
        self.b1 = Button(self.fr2, text='Procurar', command=self.buscar)
        self.b1['width']=20
        self.b1.pack()

        self.l2 = Label(self.fr3)
        self.l2['fg']='green'
        self.l2['font']=fonte1
        self.l2.pack()
        self.texto = ""

    def getTexto(self):
        return self.texto 

    def buscar(self):
        achado = self.e1.get()
        if os.path.exists(achado):
           self.texto='DIRETORIO ENCONTRADO'
        else:
           self.texto='DIRETORIO NAO ENCONTRADO'
        self.raiz.quit()

