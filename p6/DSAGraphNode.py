import DSALinkedList as ll

class DSAGraphNode():

    def __init__(self, inLabel, inValue):
        self.label = inLabel
        self.value = inValue
        self.links = ll.DSALinkedList()
        self.visited = False

    def __str__(self):
        return ("Label: " + str(self.label) + " Value : " + str(self.value))
    
    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value
    
    def getAdjacent(self):
        return self.links.display()

    def addEdge(self, vertex):
        self.links.insertLast(vertex)

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return self.visited