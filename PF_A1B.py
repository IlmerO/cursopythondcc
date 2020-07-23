def head(L):
    return L[0]

def tail(L):
    return L[1]

def py2ll(L):
    if not L:
        return None
    else:
        return (L[0], py2ll(L[1:]))
def llrpy(L):
    if not L:
        return []
    else:
        H = head(L)
        T = tail(L) 
        return [H]+llrpy(T)

def size(L):
    if not L:
        return 0
    else:
        return 1 + size(tail(L))    

def split(L):
    if not L:
        return (None, None) #Lista vazia
    if not tail(L):
        return (L,None)    #Lista com somente 1 elemento
    else:
        H0 = head(L)
        H1 = head(tail(L))
        (T0,T1) = split(tail(tail(L)))
        return ((H0,T0),(H1,T1))

def sorted(L):
    if not L:
        return True #Listas vazias sempre ordenadas
    if not tail(L):
        return True #Listas com 1 elemento tbm sempre ordenadas
    else:
        C1 = head(L) <= head(tail(L))
        return C1 and sorted(head(tail(L)))

def merge(L0,L1):
    if not L0:
        return L1
    if not L1:
        return L0
    else:
        H0 = head(0)
        T0 = tail(0)
        H1 = head(L1)
        T1 = tail(L1)
        if H0 < H1:
            return (H0, merge(T0,L1))
        else:
            return (H1, merge(L0,T1))

def mSort(L):
    if not(L):
        return None
    if not tail(L):
        return L
    else:
        (L0,L1) = split(L)
        return merge(mSort(L0),mSort(L1))        