from Node import *

class Graph:
    def __init__(self, nVertices):
        self.V = nVertices #numero vertici
        self.adj = [] #vettore di adiacenza inizializzato a vuoto
        for i in range(nVertices): #Nel vettore inserisco i nodi "SetElement" e li faccio puntare a liste con nodi adiacenti
            self.adj.append(Node(i))
            self.adj[i].listPtr = []

    def edgeInsert(self, u, v): #Doppio inserimento perchè il grafo non è diretto
        self.adj[u.value].listPtr.append(v) #non c'è controllo sull'esistenza dell'arco
        self.adj[v.value].listPtr.append(u)

    def printGraph(self):
        for i in self.adj:
            print("Vertices adjacent to vertex ", i.value, ": ")
            for j in i.listPtr:
                print(j.value, "")
