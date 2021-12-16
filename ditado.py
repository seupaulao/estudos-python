class Dicionario:
    def __init__(self):
        self.lsEsperanto=[]
        self.lsPortugues=[]
    
    def getListaEsperanto(self):
        return self.lsEsperanto

    def getListaPortugues(self):
        return self.lsPortugues

    def inserePalavra(self, port, esper):
        self.lsEsperanto.append(esper)
        self.lsPortugues.append(port)

    def imprimeLista(self):
        for i in range(len(self.lsEsperanto)):
            print self.lsEsperanto[i], '   :   ', self.lsPortugues[i]

    def alimentaDicionario(self):
        f = open('vortaro','r')
        lista = f.readlines()
        for lis in lista:
            x=lis.split(':')
            self.lsEsperanto.append(x[0].strip())
            self.lsPortugues.append(x[1].strip())
   
           
class Ditado:
      def __init__(self):
          self.acertos = 0
          self.erros   = 0   
      
      def addErro(self):
          self.erros = self.erros + 1
 
      def addAcerto(self):
          self.acertos = self.acertos + 1

      def getAcertos(self):
          return self.acertos

      def getErros(self):
          return self.erros

      def zeraPlacar(self):
          self.acertos=0
          self.erros=0

      def apresentacao(self):    
          print 'Treino de Esperanto:'
  	  print '\n'
	  print '0 - Treino Esperanto -> Portugues Sequencial'
	  print '1 - Treino Portugues -> Esperanto Sequencial'
	  print '2 - Sair'

      def busca(self, chave, conjunto1, index):
          ret = 0
          if chave.upper() == conjunto1[index].upper():
             ret = 1
          return ret

      def trEspePortSeq(self, lsEsp, lsPor):
          self.zeraPlacar()
          for i in range(len(lsEsp)):
              print '\nErros: ',self.getErros(),'        Acertos: ',self.getAcertos(), '      Palavra:',lsEsp[i], ':'
              r = raw_input('Traducao Portugues:')
              if r==':q': break
              res = self.busca(r,lsPor,i)
              if res == 1:
                 self.addAcerto()
                 print 'CERTO!!'
              else:
                 self.addErro()
                 print 'ERRADO =====>', lsPor[i] 

      def trPortEspeSeq(self, lsEsp, lsPor):
          self.zeraPlacar()
          for i in range(len(lsPor)):
              #print '\n',lsPor[i], ':'
              print '\nErros: ',self.getErros(),'        Acertos: ',self.getAcertos(), '      Palavra:',lsPor[i], ':'
              r = raw_input('Traducao Esperanto:')
              if r==':q': break
              res = self.busca(r,lsEsp, i)
              if res == 1:
                 self.addAcerto()
                 print 'TRE BONE!!'
              else:
                 self.addErro()
                 print 'MALBONE =====> ', lsEsp[i]





d = Dicionario()
d.alimentaDicionario()
dit = Ditado()
while 1:
      dit.apresentacao()
      opc = int(raw_input('Selecione uma opcao:'))
      if opc==0:
         dit.trEspePortSeq(d.getListaEsperanto(), d.getListaPortugues())
      elif opc==1:
         dit.trPortEspeSeq(d.getListaEsperanto(), d.getListaPortugues())
      elif opc==2:
         break





