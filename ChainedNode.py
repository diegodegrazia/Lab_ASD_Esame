from ChainedSet import *
from Node import *

class ChainedNode(Node):
    def __init__(self, value):
        Node.__init__(self, value)
        self.nextPtr = None
        self.setPtr = None

    def makeSet(self):
        a = ChainedSet(self, self)
        return a

    def findSet(self):
        return self.setPtr.head
