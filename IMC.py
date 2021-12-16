from Tkinter import *

class IMC:
    def __init__(self, parent):
        self.meuParente = parent
        minhaArea = Frame(parent)
        minhaArea.pack()

        Label(minhaArea, text="Peso").grid(row=0, sticky=W)
        Label(minhaArea, text="Altura").grid(row=1, sticky=W)

        self.e1 = Entry(minhaArea)
        self.e2 = Entry(minhaArea)

        self.e1.grid(row=0,column=1)
        self.e2.grid(row=1,column=1)
        self.e2.bind("<Return>",self.calcular_a)

        self.button1 = Button(minhaArea, text="Calcular", command=self.calcular)
        self.button1.grid(row=2,column=1)

        self.text1 = Text(minhaArea)
        self.text1.grid(row=3,columnspan=2,sticky=W)
        
    def calcular_a(self,event):
        self.calcular()

    def calcular(self):
        peso = float(self.e1.get())
        altura = float(self.e2.get())
        pesoAtual = peso
        altura = altura / 100
        self.text1.delete(1.0, END)
        resulIMC = self.tabelaIMC(peso,altura)
        self.text1.insert(END, resulIMC)
        self.text1.insert(END, "\n") 
        while(not self.pesoIdeal(peso,altura)):
           peso = peso - 1
    
        self.text1.insert(END, "Para entrar na faixa IDEAL voce precisa de um peso de " + str(peso) + "\n")
        imcideal = self.calculoIMC(peso,altura)
        self.text1.insert(END, "IMC de "+ str(imcideal) + "\n")
        self.text1.insert(END, "O peso que precisa perder eh :" + str( pesoAtual - peso))



    def calculoIMC(self,peso,altura):
        return peso / altura **2

    def tabelaIMC(self,peso, altura):
        imc = self.calculoIMC(peso, altura)
        if (imc < 18.5):
           return "ABAIXO do peso ideal " + str(imc)
        elif(imc >= 18.5 and imc <= 24.9):
           return "PESO IDEAL " + str(imc)
        elif(imc >= 25 and imc <= 29.9):
           return "Sobrepeso " + str(imc)
        elif(imc >= 30 and imc <= 34.9):
           return "OBESIDADE 1 "+ str(imc)
        elif(imc >= 35 and imc <= 39.9):
           return "OBESIDADE 2 " + str(imc)
        elif(imc >= 40):
           return "OBESIDADE 3 " + str(imc)

    def pesoIdeal(self,peso, altura):
        imc = self.calculoIMC(peso, altura)
        if (imc >= 18.5 and imc <= 23.9):
           return 1 
        else:
           return 0


root = Tk()
app = IMC(root)
root.mainloop()




