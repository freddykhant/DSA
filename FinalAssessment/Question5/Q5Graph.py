#
# DSA Final Assessment Question 5 - Q5Graph.py
#
# Name : Freddy Khant
# ID   : 20618166
#
# 
import numpy as np
from PracExamException import *
      
class Q5Graph():

    class Q5GraphNode():

        def __init__(self, label):
            self.label = label
            self.type = ""

        def __str__(self):
            return str(self.label)

    def __init__(self, size):
        self.maxsize = size
        self.wmatrix = np.zeros((self.maxsize,self.maxsize), dtype=int)
        self.labels = np.zeros(self.maxsize, dtype=object)
        self.count = 0

    def addVertex(self, label):
        if self.count == self.maxsize:
            raise PracExamException("graph is full")
        if not self.hasVertex(label):
            self.labels[self.count] = self.Q5GraphNode(label)
            self.count += 1

    def addEdge(self, label1, label2, weight):
        self.addVertex(label1)  # won't add if already there
        self.addVertex(label2)
        index1 = self.getIndex(label1)
        index2 = self.getIndex(label2)
        self.wmatrix[index1,index2] = weight

    def getIndex(self, label):
        index = 0
        for i in range(self.count):
            if self.labels[i].label == label:
                index = i
        return index

    def getVertex(self, label):
        for i in range(self.count):
            if self.labels[i].label == label:
                return self.labels[i]
        
    def hasVertex(self, label):
        returnVal = False
        for i in range(self.count):
            if self.labels[i].label == label:
                returnVal = True
        return returnVal

    def getVertexCount(self):
        return self.count
    
    def getEdge(self, index1, index2):
        return self.wmatrix[index1, index2]

    def hasEdge(self, index1, index2):
        hasEdge = False
        if self.getEdge(index1, index2) > 0 or self.getEdge(index2, index1) > 0:
            hasEdge = True
        return hasEdge

    def displayAsList(self):
        for i in range(self.count):
            print(self.labels[i])

    def displayAsMatrix(self):
        for w1 in self.wmatrix:
            for w2 in w1:
                print(w2, end=" ")
            print("\n")

    def displayMovies(self):
        for i in range(self.count):
            if self.labels[i].type == "M":
                print(self.labels[i])

    def displayActors(self):
        for i in range(self.count):
            if self.labels[i].type == "A":
                print(self.labels[i])

    def displayRoles(self):
        for i in range(self.count):
            if self.labels[i].type == "R":
                print(self.labels[i])

    def displayActorsMovies(self, name):
        idx = self.getIndex(name)
        for i in range(self.count):
            if self.labels[i].type == "M":
                if self.hasEdge(i, idx):
                    print("\t" + str(self.labels[i]))

    def displayMovieActors(self, name):
        idx = self.getIndex(name)
        for i in range(self.count):
            if self.labels[i].type == "A":
                if self.hasEdge(idx, i):
                    print("\t" + str(self.labels[i]))

    def displayCoStars(self, name):
        actorIdx = self.getIndex(name)
        print("Costars for " + self.labels[actorIdx].label + "\n")
        for i in range(self.count):
            if self.labels[i].type == "M":
                if self.hasEdge(i, actorIdx):
                    print(self.labels[i])
                    self.displayMovieActors(self.labels[i].label)


    def readFile(self, filename):
        try:
            file = open(filename)
            file.readline()
            line = file.readline()
            while line:
                self.processLine(line)
                line = file.readline()
            file.close()
        except IOError as e:
            print("Error in file processing: " + str(e))

    def processLine(self, row):
        edges = row.split(",")
        label1 = edges[0]
        label2 = edges[3]
        self.addEdge(label1, label2, 1)
        self.getVertex(label1).type = "M"
        self.getVertex(label2).type = "A"