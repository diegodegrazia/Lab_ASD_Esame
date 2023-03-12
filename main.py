from SetElement import *
from Graph import *

def union(x, y):
    if x.setPtr is None:
        x.make_set()
    if y.setPtr is None:
        y.make_set()
    if x.find_set() != y.find_set():
        tmp = y.find_set()  # primo elemento della lista che sposterò
        app = x.find_set()
        while app.nextPtr is not None:
            app = app.nextPtr
        app.nextPtr = tmp  # collego l'ultimo elemento della lista di x con il primo della lista di y
        while tmp is not None:  # scorro la lista di y per aggiornare i setPtr
            tmp.setPtr = x.setPtr
            tmp = tmp.nextPtr
    else:
        print("Errore: I due insiemi non sono disgiunti")

"""def connected_components(G):
    for v in G.adj:
        v.make_set()
        

a = SetElement('a')
b = SetElement('b')
c = SetElement('c')
d = SetElement('d')
e = SetElement('a')

union(a,d)
union(a,c)
union(c,c)

tmp = d.find_set()
while tmp is not None:
    print(tmp.value)
    tmp = tmp.nextPtr """

G = Graph(6)
G.edgeInsert(0,1)
G.edgeInsert(2,4)
G.edgeInsert(3,0)
G.edgeInsert(1,2)
G.edgeInsert(2,0)
G.printGraph()