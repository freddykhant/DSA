import DSALinkedList as ll

## DSAGraph Vertex Class implemented in Week 6 of DSA Practicals ##
# Dependencies: DSALinkedList #

class DSAGraphVertex():

    # Constructor: imports label, links as linked list object, initial visited as False
    def __init__(self, inLabel):
        self.label = inLabel
        self.links = ll.DSALinkedList()
        self.visited = False

    # Returns string representation of vertex object
    def __str__(self):
        return ("Label: " + str(self.label))
    
    # returns label
    def getLabel(self):
        return self.label

    # sets label 
    def setLabel(self, newLabel):
        self.label = newLabel
    
    # displays list of adjacent vertices
    def getAdjacent(self):
        return self.links.display()

    # adds vertex to adjacency list
    def addEdge(self, vertex):
        self.links.insertLast(vertex)

    # sets vertex as visited
    def setVisited(self):
        self.visited = True

    # sets vertex as unvisited
    def clearVisited(self):
        self.visited = False

    # returns if vertex is visited
    def getVisited(self):
        return self.visited