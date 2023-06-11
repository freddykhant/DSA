## DSAListNode Class implemented in Week 4 of DSA Practicals ##
# Re-implemented for keyMeUp #

class DSAListNode():

    # Initialises class fields, value is based on input, next and prev are initially none
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # Returns value
    def getValue(self):
        return self.value

    # Sets value
    def setValue(self, inValue):
        self.value = inValue
    
    # Returns next node
    def getNext(self):
        return self.next

    # Sets next node
    def setNext(self, newNext):
        self.next = newNext
    
    # Returns previous node
    def getPrev(self):
        return self.prev
    
    # Sets previous node
    def setPrev(self, newPrev):
        self.prev = newPrev