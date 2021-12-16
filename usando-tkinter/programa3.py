from Tkinter import *
root = Tk()

meucontener = Frame(root)
meucontener.pack()

botao1 = Button(meucontener)
botao1["text"] = "Oi Mundo!"
botao1["background"] = "green"
botao1.pack()


root.mainloop()

