from Tkinter import *
# <Button-1>, <Button-2>, <Button-3>   : botoes esquerdo, meio e direito do mouse respectivamente
# <Enter> : dispara quando o mouse entra no Widget
# <Leave> : dispara quando o mouse sai no Widget
# <Return>: disparado quando o usuario digita a tecla ENTER - pode ser substituido por : Control_L, Control_R,Shift_L,Shit_R,Left,Up,Down,Right,F1..12,Num_Lock,Scroll_Lock,Escape,etc.
# <Key>   : disparado quando o usuario digita uma tecla
# quando usa-se grid, somente a janela desce como pack, os componentes descem somente como grid, senao havera conflito
# dentro de cada celula da grid, os widgets estao centralizados, para reposiciona-los utiliza-se sticky=N,S,E, ou W
#
class ContasMes:

      def __init__(self, num_mes, ano, salario, plan):
          self.plano = plan
          self.nmes = num_mes
          self.ano = ano
          self.salario = salario

      def escreveTexto(self, texto, tamanho, caractere, valor, opc=">"):
          texto = texto + (tamanho - len(texto) + 1) * caractere + opc 
          return texto + str(valor)


      def calculo_outras(self, outras):
          total = 0
          for ind, valor in outras.items():
              total = total + valor
          return total  


      def calculo_salario_final(self, salario, desconto):
          valor = salario - desconto
          a = "= SALARIO LIQUIDO  "
          v = self.escreveTexto(a, 40, "=", valor)
          return v



