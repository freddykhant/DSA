import DSAListNode as node

## DSALinkedList implemented in Week 4 of DSA Practicals, reimplemented for DSAGraph ##
## Dependencies: DSAListNode ##

class DSALinkedList():

    # Initializes two fields, head and tail as None
    def __init__(self):
        self.head = None
        self.tail = None

    # Makes linked list an iterable object
    def __iter__(self):
        currNd = self.head
        while(currNd != None):
            yield currNd.value
            currNd = currNd.getNext()

    # Checks if the linked list is empty
    def isEmpty(self):
        empty = (self.head == self.tail == None)
        return empty

    # Returns the first value of the linked list
    def peekFirst(self):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        else:
            first = self.head.getValue()
        return first
    
    # Returns the last value of the linked list
    def peekLast(self):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        else:
            last = self.tail.getValue()
        return last

    # Returns a node given the value
    def peekNode(self, value):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        else:
            currNd = self.head
            while(currNd.getValue() != value):
                currNd = currNd.getNext()
        return currNd

    # Inserts a value into the first position
    def insertFirst(self, newValue):
        newNd = node.DSAListNode(newValue) # Creates new list node object
        if(self.isEmpty()): # If list is empty:
            # List head and tail is the new node
            self.head = newNd 
            self.tail = newNd
        else:
            newNd.setNext(self.head) # current head is now new node's next value
            self.head.setPrev(newNd) # current head's previous value is now the new node
            self.head = newNd # new head is now the new node
    
    # Inserts a value into the last position
    def insertLast(self, newValue):
        newNd = node.DSAListNode(newValue) # Creates new list node object
        if(self.isEmpty()): # If list is empty
            # List head and tail is the new node
            self.head = newNd 
            self.tail = newNd
        else:
            self.tail.setNext(newNd) # current tail's next value is now the new node
            newNd.setPrev(self.tail) # new node's previous value is now the current tail
            self.tail = newNd # new tail is now the new node
    
    # Removes the first value
    def removeFirst(self):
        # If the list is empty, raise error
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        elif(self.head.getNext() == None): # If the current's next value is none
            nodeValue = self.head.getValue() # first value is head's value
            # head and tail is none
            self.head = None
            self.tail = None
        else:
            nodeValue = self.head.getValue() # node value is head's value
            self.head = self.head.getNext() # head is shifted down, new head is previous head's next
        return nodeValue # return first value

    # Removes the last value
    def removeLast(self):
        if(self.isEmpty()):
            # If the list is empty, raise error
            raise Exception("Linked list empty")
        elif(self.head.getNext() == None): # If head's next is none
            nodeValue = self.tail.getValue() # last value is tail's value
            # head and tail are none
            self.head = None
            self.tail = None
        else:
            nodeValue = self.tail.getValue() # last value is tail's value
            self.tail = self.tail.getPrev() # tail is shifted up, current tail's previous
            self.tail.setNext(None) # new tail's next is none
        return nodeValue # return last value


    def removeNode(self, value):
        currNd = self.peekNode(value)
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        elif(currNd == self.head):
            nodeValue = self.removeFirst()
        elif(currNd == self.tail):
            nodeValue = self.removeLast()
        else:
            currNd.getPrev().setNext(currNd.getNext())
            currNd.getNext().setPrev(currNd.getPrev())
            nodeValue = currNd.getValue()
        return nodeValue

    # Prints contents of the linked list
    def display(self):
        for node in self:
            print(node)