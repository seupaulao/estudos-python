def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

def bbinaria(alist, chave, inicio, fim):
    meio = (inicio+fim)//2
    if alist[meio]==chave:
       return meio
    if inicio>=fim:
       return -1
    else: 
       if alist[meio] < chave:
          return bbinaria(alist, chave, meio+1, fim)
       return bbinaria(alist, chave, inicio, meio-1)


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
print(bbinaria(testlist, 2, 0, len(testlist)))
print(bbinaria(testlist, 32, 0, len(testlist)))
print(bbinaria(testlist, 14, 0, len(testlist)))
