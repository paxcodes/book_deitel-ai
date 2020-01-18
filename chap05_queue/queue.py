class Queue:
    # First In, First Out

    def __init__(self):
        self.theQueue = []

    def Add(self, item):
        self.theQueue.append(item)

    def Remove(self):
        item = self.theQueue[0]
        del self.theQueue[0]
        return item

    def IsEmpty(self):
        return len(self) == 0

    def Peek(self):
        return self.theQueue[0]

    def __len__(self):
        return len(self.theQueue)
