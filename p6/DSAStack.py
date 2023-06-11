import numpy as np

DEFAULT_CAPACITY = 100

class DSAStack():

    def __init__(self):
        self.stack = np.empty(DEFAULT_CAPACITY, dtype=object)
        self.count = 0
        self.size = len(self.stack)
    
    def getCount(self):
        return self.count
    
    def isEmpty(self):
        empty = (self.count == 0)
        return empty

    def isFull(self):
        full = (self.count == self.size)
        return full
    
    def top(self):
        if (self.isEmpty()):
            raise Exception("Stack underflow")
        else:
            topVal = self.stack[self.count-1]
        return topVal
    
    def push(self, value):
        if (self.isFull()):
            raise Exception("Stack overflow")
        else:
            self.stack[self.count] = value
            self.count += 1
    
    def pop(self):
        if (self.isEmpty()):
            raise Exception("Stack underflow")
        else:
            topVal = self.top()
            self.count -= 1
            return topVal

    def display(self):
        for element in range(self.count):
            print(self.stack[element])