import numpy as np

## DSAStack class implemented in Week 3 of DSA Practicals ##
# Re-implemented for DSAGraph ##
# Dependencies: numpy module #

DEFAULT_CAPACITY = 100 # Sets default capacity to be a constant value of 100

class DSAStack():

    # Initialises stack object to be an empty numpy  object array of size 100, count initially 0, size is length of the stack object
    def __init__(self):
        self.stack = np.empty(DEFAULT_CAPACITY, dtype=object)
        self.count = 0
        self.size = len(self.stack)
    
    # Returns stack count
    def getCount(self):
        return self.count
    
    # Checks if stack is empty
    def isEmpty(self):
        empty = (self.count == 0)
        return empty

    # Checks if stack is full
    def isFull(self):
        full = (self.count == self.size)
        return full
    
    # Returns element at the top of the stack
    def top(self):
        if (self.isEmpty()):
            raise Exception("Stack underflow")
        else:
            topVal = self.stack[self.count-1]
        return topVal
    
    # Pushes an element onto the top of the stack
    def push(self, value):
        # Raise exception if stack is full
        if (self.isFull()):
            raise Exception("Stack overflow")
        else:
            # Push element onto stack and increase stack count by 1
            self.stack[self.count] = value
            self.count += 1
    
    # Pops the top value of the stack and returns it
    def pop(self):
        # Raise exception if stack is empty
        if (self.isEmpty()):
            raise Exception("Stack underflow")
        else:
            # get top value, decrease count by 1, return top value
            topVal = self.top()
            self.count -= 1
            return topVal

    # Prints all elements in the stack
    def display(self):
        for element in range(self.count):
            print(self.stack[element])