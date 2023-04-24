from ChainedNode import *
from TreeNode import *


class Graph:
    def __init__(self, nVertices, nodeType):
        self.G = {}
        self.type = nodeType
        self.V = nVertices  # numero vertici
        for i in range(nVertices):  # inizializzo grafo con nodi e liste di adiacenza vuote
            if nodeType == "TreeNode":
                self.G[TreeNode(i)] = []
            elif nodeType == "ChainedNode":
                self.G[ChainedNode(i)] = []

    def edgeInsert(self, u, v):  # Doppio inserimento perchè il grafo non è diretto
        if not self.edgeCheck(u, v) and u != v:
            self.G[u].append(v)
            self.G[v].append(u)

    def edgeCheck(self, u, v):
        for i in self.G[u]:
            if i == v:
                return True
        return False

    def printGraph(self):
        for i in self.G:
            print_string = ""
            for j in self.G[i]:
                print_string += "-> " + str(j.value)
            print("Vertices adjacent to vertex ", i.value, ": ", print_string)

    def heuristicUnion(self, x, y):
        if x.setPtr.size < y.setPtr.size:
            self.chainedUnion(y, x)  # accodo l'insieme di x a quello di y
        else:
            self.chainedUnion(x, y)  # accodo l'insieme di y a quello di x

    def union(self, x, y):  # accodo l'insieme di y a quello di x
        if self.type == "ChainedNode":
            self.chainedUnion(x, y)
        elif self.type == "TreeNode":
            self.treeUnion(x, y)

    def chainedUnion(self, x, y):
        if x.setPtr is None:
            x.makeSet()
        if y.setPtr is None:
            y.makeSet()
        tmp = y.findSet()  # primo elemento della lista che sposterò
        app = x.findSet()
        x.setPtr.size += y.setPtr.size  # attributo size aggiornato
        while app.nextPtr is not None:
            app = app.nextPtr
        app.nextPtr = tmp  # collego l'ultimo elemento della lista di x con il primo della lista di y
        while tmp is not None:  # scorro la lista di y per aggiornare i setPtr
            tmp.setPtr = x.setPtr
            tmp = tmp.nextPtr

    def treeUnion(self, x, y):
        tmp = y.findSet()
        tmp.p = x.findSet()
