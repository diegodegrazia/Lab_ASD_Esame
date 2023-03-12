from ChainedSet import *

class SetElement:

    def __init__(self, value):
        self.value = value
        self.nextPtr = None
        self.setPtr = None

    def make_set(self):
        a = ChainedSet(self, self)
        return a

    def find_set(self):
        return self.setPtr.head