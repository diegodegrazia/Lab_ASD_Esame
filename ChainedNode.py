from ChainedSet import *
from Node import *

class ChainedNode(Node):
    def __init__(self, value):
        Node.__init__(self, value)
        self.nextPtr = None
        self.setPtr = None

    def makeSet(self):
        ChainedSet(self, self)

    def findSet(self):
        return self.setPtr.head
