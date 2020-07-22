import operator
def firstChars(L):
    lista = map(lambda x: x[0], L)
    lista2 = list(lista) 
    return lista2

def sum(L):
    soma = 0
    for i in L:
        soma = soma+i
    return soma

def avg(L):
    soma = 0
    for i in L:
        soma = soma+i
    return soma/len(L)

def maxString(L):
 
    return max(L, key=len)

def add2Dict(D, N, S):
    D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    D = {}
    for i in L:
        add2Dict(D, len(i), i)
    return D

def incValue(D, N):
    D[N] = D[N] + 1 if N in D else 1
    return D

def countFirsts(L):
    """ Conta o numero de ocorrencias do primeiro caracter de cada string em L.
    Por exemplo, countFirsts(['python', 'is', 'pythy']) === {'i': 1, 'p': 2}
    Note que essa funcao retorna um dicionario com cada caracter associada ao
    numero de strings que comecam com aquele caracter.
    """
    D = {}
    inic = firstChars(L)
    for i in inic:
        incValue(D, i)
    return D

def mostCommonFirstChar(L):
    """ Retorna a letra mais comum entre as primeiras letras de strings em L.
    Por exemplo:
    mostCommonFirstChar(['python', 'is', 'pythy']) === 'p'
    """
    D = countFirsts(L)
   # maior = max(D.items())
  #  result = filter(lambda x:x[1] == maior,D.items())
    return max(D, key=D.get)


a = ['python', 'is', 'pythy']
b = firstChars(a)
print(b)
#== ['p', 'i', 'p']
c = [1,2,3]
print(sum(c))
print(avg(c))
L0 = ['amar', 'o', 'estranho', 'deixa', 'confuso', 'este', 'coracao']
print(maxString(L0))
D = {1: ['b'], 2: ['xd'], 3: ['abc']}
print(add2Dict(D, 2, 'ww'))
print(buildLenFreq(['abc', 'xd', 'b', 'xxx']))
print(countFirsts(['python', 'is', 'pythy']))
print(mostCommonFirstChar(['python', 'is', 'pythy']))