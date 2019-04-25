class Node:
    def __init__(self, val=None, parent=None):
        self.root = parent
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def __ge__(self, other):
        assert type(other) == type(self)
        return self.value >= other.value

    def __le__(self, other):
        assert type(other) == type(self)
        return self.value <= other.value