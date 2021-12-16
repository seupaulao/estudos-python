
qteOcMel = int(raw_input("Ocorrencias de melhoria:"))
qteOc = int(raw_input("Ocorrencias :"))
qteDvExe = int(raw_input("Desvios de Execucao:"))
qteDv = int(raw_input("Desvios:"))


TotalNC = qteOcMel+qteOc+qteDvExe+qteDv
Total = 6*qteOcMel +  9*qteOc + 12*qteDvExe + 15*qteDv

print "Total Nao Conformidade : ", TotalNC
print "Total Pontos Nao Conformidade : ", Total 
print "Aderencia do Projeto   : ", 100-Total