class Dialogo:
      def __init__(self, parent):
          self.myParent = parent
          minhaArea = Frame(parent)
          minhaArea.pack()
          
          self.vet = []
          self.vet.append("Agua")
          self.vet.append("Luz")
          self.vet.append("Telefone")
          self.vet.append("TV Assinatura")
          self.vet.append("Carro")
          self.vet.append("Seguro Carro")
          self.vet.append("IPVA Carro")
          self.vet.append("Imp Carro")
          self.vet.append("Moto")
          self.vet.append("Seguro Moto")
          self.vet.append("IPVA Moto")
          self.vet.append("Imp Moto")
          self.vet.append("Imposto Qualquer")
          self.vet.append("IRPF")
          self.vet.append("Faculdade")
          self.vet.append("VISA")
          self.vet.append("MASTERCard")
          self.vet.append("HIPERCard")
          self.vet.append("RIACHUELL")
          self.vet.append("MARISA")
          self.vet.append("Outros Valores")

          Label(minhaArea, text="Mes").grid(row=0, column=0)
          Label(minhaArea, text="Ano").grid(row=0, column=1)
          Label(minhaArea, text="Salario").grid(row=0, column=2)

          self.eMes = Entry(minhaArea)
          self.eMes.grid(row=1, column=0)
          self.eAno = Entry(minhaArea)
          self.eAno.grid(row=1, column=1)
          self.eSalario = Entry(minhaArea)
          self.eSalario.grid(row=1, column=2)

          self.entrada = []
          self.maxCampos = 21
          for i in range(self.maxCampos):
              self.entrada.append(Entry(minhaArea)) 

          Label(minhaArea, text="Agua").grid(row=3, column=0)
          Label(minhaArea, text="Luz").grid(row=3, column=1)
          Label(minhaArea, text="Telefone").grid(row=3, column=2)
          Label(minhaArea, text="TV Assin").grid(row=3, column=3)
          Label(minhaArea, text="Carro").grid(row=3, column=4)
          Label(minhaArea, text="Seg Carro").grid(row=3, column=5)
          Label(minhaArea, text="IPVA Carro").grid(row=3, column=6)
          for i in range(7):          
              self.entrada[i].grid(row=4, column=i)

          Label(minhaArea, text="Imp Carro").grid(row=5, column=0)
          Label(minhaArea, text="Moto").grid(row=5, column=1)
          Label(minhaArea, text="Seg Moto").grid(row=5, column=2)
          Label(minhaArea, text="Ipva Moto").grid(row=5, column=3)
          Label(minhaArea, text="Imp Moto").grid(row=5, column=4)
          Label(minhaArea, text="Imposto Q").grid(row=5, column=5)
          Label(minhaArea, text="IRPF").grid(row=5, column=6)
          for i in range(7):
              self.entrada[i+7].grid(row=6, column=i)

          Label(minhaArea, text="Faculdade").grid(row=7, column=0)
          Label(minhaArea, text="VISA").grid(row=7, column=1)
          Label(minhaArea, text="MASTER").grid(row=7, column=2)
          Label(minhaArea, text="HIPER").grid(row=7, column=3)
          Label(minhaArea, text="RIACHUELLO").grid(row=7, column=4)
          Label(minhaArea, text="MARISA").grid(row=7, column=5)
          Label(minhaArea, text="OUTROS").grid(row=7, column=6)
          for i in range(7):
              self.entrada[i+14].grid(row=8, column=i)

          
          self.entrada[20].bind("<Return>",self.evProcessaCampos_a)
 

          self.button1 = Button(minhaArea)
          self.button1.configure(text="OK",command=self.evProcessaCampos)
          self.button1.grid(row=9,column=2,sticky=E) #coloca o botao bem no canto esquerdo

          self.button2 = Button(minhaArea)
          self.button2.configure(text="Limpar", command=self.evLimparCampos)
          self.button2.grid(row=9,column=4,sticky=W) #coloca o botao bem no canto direito

          self.button3 = Button(minhaArea)
          self.button3.configure(text="Teste", command=self.evPreencherCamposTeste)
          self.button3.grid(row=9,column=6,sticky=W) #coloca o botao bem no canto direito

          self.text1 = Text(minhaArea)
          self.text1.grid(row=10, column=0,columnspan=4)
 

      def evPreencherCamposTeste(self):
          self.eMes.insert(END, "2")
          self.eAno.insert(END, "2011")
          self.eSalario.insert(END, "4400")
 
          self.entrada[0].insert(END,"20")
          self.entrada[1].insert(END,"100")
          self.entrada[2].insert(END,"120")
          self.entrada[3].insert(END,"55")
          self.entrada[4].insert(END,"660")
          self.entrada[5].insert(END,"0")
          self.entrada[6].insert(END,"0")
          self.entrada[7].insert(END,"0")
          self.entrada[8].insert(END,"0")
          self.entrada[9].insert(END,"0")
          self.entrada[10].insert(END,"0")
          self.entrada[11].insert(END,"0")
          self.entrada[12].insert(END,"0")
          self.entrada[13].insert(END,"200")
          self.entrada[14].insert(END,"200")
          self.entrada[15].insert(END,"200")
          self.entrada[16].insert(END,"200")
          self.entrada[17].insert(END,"200")
          self.entrada[18].insert(END,"200")
          self.entrada[19].insert(END,"200")
          self.entrada[20].insert(END,"0")

      def evProcessaCampos_a(self, event):
          self.evProcessaCampos()

 
      def evProcessaCampos(self):
          nMes = int(self.eMes.get())          
          nAno = int(self.eAno.get())
          nSal = float(self.eSalario.get()) 
          plano = {}
          for i in range( self.maxCampos ):
              plano[self.vet[i]] = float(self.entrada[i].get())

          self.text1.delete(1.0,END)
          contas = ContasMes(nMes,nAno,nSal,plano)

          mes=["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
          self.text1.insert(END, "-------------------- Mes " + mes[nMes-1]  + " / " +  str(nAno) + " ------------------------")
          self.text1.insert(END, "\n")
          self.text1.insert(END, contas.escreveTexto("Salario ", 40, " ", nSal, ":"))
          self.text1.insert(END,"\n") 
          for i in range(self.maxCampos):
              self.text1.insert(END, contas.escreveTexto(self.vet[i],40," ",float(self.entrada[i].get()),":"))
              self.text1.insert(END, "\n") 

          total_outras = contas.calculo_outras(plano) 
          subtotal2 = total_outras
          self.text1.insert(END,contas.escreveTexto("Total     ", 40, "-", subtotal2))
          self.text1.insert(END,"\n")
          self.text1.insert(END,contas.calculo_salario_final(nSal, subtotal2))
          self.text1.insert(END,"\n")
 
      def evLimparCampos(self):
          for i in range(self.maxCampos):
              self.entrada[i].delete(0,END)
          self.eMes.delete(0,END)
          self.eAno.delete(0,END)
          self.eSalario.delete(0,END)

           

root=Tk()
app = Dialogo(root)
root.mainloop()
          
