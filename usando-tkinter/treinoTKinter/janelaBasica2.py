#!/usr/bin/python

from Tkinter import *

class Janela:
    def __init__(self, root):
        self.fr1 = Frame(root)
        self.fr2 = Frame(root)
        self.fr3 = Frame(root)
        self.fr3.pack()
        self.fr2.pack()
        self.fr1.pack()

        Button(self.fr1, text='BT1').pack()
        Button(self.fr2, text='BT2').pack(side=LEFT)
        Button(self.fr2, text='BT3').pack(side=LEFT)
        Button(self.fr3, text='BT6').pack(side=RIGHT)
        Button(self.fr3, text='BT5').pack(side=RIGHT)
        Button(self.fr3, text='BT4').pack(side=RIGHT)

raiz=Tk()
Janela(raiz)
raiz.mainloop()
