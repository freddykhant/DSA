## DSAQueue class implemented in Week 3 of DSA Practicals ##
# Re-implemented for DSAGraph, and keyMeUp ##
# Dependencies: DSALinkedList #

import DSALinkedList as ll

class DSAQueue():
    
    # Initialises queue class field to be an instance of DSALinkedList object 
    def __init__(self):
        self.queue = ll.DSALinkedList()
        self.count = 0

    # Makes DSAQueue an iterable object
    def __iter__(self):
        return iter(self.queue)

    # Returns queue length/count
    def length(self):
        return self.count

    # Checks if the queue is empty
    def isEmpty(self):
        if self.queue.head is None and self.queue.tail is None:
            empty = True
        else:
            empty = False
        return empty
    
    # Returns the first value in the queue
    def peek(self):
        if(self.isEmpty()):
            raise Exception("Queue underflow")
        else:
            first = self.queue.peekFirst()
        return first
    
    # Returns the last value in the queue
    def last(self):
        if(self.isEmpty()):
            raise Exception("Queue underflow")
        else:
            last = self.queue.peekLast()
        return last
    
    # Enqueue a element
    def enqueue(self, value):
        self.queue.insertLast(value)
        self.count += 1

    # Queue element at the front
    def jump(self, value):
        self.queue.insertFirst(value)
        self.count += 1

    # Dequeue an element
    def dequeue(self):
        if(self.isEmpty()):
            raise Exception("Queue underflow")
        else:
            first = self.peek()
            self.queue.removeFirst()
            self.count -= 1
        return first

    # Remove element given value
    def remove(self, value):
        if(self.isEmpty()):
            raise Exception("Queue underflow")
        else:
            removed = self.queue.removeNode(value)
            self.count -= 1
        return removed
    
    # Prints all elements in the Queue
    def display(self):
       myiter = iter(self.queue)
       value = next(myiter)
       for value in self.queue:
           print(value)