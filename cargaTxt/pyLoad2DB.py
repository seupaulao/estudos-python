#from pyPgSQL import PgSQL
from pyBancoLoad2DB import * 
from pyEstruturaLoad2DB import *
from pyAtualizaPlanoConta import *
from pyAtualizaSaldoPlanoConta import *


# problemas encontrados
#       - formato do ARQUIVO ASCII 
#       - contraponto com o formato do banco UNICODE
#       - RESOLUCAO : SET CLIENT_ENCODING=ENCODING DO ARQUIVO CARREGADO
# carga completa
#       - acontece se o banco tambem eh ASCII
#
# fazer as validacoes do arquivo TXT para o BANCO 
# 
#
#

def opcaoEntradaArq(opcao, tipo):
     if opcao == 1:
        arq = "siafiPlanoConta.dat"
        ref = "PLANO_CONTABIL_SIAFI.ref"
        nom = "--- Carga PLANO CONTAS ---"
     elif opcao == 2:
        arq = "siafiSaldoContabil.dat"
        ref = "SALDO_CONTABIL.ref"
        nom = "--- Carga SALDO DE CONTAS ---"
     
     if tipo == 1:
        return arq
     elif tipo == 2:
        return ref
     elif tipo == 3:
        return nom

    
def selecionaCarga(opcao,dsn):
     est = Estrutura()
     if opcao == 1 or opcao == 2:
        print "Carregar Tabelas Temporarias"
        print opcaoEntradaArq(opcao, 3)

        print " Carregando estrutura do arquivo..."
        est.carrega( opcaoEntradaArq(opcao, 2) )          

        print " Carregando dados do arquivo..."
        car = Carga(est.getEstrutura(), est.tamanhoRegistro())
        car.carrega( opcaoEntradaArq(opcao, 1))
        # est.imprime()
        # print "---------------------------- "
        # car.imprimeDados()
        # print "---------------------------- "
        # print "Saindo"
        # sys.exit(0)
        print " Criando o Banco e Carregando as Tabelas Temporarias "
        banco = Banco(est.getEstrutura(), car.getDados(), dsn)
        if opcao == 1:
           banco.criarTabelaCargaTTC()
           banco.montarDadosInsertTTC()
        else:
           banco.criarTabelaCargaTTS()
           banco.montarDadosInsertTTS()        
        # banco.imprimirLista()
        banco.carregarLista()
        banco.fecharConexao()

     elif opcao == 3:
        print "--- Atualizar Plano de Contas ---"
        planoConta = AtualizaPlanoConta(dsn)
        planoConta.atualizaPlanoConta()

     elif opcao == 4:
        print "--- Atualizar Saldo de Contas SIAFI ---"
        saldoConta = AtualizaSaldoPlanoConta(dsn)
        saldoConta.atualizaSaldoPlanoConta()

#     elif opcao == 5:
#        print "--- Criticar Rateio Contas ---"
#
#     elif opcao == 6:
#        print " --- Replicar Plano de Contas para um novo Exercicio ---"

     else: 
        print "----> Rodar TODOS os Processos <----"
        print "Carregando TTC..."
        banco.criarTabelaCargaTTC()
        banco.montarDadosInsertTTC()
        print "Carregando TTS..."
        banco.criarTabelaCargaTTS()
        banco.montarDadosInsertTTS()
        print "Carregando Contas Contabeis..."
        planoConta = AtualizaPlanoConta()
        planoConta.atualizaPlanoConta()
        print "Carregando Contas Corrente e Saldo..."
        saldoConta = AtualizaSaldoPlanoConta()
        saldoConta.atualizaSaldoPlanoConta()
#        print "Validando Rateio de Saldos..."
#        print "Verificando Replicar Relacionamentos e Contas Corrente..."
      
        
       
if __name__ == "__main__":
     import sys
     dsn="10.200.103.52:5433:dbd_baldi_carga2:postgres:scfla100"
     opcao = sys.argv[1] 
     if opcao == "":
        op = 0
     else:
        op = int(opcao)

     selecionaCarga(op, dsn) 




