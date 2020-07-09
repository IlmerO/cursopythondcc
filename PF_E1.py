def head(L):
    return L[0]
 
def tail(L):
    return L[1]

def py2ll(L):
    if not L:
        return None
    else:
        return (L[0], py2ll(L[1:]))

def ll2py(L):
    if not L:
        return []
    else:
        H = head(L)
        T = tail(L) 
        return [H]+ll2py(T)

def size(L):
    if not L:
        return 0
    else:
        return 1 + size(tail(L)) 

def sorted(L):
    if not L:
        return True #Listas vazias sempre ordenadas
    elif not tail(L):
        return True #Listas com 1 elemento tbm sempre ordenadas
    else:
        C1 = head(L) <= head(tail(L))
        return C1 and sorted(tail(L))

def sum(L):
    if not L:
        return None
    elif not tail(L):
        return head(L)           
    else:
        return head(L)+sum(tail(L))

def split(L):
    if not L:
        return (None, None) #Lista vazia
    elif not tail(L):
        return (L,None)    #Lista com somente 1 elemento
    else:
        H0 = head(L)
        H1 = head(tail(L))
        (T0,T1) = split(tail(tail(L)))
        return ((H0,T0),(H1,T1))


def merge(L0, L1):
    if not L0:
        return L1
    elif not L1:
        return L0
    else:
        H0 = head(L0)
        T0 = tail(L0)
        H1 = head(L1)
        T1 = tail(L1)
        if H0 < H1:
            return (H0, merge(T0,L1))
        else:
            return (H1, merge(L0,T1))

def mSort(L):
    if not(L):
        return None
    elif not tail(L):
        return L
    else:
        (L0,L1) = split(L)
        return merge(mSort(L0),mSort(L1))  

def get(L, N):
    L1 = ll2py(L)
    return L1[N]

def max(L):
    if not(L):
        return None
    elif not tail(L):
        return head(L)
    else:
        L1 = mSort(L)        
        return get(L1, size(L1)-1)

#print(max(py2ll([3, 4, 2, 5, 2, 1])))

#print(max(py2ll([0, 0, 0, 0])))

#print(max(py2ll([0, 0, 1, 0])))

#print(sorted(py2ll([1, 2, 3, 4, 5, 6])))

#print(sum(py2ll([0, 0, 1, 0])))

#print(sum(py2ll([1, 2, 3, 4])))
#print(get(py2ll([3, 4, 2, 5, 2, 1]), 0))

#print(get(py2ll([3, 4, 2, 5, 2, 1]), 1))
#print(get(py2ll([3, 4, 2, 5, 2, 1]), 2))