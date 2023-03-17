from SetElement import SetElement

class Node(SetElement):
    def __init__(self, value):
        SetElement.__init__(self, value)
        self.listPtr = None
