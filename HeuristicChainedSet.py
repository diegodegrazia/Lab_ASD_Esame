from ChainedSet import *

class HeuristicChainedSet(ChainedSet):

    def __init__(self, head, tail):
        ChainedSet.__init__(self, head, tail)
        self.size = 1
