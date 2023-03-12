from ChainedSet import *
from SetElement import *

def make_set(x):
    a = ChainedSet(x, x)
    return a

def union(x,y):
    if x.setPtr is None:
        make_set(x)
    if y.setPtr is None:
         make_set(y)
    if find_set(x) != find_set(y):
        tmp_2 = find_set(y) #primo elemento della lista che sposterò
        app = find_set(x)
        while app.nextPtr is not None:
            app = app.nextPtr
        app.nextPtr = tmp_2 #collego l'ultimo elemento della lista di x con il primo della lista di y
        while tmp_2 is not None: #scorro la lista di y per aggiornare i setPtr
            tmp_2.setPtr = x.setPtr
            tmp_2 = tmp_2.nextPtr
    else:
        print("Errore: I due insiemi non sono disgiunti")

def find_set(x):
    if x.setPtr is not None:
        return x.setPtr.head
    else:
        return None

def connected_components(graph):
    for


a = SetElement('a')
b = SetElement('b')
c = SetElement('c')
d = SetElement('d')
e = SetElement('a')
union(a,d)
union(a,c)
union(b,c)
tmp = find_set(b)
while tmp is not None:
    print(tmp.node)
    tmp = tmp.nextPtr

