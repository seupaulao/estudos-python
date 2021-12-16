def imgcrypt(entrada):
    saida=[]
    for i in range(1,len(entrada)-1,1):
        temp = []
        for j in range(1,len(entrada[0])-1,1):
            valor = (entrada[i][j] + entrada[i-1][j-1] + entrada[i-1][j] + entrada[i-1][j+1] + entrada[i][j-1] + entrada[i][j+1] + entrada[i+1][j-1] + entrada[i+1][j] + entrada[i+1][j+1])//(3*3)
            temp.append(valor)
        saida.append(temp)
    return saida        


print( imgcrypt([[1,1,1],[1,7,1],[1,1,1]]) )
print( imgcrypt([[1,1,1],[1,7,1],[1,1,1],[4,5,7]]) )
print( imgcrypt([[1,1,1,5],[1,7,1,9],[1,1,1,11]]) )
print( imgcrypt([[1,1,1,2],[1,7,1,6],[1,1,1,5],[4,2,14,3]]) )
