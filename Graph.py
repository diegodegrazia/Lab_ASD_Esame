from SetElement import *

class Graph:
    def __init__(self, nVertices):
        self.V = nVertices #numero vertici
        self.adj = [] #vettore di adiacenza inizializzato a vuoto
        for i in range(nVertices): #Nel vettore inserisco i nodi "SetElement" e li faccio puntare a liste con nodi adiacenti
            self.adj.append(SetElement(i))
            self.adj[i].nextPtr = []

    def edgeInsert(self, u, v): #Doppio inserimento perchè il grafo non è diretto
        self.adj[u].nextPtr.append(v)
        self.adj[v].nextPtr.append(u)

    def printGraph(self):
        for i in self.adj:
            print("Vertices adjacent to vertex ", i.value, ": ", i.nextPtr)
