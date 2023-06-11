# DSAQueue class implemented in Week 3, re-developed to use linked-lists #

import numpy as np
import DSALinkedList as ll

class DSAQueue():
    
    def __init__(self):
        self.queue = ll.DSALinkedList()

    def __iter__(self):
        return iter(self.queue)

    def isEmpty(self):
        empty = (self.queue.head == self.queue.tail == None)
        return empty
    
    def peek(self):
        if(self.queue.isEmpty()):
            raise Exception("Queue underflow")
        else:
            first = self.queue.peekFirst()
        return first
    
    def enqueue(self, value):
        self.queue.insertLast(value)

    def dequeue(self):
        if(self.queue.isEmpty()):
            raise Exception("Queue underflow")
        else:
            first = self.peek()
            self.queue.removeFirst()
        return first
    
    def display(self):
       myiter = iter(self.queue)
       value = next(myiter)
       for value in self.queue:
           print(value)
