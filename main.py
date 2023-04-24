from Graph import *
from random import *
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import gc


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


def heuristicConnectedComponents(graph):
    for v in graph.G:
        v.makeSet()
    for i in graph.G:
        for j in graph.G[i]:
            if i.findSet() != j.findSet():
                graph.heuristicUnion(i, j)


executionTimeMyGraph = []
executionTimeMyGraphH = []
executionTimeMyGraph_2 = []
x = []

for i in range(1, 600):
    myGraph = Graph(i, "ChainedNode")  # concatenato senza euristica
    myGraphH = Graph(i, "ChainedNode")  # concatenato con euristica
    myGraph_2 = Graph(i, "TreeNode")  # foresta con compressione

    for j in range(int(i * (i - 1) / 2)):
        myGraph.edgeInsert(list(myGraph.G.keys())[randint(0, i - 1)], list(myGraph.G.keys())[randint(0, i - 1)])
        myGraphH.edgeInsert(list(myGraphH.G.keys())[randint(0, i - 1)], list(myGraphH.G.keys())[randint(0, i - 1)])
        myGraph_2.edgeInsert(list(myGraph_2.G.keys())[randint(0, i - 1)], list(myGraph_2.G.keys())[randint(0, i - 1)])
    start_1 = timer()  # per myGraph
    connectedComponents(myGraph)
    end_1 = timer()
    startH = timer()  # per myGraphH
    heuristicConnectedComponents(myGraphH)
    endH = timer()
    start_2 = timer()  # per myGraph_2
    connectedComponents(myGraph_2)
    end_2 = timer()
    executionTimeMyGraph.append(end_1 - start_1)  # lista con tempi di esecuzione, per ogni iterazione, di connectedComponents (concatenato)
    executionTimeMyGraphH.append(endH - startH)  # lista con tempi di esecuzione, per ogni iterazione, di heuristicConnectedComponents (concatenato)
    executionTimeMyGraph_2.append(end_2 - start_2)  # lista con tempi di esecuzione, per ogni iterazione, di ConnectedComponents (foresta con compressione)
    x.append(i)
    gc.collect()

plt.plot(x, executionTimeMyGraph)
plt.plot(x, executionTimeMyGraphH)
plt.plot(x, executionTimeMyGraph_2)
plt.xlabel("Numero di vertici")
plt.ylabel("Tempo di esecuzione")
plt.title("Andamento asintotico")
plt.legend(["Componenti connesse con liste", "Componenti connesse con liste ed euristica UP", "Componenti connesse con foresta ed euristica CC"])
plt.show()
