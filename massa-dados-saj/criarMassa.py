#!/usr/bin/python

import random

padraoAviso = """INSERT INTO sajintegra.aviso(  tp_comunicacao,  dh_disponibilizacao,  dh_recebimento,  dh_ajuizamento,  co_orgao_julgador,  vl_causa,
  id_solicitacao_aviso,  in_situacao,  id_processo,  co_nivel_sigilo,  co_localidade,  id_comunicacao,  nr_classe_processual,  nr_classe_processual_original,
  ds_teor_comunicacao,  dh_ciencia_comunicacao,  dh_referencia_comunicacao,  tp_prazo_comunicacao,  nr_prazo,  dh_vencimento_comunicacao)VALUES(
  %s,  %s,  %s,  %s,  %s,  %s,  
  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  
  %s,  %s,  %s,  %s,  %s,  %s);"""

padraoSolicitacaoComunicacao = """
INSERT INTO sajintegra.solicitacao_comunicacao(  dh_solicitacao_comunicacao,  dh_atualizacao,  dh_proxima_execucao, in_situacao,  id_orgao_justica,  id_usuario,  id_aviso)
VALUES(  getdate(),  getdate(),  getdate(),  '%s',  %d,  %d,  %d);
"""

padraoHistoricoSolicitacaoComunicacao = """
INSERT INTO sajintegra.historico_solicitacao_comunicacao(  id_solicitacao_comunicacao,  dh_andamento,  in_situacao,  tx_mensagem,  in_situacao_aviso)
VALUES(  %d,  getdate(),  '%s',  '%s',  '%s');
"""
def posicao(lista):
    return random.randint(0, len(lista)-1) 

def getCoOrgaoJulgador():
    lista = ["'18'","'PE9'","'PE8'","'RN9'","'RN8'"]
    return lista[posicao(lista)]

def getValor():
    lista = [55000,113999.99,178282.0,21000.98]
    return lista[posicao(lista)]

def getIdSolicitacaoAviso():
    lista = [138,140,144,142]
    return lista[posicao(lista)]

def getIdProcesso():
    lista = [3100,3154,3188,3167]
    return lista[posicao(lista)]

def getCoLocalidade():
    lista = ["'234400'"]
    return lista[0]

def getIdComunicacao():
    lista=[20170117477455,20170117477456,20170117477457,20170117477458]
    return lista[posicao(lista)]

def escreve(fo, st):
    print st
    fo.write(st)

def getIdOrgaoJustica():
    lista=[190,191,192,193,194]
    return lista[posicao(lista)]

def criarAvisos(fo, qte):
    for i in range(qte):
        escreve(fo, padraoAviso % ("'INT'", "getDate()-10", "getDate()", "getDate()+200", "'18'", getValor(), getIdSolicitacaoAviso(), "'REC'",getIdProcesso(),0,getCoLocalidade(),getIdComunicacao(),"1116","null","'teor algum'","null","null","'PRZ'",10,"getDate()"))
    print "\n\n"

def criarSComunicacao(fo, firstKeyRangeAviso,qte):
    chave = firstKeyRangeAviso
    for i in range(qte): 
        escreve(fo, padraoSolicitacaoComunicacao % ("SOL",getIdOrgaoJustica(),2,chave))
        chave += 1 
    print "\n\n"

padraoHistoricoParte = """
INSERT INTO sajintegra.parte(  id_aviso,  tp_polo, tp_pessoa,  nr_documento,  tp_sexo,  no_parte)VALUES(
  %d,  '%s',  '%s',  '%s',  '%s',  '%s');
"""

padraoHistoricoProcessoVinculado = """
INSERT INTO sajintegra.processo_vinculado(  id_aviso,  nr_cnj_processo_vinculado,  tp_vinculo)VALUES(
  %d,  '%s',  '%s');
"""

padraoHistoricoAssuntoAviso = """
INSERT INTO sajintegra.assunto_aviso(  id_aviso,  id_assunto,  id_assunto_original,  in_principal)VALUES(
  %d,  %s,  %s,  '%s');
"""


def criarHSComunicacao(fo, firstKeySC, firstKeyAV, qte):
    chavesc = firstKeySC
    chaveav = firstKeyAV
    for i in range(qte):
        temp1 = padraoHistoricoSolicitacaoComunicacao % (chavesc, "SOL","VALOR ESCRITO X " + str(chavesc), "CCT")
        temp2 = padraoHistoricoSolicitacaoComunicacao % (chavesc, "DVA","VALOR ESCRITO Y " + str(chavesc), "CCT")
        escreve(fo, temp1)
        escreve(fo, temp2)
        chavesc += 1
    for i in range(qte):
        temp1 = padraoHistoricoParte % (chaveav, "PA","J", "11715983000169","D","TEXTO INVENTADO 10")
        escreve(fo, temp1)
        chaveav += 1 
    chaveav = firstKeyAV
    for i in range(qte):
        temp1 = padraoHistoricoProcessoVinculado % (chaveav, "00006987320164058308","DP")
        temp2 = padraoHistoricoProcessoVinculado % (chaveav, "00006987320164058307","OR")
        escreve(fo, temp1)
        escreve(fo, temp2)
	chaveav += 1 
    chaveav = firstKeyAV
    for i in range(qte):
        temp1 = padraoHistoricoAssuntoAviso % (chaveav, "6017","NULL","1")
        escreve(fo, temp1)
        chaveav += 1  
    print "\n"

def menu_gerarAviso():
    print "\nGerando SQL Avisos\n"
    qte = 1000
    try:
       qte = int(raw_input("Digite a quantidade:"))
    except:
       print "\nNumero Invalido. Estabelecendo 1000 inserts. Arquivo : avisos.sql."
       qte=1000
    fo = open("avisos.sql","w")
    criarAvisos(fo, qte)
    fo.close()

def menu_gerarSolicitacao():
    print "\nGerando SQL Solicitacao de Comunicacao\n"
    try:
       qte = int(raw_input("Digite a quantidade:"))
       inicio = int(raw_input("Digite o ponto de inicio:"))
       fo = open("solicitacoes.sql","w")
       criarSComunicacao(fo, inicio, qte)
       fo.close()
    except:
       print "\nNumero Invalido. Refaca a operacao."

def menu_gerarHistorico():
    print "\nGerando SQL Historico Solicitacao de Comunicacao\n"
    #try:
    qte = int(raw_input("Digite a quantidade:"))
    iniciosc = int(raw_input("Digite o id_solicitacao_comunicacao inicial:"))
    inicioav = int(raw_input("Digite o id_aviso inicial:"))
    fo = open("historicos.sql","w")
    criarHSComunicacao(fo, iniciosc, inicioav, qte)
    fo.close()
    #except:
    #   print "\nNumero Invalido. Refaca a operacao."
       
def menu():
    op = 0
    print "\nGerar Massa Dados SAJ \n"
    while op < 9:
       print "1. Gerar Avisos"
       print "2. Gerar Solicitacao de Comunicacao"
       print "3. Gerar Historico de Solicitacao de Comunicacao e demais"
       print "9. Sair"
       print "\n"
       try:
          op = int(raw_input("Escolha sua opcao:"))
       except:
          op = 0
       if (op==1):
          menu_gerarAviso()
       elif (op==2):
          menu_gerarSolicitacao()
       elif (op==3):
          menu_gerarHistorico()
       elif (op>=9):
          print "\nAte a Proxima!"
       else:
          print "\nOpcao Invalida. Repita a Operacao."

menu()


