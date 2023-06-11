import DSAListNode as node

class DSALinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNd = self.head
        while(currNd != None):
            yield currNd.value
            currNd = currNd.getNext()

    def isEmpty(self):
        empty = (self.head == self.tail == None)
        return empty

    def peekFirst(self):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        else:
            first = self.head.getValue()
        return first
    
    def peekLast(self):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        else:
            last = self.tail.getValue()
        return last

    def insertFirst(self, newValue):
        newNd = node.DSAListNode(newValue)
        if(self.isEmpty()):
            self.head = newNd
            self.tail = newNd
        else:
            newNd.setNext(self.head)
            self.head.setPrev(newNd)
            self.head = newNd
    
    def insertLast(self, newValue):
        newNd = node.DSAListNode(newValue)
        if(self.isEmpty()):
            self.head = newNd
            self.tail = newNd
        else:
            self.tail.setNext(newNd)
            newNd.setPrev(self.tail)
            self.tail = newNd
    
    def removeFirst(self):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        elif(self.head.getNext() == None):
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
        return nodeValue
    
    def removeLast(self):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        elif(self.head.getNext() == None):
            nodeValue = self.tail.getValue()
            self.head = None
            self.tail = None
        else:
            nodeValue = self.tail.getValue()
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
        return nodeValue

    def display(self):
        for node in self:
            print(node)