from Graph import *
from random import *
import matplotlib.pyplot as plt
from timeit import default_timer as timer

def connectedComponents(graph):
    for v in graph.G:
        v.makeSet()
    for i in graph.G:
        for j in graph.G[i]:
            if i.findSet() != j.findSet():
                graph.union(i, j)


def sameComponents(u, v):
    if u.findSet() == v.findSet():
        return True
    else:
        return False


n = 10

myGraph = Graph(n, "ChainedNode")
myGraph_2 = Graph(n, "TreeNode")


"""for i in range(0, randint(0, int(n * (n - 1) / 2))):  # randomizzo numero degli archi (da 0 a nMax = n*(n-1)/2)
    G.edgeInsert(G.adj[randint(0, n - 1)], G.adj[randint(0, n - 1)])
G.printGraph()

start = timer()
connectedComponents(G)
end = timer()
executionTime = end - start"""
# devo fare un array dei tempi e disegnare i grafici

myGraph.edgeInsert(list(myGraph.G.keys())[0], list(myGraph.G.keys())[5])
myGraph.edgeInsert(list(myGraph.G.keys())[4], list(myGraph.G.keys())[5])
myGraph.edgeInsert(list(myGraph.G.keys())[1], list(myGraph.G.keys())[7])
myGraph.edgeInsert(list(myGraph.G.keys())[4], list(myGraph.G.keys())[9])
myGraph.edgeInsert(list(myGraph.G.keys())[1], list(myGraph.G.keys())[0])
myGraph.edgeInsert(list(myGraph.G.keys())[6], list(myGraph.G.keys())[8])
myGraph.edgeInsert(list(myGraph.G.keys())[9], list(myGraph.G.keys())[8])
myGraph.edgeInsert(list(myGraph.G.keys())[4], list(myGraph.G.keys())[6])
myGraph.printGraph()
connectedComponents(myGraph)
print("-------------------------------------------------------------")
print(sameComponents(list(myGraph.G.keys())[2], list(myGraph.G.keys())[1]))
print(sameComponents(list(myGraph.G.keys())[2], list(myGraph.G.keys())[9]))
print(sameComponents(list(myGraph.G.keys())[0], list(myGraph.G.keys())[1]))
print(sameComponents(list(myGraph.G.keys())[9], list(myGraph.G.keys())[8]))
print(sameComponents(list(myGraph.G.keys())[6], list(myGraph.G.keys())[4]))
print(sameComponents(list(myGraph.G.keys())[2], list(myGraph.G.keys())[5]))
print(sameComponents(list(myGraph.G.keys())[7], list(myGraph.G.keys())[3]))
print(sameComponents(list(myGraph.G.keys())[3], list(myGraph.G.keys())[2]))

myGraph_2.edgeInsert(list(myGraph_2.G.keys())[0], list(myGraph_2.G.keys())[5])
myGraph_2.edgeInsert(list(myGraph_2.G.keys())[4], list(myGraph_2.G.keys())[5])
myGraph_2.edgeInsert(list(myGraph_2.G.keys())[1], list(myGraph_2.G.keys())[7])
myGraph_2.edgeInsert(list(myGraph_2.G.keys())[4], list(myGraph_2.G.keys())[9])
myGraph_2.edgeInsert(list(myGraph_2.G.keys())[1], list(myGraph_2.G.keys())[0])
myGraph_2.edgeInsert(list(myGraph_2.G.keys())[6], list(myGraph_2.G.keys())[8])
myGraph_2.edgeInsert(list(myGraph_2.G.keys())[9], list(myGraph_2.G.keys())[8])
myGraph_2.edgeInsert(list(myGraph_2.G.keys())[4], list(myGraph_2.G.keys())[6])
myGraph_2.printGraph()
connectedComponents(myGraph_2)
print("-------------------------------------------------------------")
print(sameComponents(list(myGraph_2.G.keys())[2], list(myGraph_2.G.keys())[1]))
print(sameComponents(list(myGraph_2.G.keys())[2], list(myGraph_2.G.keys())[9]))
print(sameComponents(list(myGraph_2.G.keys())[0], list(myGraph_2.G.keys())[1]))
print(sameComponents(list(myGraph_2.G.keys())[9], list(myGraph_2.G.keys())[8]))
print(sameComponents(list(myGraph_2.G.keys())[6], list(myGraph_2.G.keys())[4]))
print(sameComponents(list(myGraph_2.G.keys())[2], list(myGraph_2.G.keys())[5]))
print(sameComponents(list(myGraph_2.G.keys())[7], list(myGraph_2.G.keys())[3]))
print(sameComponents(list(myGraph_2.G.keys())[3], list(myGraph_2.G.keys())[2]))