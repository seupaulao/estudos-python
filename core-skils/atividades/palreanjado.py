import itertools

#gerador de permutacoes
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

#uso de itertools.permutations
#solucao bonita, porem nao otima vai quebrar a maquina 
#no caso de len(x)>20 caracteres
def ehPalindromo(inputString):
    return sum([ it == it[::-1] for it in list(itertools.permutations(inputString,len(inputString)))]) > 0


def ehPal(s):
    if len(s)<2:
        return True
    else:
        lista = [j for j in s]
        contagem = [lista.count(i) for i in set(lista)]
        if len(set(lista)) == 1:
            return True
        else:
            if len(s) % 2 == 0:
                cpares = sum([p % 2 == 0 for p in contagem])
                if cpares == len(set(lista)):
                    return True
                else:
                    return False
            else:
                cimpar = [p % 2 != 0 for p in contagem]
                qi = sum(cimpar)
                qp = len(cimpar)-qi
                if qi == 1 and qp >= 1:
                    return True
                else:
                    return False




print(ehPal("z"))
print(ehPal("zaa"))
print(ehPal("zyyzzzzz"))
print(ehPal("aabb"))
print(ehPal("aaabb"))
print(ehPal("abca"))
print(ehPal("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"))




            
