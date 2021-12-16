#!/usr/bin/python

from Tkinter import *

class Janela:
    def __init__(self, root):
        self.fr1 = Frame(root)
        self.fr1.pack()

        self.msglb1 = "Clique para ficar amarelo!"
        self.lb1 = Label(self.fr1, text=self.msglb1)
        self.lb1['width']=len(self.msglb1)
        self.lb1['height']=3
        self.lb1.pack() 
        
        self.msglb2="Arraste o mouse sobre o botao"
        self.lb2 = Label(self.fr1, text=self.msglb2, font=('Arial','12','bold'))
        self.lb2['height']=3
        self.lb2['width']=len(self.msglb2)
        self.lb2.pack()

        self.bt1 = Button(self.fr1, text='Clique',bg='green')
        self.bt1.bind("<Button-1>",self.muda_cor)
        self.bt1.bind("<Motion>",self.sobre_botao)
        self.bt1.bind("<Leave>",self.fora_botao)
        self.bt1.pack()

    def sobre_botao(self, event):
        self.lb2['text']="Isso esta em cima de mim"
        self.lb2['fg']='red'

    def fora_botao(self, event):
        self.lb2['text']="Saiu de cima!"
        self.lb2['fg']='yellow'   

    def muda_cor(self, event):
        if self.bt1['bg']=='green':
           self.bt1['bg']='yellow'
           self.bt1['text']='Clique para ficar verde'
        else: 
           self.bt1['bg']='green'
           self.bt1['text']='Clique para ficar amarelo'

raiz=Tk()
Janela(raiz)
raiz.mainloop()
