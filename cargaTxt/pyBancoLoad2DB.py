from pyPgSQL import PgSQL

class Banco():
      def __init__(self,estr,lista,dataSourceName):
          self.estrutura = estr
          self.listaValores = lista
          self.listaInsert = []
          self.db = PgSQL.connect(dataSourceName)
          self.cu = self.db.cursor()
      #   self.nomeTabela = nometab
    
      # def criarTabelaQualquer(self):
      # def getCabecalhoTabelaQualquer(self):
      # def montarDadosTabelaQualquer(self):

      # tabela de carga para plano de conta SIAFI
      def criarTabelaCargaTTC(self):
          try:
            self.cu.execute("DROP TABLE TTC_TABELA_TEMPORARIA_CONTA")
          except:
            pass

          self.db.commit()
          
          s = """ 
             CREATE TABLE TTC_TABELA_TEMPORARIA_CONTA( 
	     EXERCICIO integer, 
	     GR_CODIGO_CONTA integer, 
	     IT_NO_CONTA text, 
	     IT_TX_FUNCAO_CONTA text, 
	     IT_TX_CIRCUNSTANCIA_DEBITO text, 
	     IT_TX_CIRCUNSTANCIA_CREDITO text, 
	     IT_IN_CONTA_CORRENTE_CONTABIL integer, 
	     IT_IN_ENCERRAMENTO integer, 
	     IT_IN_INVERSAO_SALDO integer, 
	     IT_IN_ESCRITURACAO integer, 
	     IT_IN_SALDOCONTABIL varchar(2), 
	     IT_IN_CONTA_CAMBIO integer, 
	     SB_NATUREZA_DESPESA integer 
	     );          """
          self.cu.execute(s)
          self.db.commit()       

      # tabela de carga para saldo de contas
      def criarTabelaCargaTTS(self):
          try:
            self.cu.execute("DROP TABLE TTS_TABELA_TEMPORARIA_SALDO")
          except:
            pass

          self.db.commit()
          
          s = """
                        CREATE TABLE TTS_TABELA_TEMPORARIA_SALDO(  
    	 		EXERCICIO    integer,
	 		IT_CO_GESTAO      integer,
		 	IT_CO_UNIDADE_GESTORA                   integer,
		        GR_CODIGO_CONTA                         integer,
		   	IT_CO_CONTA_CORRENTE_CONTABIL           varchar(43),
	       	        DESCRICAO_CC				 varchar(108),
    	       	        IT_VA_DEBITO_INICIAL                    numeric(17,2),
    	       	        IT_VA_CREDITO_INICIAL                   numeric(17,2),
                      """
          for i in range(1,15):
              s = s + "IT_VA_DEBITO_MENSAL_%d_       numeric(17,2), " % i

          for i in range(1,15):
              s = s + "IT_VA_CREDITO_MENSAL_%d_       numeric(17,2)" %i
              if (i<14):
                 s = s + ", "
          
          s = s + ");"

          self.cu.execute(s)
          self.db.commit()       


         
      def retiraCaracteresEspeciais(self, str):
          str = str.replace("'","")
          str = str.replace("\"","")
          return str


      def verificaTipoEstrutura(self, di, diEstrutura, nome):
          vl = self.retiraCaracteresEspeciais(di[nome])
          if diEstrutura[nome][0]=="A":
             return "'" + vl + "'"
          else:
             return vl
          
      def formatar(self,valor):
          s = ""
          i = 0
          while i < 5:
                s = s + valor[i] + "."
                i = i + 1
          s = s + valor[5:7] + "."
          s = s + valor[7:9]
          return s
 

      def getCabecalhoInsertTTC(self):

          cabecalho = """
                 INSERT INTO TTC_TABELA_TEMPORARIA_CONTA(
                    EXERCICIO,
                    GR_CODIGO_CONTA, 
                    IT_NO_CONTA, 
                    IT_TX_FUNCAO_CONTA, 
                    IT_TX_CIRCUNSTANCIA_DEBITO, 
                    IT_TX_CIRCUNSTANCIA_CREDITO, 
                    IT_IN_CONTA_CORRENTE_CONTABIL,
                    IT_IN_ENCERRAMENTO,
                    IT_IN_INVERSAO_SALDO,
                    IT_IN_ESCRITURACAO,
                    IT_IN_SALDOCONTABIL,
                    IT_IN_CONTA_CAMBIO,
                    SB_NATUREZA_DESPESA) values ("""
          return cabecalho

      def getCabecalhoInsertTTS(self):
          cabecalho = """
                        INSERT INTO TTS_TABELA_TEMPORARIA_SALDO(  
    	 		EXERCICIO   ,
	 		IT_CO_GESTAO  ,
		 	IT_CO_UNIDADE_GESTORA ,
		        GR_CODIGO_CONTA       ,
		   	IT_CO_CONTA_CORRENTE_CONTABIL  ,
	       	        DESCRICAO_CC		       ,
    	       	        IT_VA_DEBITO_INICIAL                ,
    	       	        IT_VA_CREDITO_INICIAL               ,
                      """
          for i in range(1,15):
              cabecalho = cabecalho + "IT_VA_DEBITO_MENSAL_%d_, " % i

          for i in range(1,15):
              cabecalho = cabecalho + "IT_VA_CREDITO_MENSAL_%d_" % i
              if (i<14):
                 cabecalho = cabecalho + ", "
 
          cabecalho = cabecalho + ") VALUES ( "
          return cabecalho


