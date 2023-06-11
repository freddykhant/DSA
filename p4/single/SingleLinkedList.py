import DSAListNode as node

class DSALinkedList():

    def __init__(self):
        self.head = None

    def isEmpty(self):
        empty = (self.head == None)
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
            currNd = self.head
            while(currNd.getNext() != None):
                currNd = currNd.getNext()
            nodeValue = currNd.getValue()
        return nodeValue

    def insertFirst(self, newValue):
        newNd = node.DSAListNode(newValue)
        if(self.isEmpty()):
            self.head = newNd
        else:
            newNd.setNext(self.head)
            self.head = newNd
    
    def insertLast(self, newValue):
        newNd = node.DSAListNode(newValue)
        if(self.isEmpty()):
            self.head = newNd
        else:
            currNd = self.head
            while(currNd.getNext() != None):
                currNd = currNd.getNext()
            currNd.setNext(newNd)
    
    def removeFirst(self):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
        return nodeValue
    
    def removeLast(self):
        if(self.isEmpty()):
            raise Exception("Linked list empty")
        elif(self.head.getNext() == None):
            nodeValue = self.head.getValue()
            self.head = None
        else:
            prevNd = None
            currNd = self.head
            while(currNd.getNext() != None):
                prevNd = currNd
                currNd = currNd.getNext()
            prevNd.setNext(None)
            nodeValue = currNd.getValue()
        return nodeValue