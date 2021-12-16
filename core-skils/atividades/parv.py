def analisa(a,b):
    if sorted(a) != sorted(b):
        return False
    else:
        fora = 0 
        for i in range(len(a)):
            if a[i] != b[i]:
                fora += 1
        if fora > 2:
            return False
        else:
            return True
                       

print(analisa([1,2,3],[1,2,3]))       
print(analisa([1,2,3],[2,1,3]))       
print(analisa([1,2,3],[3,1,2]))       
print(analisa([1,2,3],[3,2,3]))       
print(analisa([1,2,2],[2,1,1]))       