# tabela temporaria TTC_TABELA_TEMPORARIA_CONTA 
      def montarDadosInsertTTC(self):
          diEstrutura = dict(self.estrutura)
          cabecalho = self.getCabecalhoInsertTTC()

          for listaTuplas in self.listaValores:
              s = cabecalho

              di = dict(listaTuplas)
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'EXERCICIO') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'GR-CODIGO-CONTA') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-NO-CONTA') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-TX-FUNCAO-CONTA') + ","

              vl = ""
              for i in range(1,21):
                  vl = vl + di["IT-TX-CIRCUNSTANCIA-DEBITO(%d)" % (i)] 

              s = s + "'" + self.retiraCaracteresEspeciais(vl) + " ' " + ","
              
              vl = ""
              for i in range(1,21):
                  vl = vl + di["IT-TX-CIRCUNSTANCIA-CREDITO(%d)" % (i)] 

              s = s + "'" + self.retiraCaracteresEspeciais( vl ) + " ' " + ","

              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-IN-CONTA-CORRENTE-CONTABIL') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-IN-ENCERRAMENTO') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-IN-INVERSAO-SALDO') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-IN-ESCRITURACAO') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-IN-SALDO-CONTABIL') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-IN-CONTA-CAMBIO') + ","
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'SB-NATUREZA-DESPESA') + ","
              s = s[0:len(s)-1] + ");"
             
              self.listaInsert.append(s)

      def formatarValor(self, valor):
          a = valor[0:17] + "." + valor[17:19] 
          return a

# tabela temporaria TTS_TABELA_TEMPORARIA_SALDO 
      def montarDadosInsertTTS(self):
          diEstrutura = dict(self.estrutura)
          cabecalho = self.getCabecalhoInsertTTS()

          for listaTuplas in self.listaValores:
              s = cabecalho

              di = dict(listaTuplas)
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'EXERCICIO') + ","                  
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-CO-GESTAO') + ","                  
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-CO-UNIDADE-GESTORA') + ","         
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'GR-CODIGO-CONTA') + ","               
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'IT-CO-CONTA-CORRENTE-CONTABIL') + "," 
              s = s + self.verificaTipoEstrutura(di,diEstrutura,'DESCRICAO-CC') + "," 
              s = s + self.formatarValor(di['IT-VA-DEBITO-INICIAL']) + ","          
              s = s + self.formatarValor(di['IT-VA-CREDITO-INICIAL']) + ","          
              for i in range(1,15):
	          s = s + self.formatarValor(di['IT-VA-DEBITO-MENSAL(%d)' % i]) + ","        
              for i in range(1,15):
                  s = s + self.formatarValor(di['IT-VA-CREDITO-MENSAL(%d)' % i]) + ","
  

              s = s[0:len(s)-1] + ");"
             
              self.listaInsert.append(s)

      def zerarListaInsert(self):
          self.listaInsert = []
 
      def carregarLista(self):
          for item in self.listaInsert:
              try:
                   self.cu.execute("SET CLIENT_ENCODING='ISO-8859-1'")
                   self.cu.execute(item)
                   self.db.commit()
              except:
                   print "ERRO        --------->  "   + item 


      def fecharConexao(self):
          self.cu.close()
          self.db.close()

      def imprimirLista(self):
          for i in self.listaInsert:
              print i
          


