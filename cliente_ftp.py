import os
from ftplib import FTP
                                                                                                                                                                              
os.system("clear")
endereco_ftp = raw_input("Digite o endereco do ftp: ")
usuario = raw_input("Usuario: ")
senha = raw_input("Senha: ")
conexao_ftp = FTP(endereco_ftp)
                                                                                                  
print "\nFTP aberto: " + endereco_ftp + "\n"
conexao_ftp.login(usuario,senha)
print conexao_ftp.getwelcome() + "\n"
diretorio_corrente = conexao_ftp.pwd()
print "Diretorio corrente: " + diretorio_corrente + "\n"
conexao_ftp.retrlines('LIST')
                                                                                                  
def opcoes():
  opcao_quit = raw_input("Deseja sair?(sim/nao): ")
  if opcao_quit == "sim":
                                                                                                  
   print "Saindo...\n"
   conexao_ftp.quit()
                                                                                                  
  elif opcao_quit == "nao":
    diretorio_desejado = raw_input("Digite o diretorio para visualizacao: ")
    conexao_ftp.cwd(diretorio_desejado)
    conexao_ftp.retrlines('LIST')
    opcoes()
                                                                                                  
  else: print "Apenas digite sim ou nao!"
