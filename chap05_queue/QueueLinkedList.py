class QueueLinkedList:

    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.size = 0


class Node:

    def __init__(self, value):
        self.value = value
        self.nextNode = None
