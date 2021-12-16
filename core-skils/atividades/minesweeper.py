# matrix = [[true, false, false],
#          [false, true, false],
#          [false, false, false]]
#
#minesweeper(matrix) = [[1, 2, 1],
#                       [2, 1, 1],
#                       [1, 1, 1]]
def verifica(tamanho, matrix, saida):
    for i in range(tamanho):
        for j in range(tamanho):
            if matrix[i][j]==True:
                if i-1 >= 0:
                    if j-1 >= 0: 
                        saida[i-1][j-1] += 1
                    saida[i-1][j] += 1
                    if j+1 <= tamanho-1: 
                        saida[i-1][j+1] += 1
                if j-1 >= 0: 
                    saida[i][j-1] += 1
                if j+1 <= tamanho-1: 
                    saida[i][j+1] += int(1)
                if i+1<=tamanho-1:
                    if j-1 >= 0: 
                        saida[i+1][j-1] += 1
                    saida[i+1][j] += 1
                    if j+1 <= tamanho-1: 
                        saida[i+1][j+1] += 1
    return saida

def montar(tamanho):
    saida = []
    for i in range(tamanho):
        t = []
        for j in range(tamanho):
            t.append(0)
        saida.append(t)
    return saida 
    
def minesweeper(matrix):
    tamanho = len(matrix[0])
    saida = montar(tamanho)
    return verifica(tamanho,matrix,saida)    

                

print( minesweeper([[True, False, False], [False, True, False], [False, False, False]]))
print( minesweeper([[False, False, False], [False, False, False], [False, False, False]]))

