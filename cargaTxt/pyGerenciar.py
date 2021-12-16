class GerenciaLog():
      def __init__(self,banco):
          self.db = banco

      def addMsgLog(self, descricao):
          self.println(descricao)
          sql = "INSERT INTO TLO_TABELA_LOG (TLO_DSC_MENSAGEM, TLO_DAT_MENSAGEM) VALUES ('%s',current_timestamp);" % descricao
          st = self.db.cursor()
          st.execute(sql)
          self.db.commit()
          st.close()

      def closeFileMsgLog(self):
          self.FILE.close()

      def openFileMsgLog(self):
          self.FILE = open("atualizacao_saldo.log", w)

      def addMsg(self, msg):
          self.FILE.write("%s \n" % msg)

      def println(self, msg):
          print msg
          self.addMsg(msg)
 
      
      

class GerenciaEmail():
      def __init__(self, banco,baldilink):
          self.db = banco
          self.link = baldilink
          
      def getLinkMensagemEmail(self):
          return "<a href='"+self.link+"'>BALDI</a>"

      def getNomeContaContabil(self, conta):
          st = self.db.cursor()
          st.execute("select ctb_dsc_nome from ctb_conta_contabil where ctb_dsc_numero = '%s'" % conta)
          rs = st.fetchone()
          st.close()
          return rs["ctb_dsc_nome"]
 
      def getTamanhoResultSet(self, st):
          return st.res.cmdTuples

      def getConsultaTabelaEmails(self, contaContabil):
          sql = """
	  select ccr_dsc_numero, ccr_dsc_nome, ctb_dsc_numero, ctb_dsc_nome, 
	  sum(janeiro) as janeiro,sum(fevereiro) as fevereiro, sum(marco) as marco,  
	  sum(abril) as abril,sum(maio) as maio, sum(junho) as junho,  
	  sum(julho) as julho,sum(agosto) as agosto, sum(setembro) as setembro,  
	  sum(outubro) as outubro, sum(novembro) as novembro, sum(dezembro) as dezembro
	  from ( 
	  select ccr_dsc_numero, ccr_dsc_nome, ctb.ctb_dsc_numero, ctb.ctb_dsc_nome,
	  case when eme.eme_num_mes=1 then scr.scr_val_saldo else 0 end as janeiro, 
	  case when eme.eme_num_mes=2 then scr.scr_val_saldo else 0 end as fevereiro,  
	  case when eme.eme_num_mes=3 then scr.scr_val_saldo else 0 end as marco,  
	  case when eme.eme_num_mes=4 then scr.scr_val_saldo else 0 end as abril,  
	  case when eme.eme_num_mes=5 then scr.scr_val_saldo else 0 end as maio,  
	  case when eme.eme_num_mes=6 then scr.scr_val_saldo else 0 end as junho,  
	  case when eme.eme_num_mes=7 then scr.scr_val_saldo else 0 end as julho,  
	  case when eme.eme_num_mes=8 then scr.scr_val_saldo else 0 end as agosto,  
	  case when eme.eme_num_mes=9 then scr.scr_val_saldo else 0 end as setembro,  
	  case when eme.eme_num_mes=10 then scr.scr_val_saldo else 0 end as outubro,  
	  case when eme.eme_num_mes=11 then scr.scr_val_saldo else 0 end as novembro,  
	  case when eme.eme_num_mes=12 then scr.scr_val_saldo else 0 end as dezembro  
	  from scr_saldo_conta_corrente scr 
	  inner join eme_exercicio_mes eme on scr.eme_idt_chave = eme.eme_idt_chave 
	  inner join ccr_conta_corrente ccr on scr.ccr_idt_chave = ccr.ccr_idt_chave 
	  inner join ctb_conta_contabil ctb on ctb.ctb_idt_chave = scr.ctb_idt_chave  
	  where ctb_dsc_numero = '%s'  
	  order by 5 ) as tabela 
	  group by ccr_dsc_numero, ccr_dsc_nome, ctb_dsc_numero, ctb_dsc_nome 		
          """
          sql = sql % contaContabil
          return sql

      def getConsultaTabelaEmails(self, contaContabil, contaCorrente):
          sql = """
	  select ccr_dsc_numero, ccr_dsc_nome, ctb_dsc_numero, ctb_dsc_nome, 
	  sum(janeiro) as janeiro,sum(fevereiro) as fevereiro, sum(marco) as marco,  
	  sum(abril) as abril,sum(maio) as maio, sum(junho) as junho,  
	  sum(julho) as julho,sum(agosto) as agosto, sum(setembro) as setembro,  
	  sum(outubro) as outubro, sum(novembro) as novembro, sum(dezembro) as dezembro
	  from ( 
	  select ccr_dsc_numero, ccr_dsc_nome, ctb.ctb_dsc_numero, ctb.ctb_dsc_nome,
	  case when eme.eme_num_mes=1 then scr.scr_val_saldo else 0 end as janeiro, 
	  case when eme.eme_num_mes=2 then scr.scr_val_saldo else 0 end as fevereiro,  
	  case when eme.eme_num_mes=3 then scr.scr_val_saldo else 0 end as marco,  
	  case when eme.eme_num_mes=4 then scr.scr_val_saldo else 0 end as abril,  
	  case when eme.eme_num_mes=5 then scr.scr_val_saldo else 0 end as maio,  
	  case when eme.eme_num_mes=6 then scr.scr_val_saldo else 0 end as junho,  
	  case when eme.eme_num_mes=7 then scr.scr_val_saldo else 0 end as julho,  
	  case when eme.eme_num_mes=8 then scr.scr_val_saldo else 0 end as agosto,  
	  case when eme.eme_num_mes=9 then scr.scr_val_saldo else 0 end as setembro,  
	  case when eme.eme_num_mes=10 then scr.scr_val_saldo else 0 end as outubro,  
	  case when eme.eme_num_mes=11 then scr.scr_val_saldo else 0 end as novembro,  
	  case when eme.eme_num_mes=12 then scr.scr_val_saldo else 0 end as dezembro  
	  from scr_saldo_conta_corrente scr 
	  inner join eme_exercicio_mes eme on scr.eme_idt_chave = eme.eme_idt_chave 
	  inner join ccr_conta_corrente ccr on scr.ccr_idt_chave = ccr.ccr_idt_chave 
	  inner join ctb_conta_contabil ctb on ctb.ctb_idt_chave = scr.ctb_idt_chave  
	  where ctb_dsc_numero = '%s'  
	  and ccr_dsc_numero='%s' 
	  order by 5 
	  ) as tabela 
	  group by ccr_dsc_numero, ccr_dsc_nome, ctb_dsc_numero, ctb_dsc_nome 		
          """
          sql = sql % (contaContabil, contaCorrente)
          return sql
      
      def getConTabEmCcrRat(self, contaContabil, contaCorrente):
          sql = """
          select ccr_dsc_numero, ccr_dsc_nome, ctb_dsc_numero, ctb_dsc_nome, 
	  sum(janeiro) as janeiro,sum(fevereiro) as fevereiro, sum(marco) as marco,  
	  sum(abril) as abril,sum(maio) as maio, sum(junho) as junho,  
	  sum(julho) as julho,sum(agosto) as agosto, sum(setembro) as setembro,  
	  sum(outubro) as outubro, sum(novembro) as novembro, sum(dezembro) as dezembro
	  from ( 
	  select ccr_dsc_numero, ccr_dsc_nome, ctb.ctb_dsc_numero, ctb.ctb_dsc_nome,
	  case when eme.eme_num_mes=1 then scr.scr_val_saldo else 0 end as janeiro, 
	  case when eme.eme_num_mes=2 then scr.scr_val_saldo else 0 end as fevereiro,  
	  case when eme.eme_num_mes=3 then scr.scr_val_saldo else 0 end as marco,  
	  case when eme.eme_num_mes=4 then scr.scr_val_saldo else 0 end as abril,  
	  case when eme.eme_num_mes=5 then scr.scr_val_saldo else 0 end as maio,  
	  case when eme.eme_num_mes=6 then scr.scr_val_saldo else 0 end as junho,  
	  case when eme.eme_num_mes=7 then scr.scr_val_saldo else 0 end as julho,  
	  case when eme.eme_num_mes=8 then scr.scr_val_saldo else 0 end as agosto,  
	  case when eme.eme_num_mes=9 then scr.scr_val_saldo else 0 end as setembro,  
	  case when eme.eme_num_mes=10 then scr.scr_val_saldo else 0 end as outubro,  
	  case when eme.eme_num_mes=11 then scr.scr_val_saldo else 0 end as novembro,  
	  case when eme.eme_num_mes=12 then scr.scr_val_saldo else 0 end as dezembro  
	  from rts_relacao_saldo rts 
	  inner join rcr_relacao_saldo_conta_corrente rcr on rts.rcr_idt_chave = rcr.rcr_idt_chave 
	  inner join rcb_relacao_plano_conta_contabil rcb on rcr.rcb_idt_chave = rcb.rcb_idt_chave 
	  inner join scr_saldo_conta_corrente scr on scr.scr_idt_chave = rcr.scr_idt_chave 
	  inner join eme_exercicio_mes eme on scr.eme_idt_chave = eme.eme_idt_chave 
	  inner join ccr_conta_corrente ccr on scr.ccr_idt_chave = ccr.ccr_idt_chave 
	  inner join ctb_conta_contabil ctb on ctb.ctb_idt_chave = scr.ctb_idt_chave  
	  where ctb_dsc_numero = '%s'  
	  and ccr_dsc_numero='%s' 
	  order by 5 
	  ) as tabela 
	  group by ccr_dsc_numero, ccr_dsc_nome, ctb_dsc_numero, ctb_dsc_nome 		
          """
          sql = sql % (contaContabil, contaCorrente)
          return sql

      def getAssuntoMensagemEmail(self, tipo):
	  assunto = "";
	  if (tipo == "MSE002"):
	     assunto = "Sistema BALDI – ALERTA - Atualização de saldo de conta(s) sem relacionamento(s)";
    	  elif (tipo == "MSE003"): 
	     assunto = "Sistema BALDI – ALERTA - Atualização de saldo de conta(s) com o(s) mês(s) fechado(s)";
	  elif (tipo == "MSE004"): 
	     assunto = "Sistema BALDI – ALERTA - Atualização automática de saldo de conta(s) configurada(s) como manual(is)";
	  elif (tipo == "MSE005"): 
	     assunto = "Sistema BALDI – ALERTA - Atualização de saldo de conta(s) diverge de saldo distribuído informado ";
	  return assunto;
      
      def getCorTipoEmail(self, valor, tipo, mesAtual, mesCarga):
          val = ""
          if (mesAtual == mesCarga):
             if (tipo == "MSE003"):
                val = "<font color='#FF0000'>" + valor + "</font>"
             elif (tipo == "MSE004"):
                val = "<font color='#0000FF'>" + valor + "</font>" 	
             else:
                val = valor
          else:
             val=valor
          return val
   
      def getTabelaEmails(self, tipo, conta, mes):
          st = self.db.cursor()
          st.execute(self.getConsultaTabelaEmails())
          rs = st.fetchone()
          tabhtml = ""
          if (rs):
             tabhtml = tabhtml + "<table><tr> <th>CONTA</th> <th>NOME</th> "
             # TODO : continuar



