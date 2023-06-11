class DSAListNode():

    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def setValue(self, inValue):
        self.value = inValue
        
    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext
    