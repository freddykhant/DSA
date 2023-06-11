# DSAStack class implemented in Week 3, re-developed to use linked-lists #

import numpy as np
import DSALinkedList as ll

class DSAStack():

    def __init__(self):
        self.stack = ll.DSALinkedList()
    
    def __iter__(self):
        return iter(self.stack)

    def top(self):
        if(self.stack.isEmpty()):
            raise Exception("Stack underflow")
        else:
            top = self.stack.peekFirst()
        return top
    
    def push(self, value):
        self.stack.insertFirst(value)
    
    def pop(self):
        if(self.stack.isEmpty()):
            raise Exception("Stack underflow")
        else:
            top = self.top()
            self.stack.removeFirst()
        return top

    def display(self):
       myiter = iter(self.stack)
       value = next(myiter)
       for value in self.stack:
           print(value)

if __name__ == "__main__":
    stack = DSAStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()