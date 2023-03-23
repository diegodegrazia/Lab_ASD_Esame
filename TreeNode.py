from Node import *

class TreeNode(Node):
    def __init__(self, value):
        Node.__init__(self, value)
        self.p = None  # "puntatore" al padre

    def makeSet(self):
        self.p = self

    def findSet(self):
        if self != self.p:
            self.p = self.p.findSet()
        return self.p