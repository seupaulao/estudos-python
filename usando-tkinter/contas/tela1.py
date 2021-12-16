from Tkinter import *

# <Button-1>, <Button-2>, <Button-3>   : botoes esquerdo, meio e direito do mouse respectivamente
# <Enter> : dispara quando o mouse entra no Widget
# <Leave> : dispara quando o mouse sai no Widget
# <Return>: disparado quando o usuario digita a tecla ENTER - pode ser substituido por : Control_L, Control_R,Shift_L,Shit_R,Left,Up,Down,Right,F1..12,Num_Lock,Scroll_Lock,Escape,etc.
# <Key>   : disparado quando o usuario digita uma tecla
# quando usa-se grid, somente a janela desce como pack, os componentes descem somente como grid, senao havera conflito
# dentro de cada celula da grid, os widgets estao centralizados, para reposiciona-los utiliza-se sticky=N,S,E, ou W
#


class Dialogo:
      def __init__(self, parent):
          self.myParent = parent
          minhaArea = Frame(parent)
          minhaArea.pack()

          Label(minhaArea, text="Primeiro:").grid(sticky=W)
          Label(minhaArea, text="Foi Digitado:").grid(sticky=W)

          self.e1 = Entry(minhaArea) 
          self.e2 = Entry(minhaArea) 

          self.e1.bind("<Return>",self.evCopiaTexto_a)
          self.e1.grid(row=0, column=1, sticky=W)
          self.e2.grid(row=1, column=1, sticky=W)
 

          self.button1 = Button(minhaArea)
          self.button1.configure(text="OK",command=self.evCopiaTexto)
          self.button1.grid(row=2,column=0,sticky=W) #coloca o botao bem no canto esquerdo

          self.button2 = Button(minhaArea)
          self.button2.configure(text="Cancelar", command=self.evFecharPrograma)
          self.button2.grid(row=2,column=1,sticky=E) #coloca o botao bem no canto direito

      def evFecharPrograma(self):
          print "Tchau!"
          self.myParent.destroy() 

      def evCopiaTexto_a(self, event):
          self.evCopiaTexto() 

      def evCopiaTexto(self):
          print "Copia o texto ",self.e1.get()," do widget 1 para o widget 2"  
          self.e2.delete(0,END)
          texto = self.e1.get()
          self.e2.insert(END, texto)
 

root=Tk()
app = Dialogo(root)
root.mainloop()
          
