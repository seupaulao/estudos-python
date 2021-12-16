from pyPgSQL import PgSQL
from pyFuncoesBasicas import *

# basico pypgsql
# db = connect(dsn)
# curs = db.cursor()
# curs.execute(sql)                                        # DELETE,INSERT,UPDATE,CREATE,DROP,ALTER TABLE,SELECT
# curs.executemany("INSERT basic VALUES(%s, %s)", params)  # params sao os valores a serem adicionados, funciona como um batch do JAVA
#
# res = curs.fetchone()                                    # traz um unico registro, o proximo
# while res:
#     print " a=%d   b=%d" % (res.a, res.b)
#     res = curs.fetchone()
#
# curs.rewind()                                            # funciona como o ResultSet.BeforeFirst() do JAVA
# acessando os campos pode ser,
# res[0], res[1], ...
# res["colunaA"], res["colunaB"], ...
# res.colunaA, res.colunaB, ...
#
# self.curs.oidValue => OID, para detectar um INSERT
# self.curs.res.cmdTuples => numero de linhas afetadas por um DELETE ou UPDATE


class AtualizaPlanoConta():
   def __init__(self, dataSourceName):
      self.dsn = dataSourceName
      self.db = PgSQL.connect(self.getDSN)
      self.PCO = -1

   def setPCO(self, valor):
      self.PCO = valor

   def getPCO(self):
      return self.PCO
      
   def getExeIdtChave(self,ano):
      exeIdtChave = -1
      cur1 = self.db.cursor()
      cur2 = self.db.cursor()
      cur1.execute("select exe_idt_chave,exe_num_ano from exe_exercicio where exe_num_ano=%d" % ano)
      rs = cur1.fetchone() 
      if (rs):
         exeIdtChave = rs.exe_idt_chave
      else:
         cur2.execute("insert into exe_exercicio(exe_num_ano) values(%d)" % ano)
         self.db.commit()
         cur2.close()
         cur1.execute("select exe_idt_chave,exe_num_ano from exe_exercicio where exe_num_ano=%d" % ano)
         rs = cur1.fetchone()
         exeIdtChave = rs.exe_idt_chave
      cur1.close()
      return exeIdtChave

   def getMscIdtChave(self):
      mscIdtChave = -1
      cur1 = self.db.cursor()
      cur2 = self.db.cursor()
      cur1.execute("select msc_idt_chave, msc_dsc_mascara from msc_mascara where msc_dsc_mascara='#.#.#.#.#.##.##'")
      rs = cur1.fetchone() 
      if (rs):
         mscIdtChave = rs.msc_idt_chave
      else:
         cur2.execute("insert into msc_mascara(msc_dsc_mascara) values('#.#.#.#.#.##.##')")
         self.db.commit()
         cur2.close()
         cur1.execute("select msc_idt_chave, msc_dsc_mascara from msc_mascara where msc_dsc_mascara='#.#.#.#.#.##.##'")
         rs = cur1.fetchone()
         mscIdtChave = rs.msc_idt_chave
      cur1.close()
      return mscIdtChave
      
   def getTpbcIdtChave(self):
      cur1 = self.db.cursor()
      cur1.execute("select tpcb_idt_chave,tpcb_dsc_tipo from TPCB_TIPO_PLANO_CONTA_CONTABIL where tpcb_dsc_tipo='SIAFI'") 
      rs = cur1.fetchone()
      cur1.close()
      return rs["tpcb_idt_chave"]

   def getPcoIdtChave(self,anoExercicio, exeIdtChave, mscIdtChave, tpcbIdtChave):
      pcoIdtChave = -1
      cur1 = self.db.cursor()
      cur1.execute("select pco_idt_chave from pco_plano_conta where exe_idt_chave=%d and msc_idt_chave=%d and tpcb_idt_chave=%d" % (exeIdtChave, mscIdtChave, tpcbIdtChave))
      rs = cur1.fetchone()
      if (rs):
         cur1.close()
         return rs["pco_idt_chave"]
      else:
         nome = "SIAFI %d" % anoExercicio
         txt = "PLANO CONTA SIAFI %d" % anoExercicio
         cur1.execute("insert into pco_plano_conta(exe_idt_chave, msc_idt_chave, pco_dsc_nome, pco_txt_descricao, tpcb_idt_chave) values(%d,%d,'%s','%s',%d);" % (exeIdtChave, mscIdtChave, nome, txt, tpcbIdtChave)) 
         self.db.commit()
         cur1.execute("select pco_idt_chave from pco_plano_conta where exe_idt_chave=%d and msc_idt_chave=%d and tpcb_idt_chave=%d" % (exeIdtChave, mscIdtChave, tpcbIdtChave))
         rs = cur1.fetchone()
         cur1.close()
         return rs["pco_idt_chave"]


   def self.carregarContasContabeis(self, pcoIdtChave):
      cur1 = self.db.cursor()
      cur2 = self.db.cursor()
      cur1.execute(""" select  exercicio, gr_codigo_conta ,   it_no_conta ,   it_tx_funcao_conta ,   it_tx_circunstancia_debito ,   it_tx_circunstancia_credito , 
		      it_in_conta_corrente_contabil ,   it_in_encerramento ,   it_in_inversao_saldo ,   it_in_escrituracao ,   it_in_saldocontabil , 
		      it_in_conta_cambio ,   sb_natureza_despesa from ttc_tabela_temporaria_conta """)
      rs1 = cur1.fetchone()
      while rs1:
         funcao = FormatNumber()
         ctbDscNumero = funcao.formatarMascaraSIAFI(rs1["gr_codigo_conta"])
         ctbDscNome = rs1["it_no_conta"]
         ctbTxtDescricao = rs1["it_tx_funcao_conta"] + rs1["it_tx_circunstancia_debito"] + rs1["it_tx_circunstancia_credito"]
         ctbDscNatureza  = rs1["it_in_saldocontabil"]
	 ctbFlgEscrituracao = funcao.existe(rs1["it_in_escrituracao"] == 1, 'true', 'false')
	 ctbFlgAtualizacaoManual = 'false'
	 ctbItInContaCorrenteContabil = rs1["it_in_conta_corrente_contabil"]
	 ctbItInEncerramento= rs1["it_in_encerramento"]
	 ctbItInInversaoSaldo= rs1["it_in_inversao_saldo"]
	 ctbItInContaCambio= rs1["it_in_conta_cambio"]
	 ctbSbNaturezaDespesa= rs1["sb_natureza_despesa"]

         String dscTipo = funcao.identificaTipo(ctbDscNumero);


         strUp = """ 
                        UPDATE CTB_CONTA_CONTABIL SET 
                        ctb_dsc_nome = %d,
                        ctb_txt_descricao = '%s',
                        ctb_dsc_natureza = '%s',
                        ctb_flg_escrituracao = %s
			ctb_flg_atualizacao_manual = %s
                        ctb_it_in_conta_corrente_contabil = %d
			ctb_it_in_encerramento = %d
			ctb_it_in_inversao_saldo = %d
			ctb_it_in_conta_cambio = %d
			ctb_sb_natureza_despesa = %d
			ctb_dsc_tipo = '%s'
			 WHERE ctb_dsc_numero = '%s'
			 AND pco_idt_chave='%d';
                     """
         strUp = strUp % (ctbDscNome, ctbTxtDescricao, ctbDscNatureza, ctbFlgEscrituracao,ctbFlgAtualizacaoManual,ctbItInContaCorrenteContabil,ctbItInEncerramento,ctbItInInversaoSaldo,ctbItInContaCambio,ctbSbNaturezaDespesa,dscTipo,ctbDscNumero,pcoIdtChave)
         strIn = """
                   INSERT INTO 
                   ctb_conta_contabil(ctb_dsc_numero,ctb_dsc_nome,ctb_txt_descricao,ctb_dsc_natureza,
                   ctb_flg_escrituracao,ctb_flg_atualizacao_manual,ctb_it_in_conta_corrente_contabil,
                   ctb_it_in_encerramento,ctb_it_in_inversao_saldo,ctb_it_in_conta_cambio,ctb_sb_natureza_despesa,ctb_dsc_tipo,pco_idt_chave,ctb_idt_chave_pai) VALUES(
                   '%s', '%s', '%s', '%s', %s, %s, %d, %d, %d, %d, %d, '%s','%s', %d,null );
                 """
         strIn = strIn % (ctbDscNumero,ctbDscNome,ctbTxtDescricao,ctbDscNatureza,ctbFlgEscrituracao,ctbFlgAtualizacaoManual,ctbItInContaCorrenteContabil,ctbItInEncerramento,ctbItInInversaoSaldo,ctbItInContaCambio,ctbSbNaturezaDespesa,dscTipo,pcoIdtChave)

         cur2.execute(strUp)
         if (self.cur2.res.cmdTuples < 0):
            cur2.execute(strIn)

         rs1 = cur1.fetchone()

      self.db.commit()
      cur2.close()
      cur1.close()   
                

   def atualizandoPai(self, pcoIdtChave):
      cur1 = self.db.cursor()
      cur2 = self.db.cursor()
      consulta1 = "select ctb_idt_chave from ctb_conta_contabil ctb where ctb.ctb_dsc_numero = '%s'"
      consulta2 = "select ctb.ctb_idt_chave,ctb.ctb_dsc_numero from ctb_conta_contabil ctb where ctb.ctb_idt_chave_pai is null and pco_idt_chave = %d" % (pcoIdtChave)
      cur1.execute(consulta2)
      rs1 = cur1.fetchone 
      supdate = "UPDATE CTB_CONTA_CONTABIL SET CTB_IDT_CHAVE_PAI = %d  WHERE PCO_IDT_CHAVE ="+pcodIdtChave+"  AND CTB_IDT_CHAVE = %d "
      funcao = FormatNumber()
      while rs1:
          ctbIdtChave = rs1["ctb_idt_chave"]
          ctbDscNumero = rs1["ctb_idt_chave"]
          ctbDscNumeroPai = funcao.getNumeroDoPai(ctbDscNumero)
          sql1 = consulta1 % (ctbDscNumeroPai)
          cur2.execute(sql1)
          ctbIdtChavePai = -1
          res = cur2.fetchone()
          if (res):
             rsPai = cur2.fetchone()
             ctbIdtChavePai = rsPai["ctb_idt_chave"]
          else:
             while ctbDscNumeroPai != "" and ctbIdtChavePai == "":
                  ctbDscNumeroPai = funcao.getNumeroDoPai(ctbDscNumeroPai)
                  sql1 = consulta1 % (ctbDscNumeroPai)
                  cur2.execute(sql1)
                  res = cur2.fetchone()
                  if (res):
                     rsPai = cur2.fetchone()
                     ctbIdtChavePai = rsPai["ctb_idt_chave"]

          if (ctbIdtChavePai != ""):
             sql2 = supdate % (ctbIdtChavePai, ctbIdtChave)
             cur2.execute(sql2)

      self.db.commit()
      cur2.close()
      cur1.close()
 

   def atualizaPlanoConta(self):
      cur = self.db.cursor()
      cur.execute("select distinct exercicio from ttc_tabela_temporaria_conta")    
      rs = cur.fetchone()
      
      while rs:
          print "Iniciando o EXERCICIO..."
          anoExercicio = rs["exercicio"]
          exeIdtChave = self.getExeIdtChave(anoExercicio) 

          print "Iniciando a MASCARA..."
          mscIdtChave = self.getMscIdtChave()

          print "Iniciando TIPO PLANO CONTA..."
          tpcbIdtChave = self.getTpbcIdtChave()

          print "Procurando pelo Plano de Contas..."
          pcoIdtChave = self.getPcoIdtChave(anoExercicio, exeIdtChave, mscIdtChave, tpcbIdtChave)
          self.setPCO(pcoIdtChave)

          print "Carregando as Contas Contabeis..."
          self.carregarContasContabeis(pcoIdtChave)

          print "Atualizando somente aquelas contas onde o pai IS NULL"
          self.atualizandoPai(pcoIdtChave)




