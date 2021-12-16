from pyPgSQL import PgSQL
from pyFuncoesBasicas import *
from pyAtualizaPlanoConta import *
from pyGerenciar import *

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

class AtualizaSaldoPlanoConta():
      def __init__(self, dataSourceName,pcoIdtChave,testarContaSemRel,emailsResponsaveis):
          self.dsn = dataSourceName
          self.db = PgSQL.connect(self.getDSN)
          self.pcoIdtChave = pcoIdtChave
	  self.sstUpdate = "update SCR_SALDO_CONTA_CORRENTE SET SCR_FLG_ATUALIZADO=%s, SCR_VAL_DEBITO_INICIAL=%s, SCR_VAL_CREDITO_INICIAL=%s, SCR_VAL_SALDO=%s, SCR_DSC_UNIDADE_GESTORA='%s' WHERE SCR_IDT_CHAVE=%d ;";
	  self.sstInsert = "insert into SCR_SALDO_CONTA_CORRENTE(CTB_IDT_CHAVE,EME_IDT_CHAVE,CCR_IDT_CHAVE,SCR_FLG_ATUALIZADO,SCR_VAL_DEBITO_INICIAL,SCR_VAL_CREDITO_INICIAL,SCR_VAL_SALDO, SCR_DSC_UNIDADE_GESTORA) VALUES (%d,%d,%d,%s,%s,%s,%s,'%s');";
 	  self.consulta1 = "select eme_idt_chave,seme_idt_chave from eme_exercicio_mes where eme_num_mes=%d and exe_idt_chave=%d";
          self.consulta2 = "select ctb_idt_chave,ctb_flg_atualizacao_manual from ctb_conta_contabil where ctb_dsc_numero = '%s' and pco_idt_chave=%d"; 
          self.aPC = AtualizaPlanoConta(self.dsn)
          self.tcsr = testarContaSemRel           # default true, opcional false
          self.funcao = FormatNumber()
          self.emails = emailsResponsaveis        # [(nome, email)]
          self.gerenciarEmail = GerenciarEmail()  # TODO: escrever esta classe
          self.gerenciaLog = GerenciarLog()       
          self.dicionario  = []

      def atualizaSaldoPlanoConta(self):
          print "Carregando Contas Corrente..."
          carregaContasCorrente()

          tpcbIdtChave = aPC.getTpbcIdtChave()
          print "Teste das contas sem relacionamento"
          if (tcsr):
             testeContasSemRelacionamento()
         
          print "Montando tabela de chaves do Saldo de Contas"
          montarDicionarioScrIdtChave()
          
          print "Inicio da Carga dos Saldos..."
          # TODO: criar a rotina de carregar saldos
          
      def montarDicionarioScrIdtChave(self):
          sql = "select scr_idt_chave, ctb_idt_chave, eme_idt_chave, ccr_idt_chave, scr_dsc_unidade_gestora from scr_saldo_conta_corrente"
          st = self.db.cursor()
          st.execute(sql)
          rs = st.fetchone()
          lista = []
          while rs:
                chave = "%d_%d_%d_%d" % (rs["ctb_idt_chave"], rs["eme_idt_chave"], rs["ccr_idt_chave"], rs["scr_dsc_unidade_gestora"])
                lista.append((chave, rs["scr_idt_chave"])) 
          self.dicionario = dict(lista)
           


      # TODO:implementar as funcoes de acordo com o JAVA
      def gerarPendencia(self, scr, saldoAtual, observacao, acao):

      def carregarValoresSaldoAnterior(self, ctb, ccr, eme, scr, DEBINICIAL, CREDINICIAL, DEBMENSAL, CREDMENSAL,saldoAtual):

      def existeDivergenciaSaldoRateio(self, numContaContabil, numContaCorrente, mesCarga, pcbIdtChave, emeIdtChave, ccrIdtChave, pcoIdtChave, valorRateio):

      def existeAtualizacaoContasSaldoManual(self, flag, numContaContabil, numContaCorrente, mesCarga, pcoIdtChave):

      def existeAtualizacaoMesFechado(self, contaContabil, contaCorrente, ctbIdtChave, emeIdtChave, ccrIdtChave, mesCarga, pcoIdtChave, saldoNovo):

      def existeRelacionamentoOutrasContas(self,st,conta,mes):
          rs = st.fetchone()
          if (rs):
                descricao = "Conta de Numero %s de conta corrente sem relacionamento com outra conta" % conta
		self.gerenciarLog.addMsgLog(self.db, descricao);
                tipo = "MSE002"
                assunto = self.gerenciarEmail.getAssuntoMensagemEmail(tipo)
                msg = self.gerenciarEmail.getCorpoMensagemEmail(self.db,tipo,conta,mes)
                self.gerenciarEmail.enviarEmail(self.emails, assunto, msg)
           
      def testeContasSemRelacionamento(self):
          sql = "select distinct gr_codigo_conta from tts_tabela_temporaria_saldo"
          st = self.db.cursor()
          st1 = self.db.cursor()
          st.execute(sql)
          rs = st.fetchone()
          while rs:
                conta = self.funcao.formatarMascaraSIAFI(rs["gr_codigo_conta"])
                for mes in range(1,13):
                    sql = "select count(*) from rcb_relacao_plano_conta_contabil rcb inner join ctb_conta_contabil ctb on rcb.ctb_idt_chave_origem = ctb.ctb_idt_chave where ctb.ctb_dsc_numero='%s'" % conta
                    st1.execute(sql)
                    existeRelacionamentoOutrasContas(st1,conta,mes)  
          st1.close()
          st.close()     
      
      def carregaContasCorrente(self):
          sql = " select distinct it_co_conta_corrente_contabil,descricao_cc from tts_tabela_temporaria_saldo "
          si = " insert into ccr_conta_corrente(ccr_dsc_nome,ccr_dsc_numero) values ('%s','%s') "
          su = " update ccr_conta_corrente set ccr_dsc_nome = '%s' where ccr_dsc_numero='%s' "
          st = self.db.cursor()
          st1 = self.db.cursor()
          st.execute(sql)
          rs1 = st1.fetchone()
          while rs1:
                temp = su % (rs1["descricao_cc"], rs1["it_co_conta_corrente_contabil"])
                st1.execute(temp)
                if (self.curs.res.cmdTuples <= 0):
                   temp = si % (rs1["it_co_conta_corrente_contabil"], rs1["descricao_cc"])
                   st1.execute(temp)
                rs1 = st1.fetchone()
          st1.close()
          st.close()


