class ChainedSet:

    def __init__(self, head, tail):
        self.head = head  # corrisponde al rappresentante
        self.tail = tail  # corrisponde alla coda
        head.setPtr = self
        self.size = 1  # per l'euristica
