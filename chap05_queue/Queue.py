class Queue:
    # First In, First Out

    def __init__(self):
        self.theQueue = []

    def Add(self, item):
        self.theQueue.append(item)

    def Remove(self):
        """
        Retrieves the value of the next item in the queue
        without removing it from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        item = self.theQueue[0]
        del self.theQueue[0]
        return item

    def IsEmpty(self):
        return len(self) == 0

    def Peek(self):
        """
        Retrieves the value of the next item in the queue
        without removing it from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        return self.theQueue[0]

    def __len__(self):
        return len(self.theQueue)
