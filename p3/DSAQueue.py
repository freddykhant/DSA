import numpy as np

DEFAULT_CAPACITY = 100

class DSAQueue():
    def __init__(self):
        self.queue = np.empty(DEFAULT_CAPACITY, dtype= object)
        self.front = 0
        self.rear = 0
        self.count = 0
        self.size = len(self.queue)

    def getCount(self):
        return self.count

    def isEmpty(self):
        empty = (self.count == 0)
        return empty
    
    def isFull(self):
        full = (self.count == self.size)
        return full
    
    def peek(self):
        if(self.isEmpty()):
            raise Exception("Queue underflow")
        else:
            first = self.queue[self.front]
            return first

class shufflingQueue(DSAQueue):
    def __init__(self):
        super().__init__()
    
    def enqueue(self, value):
        if (self.isFull()):
            raise Exception("Queue overflow")
        else:
            self.queue[self.rear] = value
            self.rear += 1
            self.count += 1

    def dequeue(self):
        if (self.isEmpty()):
            raise Exception("Queue underflow")
        else:
            self.front += 1
            self.count -= 1

class circularQueue(DSAQueue):
    def __init__(self):
        super().__init__()
    
    def enqueue(self, value):
        if (self.isFull()):
            self.count -= 1
        self.queue[self.rear] = value
        self.count += 1
        self.rear = ((self.rear+1) % self.size)

    def dequeue(self):
        if (self.isEmpty()):
            raise Exception("Queue underflow")
        else:
            self.count -= 1
            self.front = ((self.front+1) % self.size)
