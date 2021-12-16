#!/usr/bin/python

from Tkinter import *
#importa o arquivo janelaBasica6 e sua classe
import janelaBasica6

class Janela7:
    def __init__(self, raiz):
        self.f1 = Frame(raiz)
        self.f2 = Frame(raiz)
        self.f1.pack()
        self.f2.pack()
        self.root=raiz 

        self.botao1 = Button(self.f1, text='Escolher', width=25)
        self.botao1.bind("<ButtonRelease>", self.escolherDir)
        self.botao1.pack()
   
        self.l1 = Label(self.f2, fg='blue', font=('Arial',14,'bold'))
        self.l1.pack()

    def escolherDir(self, event):
        #cria uma nova instancia de tkinter para a classe Janela6 do arquivo importado 
        instancia2 = Tk()
        jan=janelaBasica6.Janela6(instancia2)
        instancia2.mainloop()
        #ao clicar no botao da janela6, eh 'quitado' o programa Janela6, mas a classe ainda tem valores
        #pega o valor da classe
        self.l1['text']=jan.getTexto()
        #destroi a janela6 de modo a fechar a janela aberta definitivamente
        instancia2.destroy()
 

instancia=Tk()
Janela7(instancia)
instancia.mainloop()

