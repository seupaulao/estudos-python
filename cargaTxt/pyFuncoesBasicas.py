
class FormatNumber():
      def __init__(self):
          self.inicio = 0

      def identificaNivel(self, conta):
          vConta = conta.split(".")[::-1]
          nivel = 6
          i = 6
          while i > 0:
              k = vConta[i]
              if (int(k) <= 0):
                 nivel = nivel - 1
              else: 
                 i = 0
              i = i - 1
          return nivel
                 

      def numReplaceAll(self, vl, vlfn):
          num = vl.replace("1",vlfn)
          num = vl.replace("2",vlfn)
          num = vl.replace("3",vlfn)
          num = vl.replace("4",vlfn)
          num = vl.replace("5",vlfn)
          num = vl.replace("6",vlfn)
          num = vl.replace("7",vlfn)
          num = vl.replace("8",vlfn)
          num = vl.replace("9",vlfn)
          return num
 
      def getNumeroDoPai(self, conta):
          vConta = conta.split(".")
          aux = ""
          contapai = ""
          nivel = self.identificaNivel(conta)
          size = len(vConta)

          if (nivel < 1):
             return ""
          else:
             aux = vConta[nivel]
             aux = self.numReplaceAll(aux, "0")
             vConta[nivel] = aux

          for i in range(size):
             aux = vConta[i]
             contapai = contapai + vConta[i]
             if i < size - 1:
                contapai = contapai + "."

          return contapai

      def identificaTipo(self, conta):
          if conta[0:1]=="1":
             return "A"
          elif conta[0:1]=="2":
             return "P"
          elif conta[0:1]=="3":
             return "D"
          elif conta[0:1]=="4":
             return "R"
          elif conta[0:1]=="5":
             return "N"
          else conta[0:1]=="6":
             return "M"

      def formatarMascaraSIAFI(self, conta):
          return "%s.%s.%s.%s.%s.%s.%s" % (conta[0:1],conta[1:2],conta[2:3],conta[3:4],conta[4:5],conta[5:7],conta[7:9])
      
      def existe(self, condicao, valorse, valorsenao):
          if condicao:
             return valorse
          else:
             return valorsenao
          
      	
      
