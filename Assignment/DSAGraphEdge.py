## DSAGraph Edge Class implemented for DSA Assignment 1 ##
# No dependencies, DSAGraph aggregates DSAGraphEdge ##

class DSAGraphEdge():

    # Constructor taking fromVertex and toVertex as arguments, label is the combination of to and from, weight is initially 1
    def __init__(self, fromVertex, toVertex):
        self.fro = fromVertex
        self.to = toVertex
        self.label = self.fro.label + self.to.label

    # Returns string representation of edge object
    def __str__(self):
        return ("From " + str(self.fro) + " to " + str(self.to))
    
    # Returns label
    def getLabel(self):
        return self.label

    # Sets label
    def setLabel(self, newFrom, newTo):
        self.label = newFrom + newTo

    # Returns from vertex
    def getFrom(self):
        return self.fro

    # Returns to vertex
    def getTo(self):
        return self.to

    # Sets from vertex
    def setFrom(self, newFrom):
        self.fro = newFrom

    # Sets to vertex
    def setTo(self, newTo):
        self.to = newTo