from SetElement import *
from Graph import *
from random import *
import matplotlib.pyplot as plt
from timeit import default_timer as timer


def heuristic_union(x,y):
    if x.setPtr.size < y.setPtr.size:
        union(y, x) #accodo l'insieme di x a quello di y
    else:
        union(x, y) #accodo l'insieme di y a quello di x

def union(x, y): #accodo l'insieme di y a quello di x
    if x.setPtr is None:
        x.make_set()
    if y.setPtr is None:
        y.make_set()
    if x.find_set() != y.find_set():
        tmp = y.find_set()  # primo elemento della lista che sposterò
        app = x.find_set()
        x.setPtr.size += y.setPtr.size #attributo size aggiornato
        while app.nextPtr is not None:
            app = app.nextPtr
        app.nextPtr = tmp  # collego l'ultimo elemento della lista di x con il primo della lista di y
        while tmp is not None:  # scorro la lista di y per aggiornare i setPtr
            tmp.setPtr = x.setPtr
            tmp = tmp.nextPtr
    else:
        print("Errore: I due insiemi non sono disgiunti")


def connected_components(G):
    for v in G.adj:
        v.make_set()
    for i in G.adj:
        for j in i.listPtr:
            if i.find_set() != j.find_set():
                union(i,j)

def same_components(u,v):
    if u.find_set() == v.find_set():
        return True
    else:
        return False

n = 10

G = Graph(n)

for i in range(0, randint(0, int(n*(n-1)/2))): #randomizzo numero degli archi (da 0 a nMax = n*(n-1)/2)
    G.edgeInsert(G.adj[randint(0, n-1)], G.adj[randint(0, n-1)])
G.printGraph()

start = timer()
connected_components(G)
end = timer()
#devo fare un array dei tempi e disegnare i grafici

