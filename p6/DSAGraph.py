import DSALinkedList as ll
import DSAGraphNode as node
import DSAStack as s
import DSAQueue as q

class DSAGraph():

    def __init__(self):
        self.vertices = ll.DSALinkedList()
        self.edges = ll.DSALinkedList()
    
    def addVertex(self, label, value):
        if self.hasVertex(label):
            raise Exception("Vertex " + str(label) + " already exists")
        else:
            newVertex = node.DSAGraphNode(label, value)
            self.vertices.insertLast(newVertex)

    def addEdge(self, label1, label2):
        edge = [label1, label2]
        if self.hasEdge(label1, label2):
            raise Exception("Edge " + str(label1) + " to " + str(label2) + " already exists")
        elif not self.hasVertex(label1):
            raise Exception("Vertex " + str(label1) + " does not exist")
        elif not self.hasVertex(label2):
            raise Exception("Vertex " + str(label2) + " does not exist")
        elif self.hasVertex(label1) and self.hasVertex(label2):
            self.getVertex(label1).addEdge(self.getVertex(label2))
            self.getVertex(label2).addEdge(self.getVertex(label1))
            self.edges.insertLast(edge)

    def hasVertex(self, label):
        if self.getVertex(label) in self.vertices:
            return True
        else:
            return False
        
    def hasEdge(self, label1, label2):
        if ((self.getVertex(label2) in self.getVertex(label1).links) and (self.getVertex(label1) in self.getVertex(label2).links)):
            return True
        else:
            return False

    def getVertexCount(self):
        vertexCount = 0
        for vertex in self.vertices:
            vertexCount += 1
        return vertexCount

    def getEdgeCount(self):
        edgeCount = 0
        for edge in self.edges:
            edgeCount += 1
        return edgeCount

    def getVertex(self, label):
        for vertex in self.vertices:
            if vertex.label == label:
                    return vertex

    def getAdjacent(self, label):
        if self.hasVertex(label):
            return self.getVertex(label).getAdjacent()
        else:
            raise Exception("Vertex " + str(label) + " does not exist")

    def isAdjacent(self, label1, label2):
        if self.hasVertex(label1) and self.hasVertex(label2):
            if self.hasEdge(label1, label2):
                return True
            else:
                return False
        else:
            raise Exception("Vertices " + str(label1) + str(label2) + " do not exist")

    def displayGraph(self):
        self.vertices.display()

    def displayList(self):
        for vertex in self.vertices:
            print(str(vertex) + " links: ")
            vertex.getAdjacent()
            print("\n")

    def displayMatrix(self):
        for vertex1 in self.vertices:
            for vertex2 in self.vertices:
                if vertex2 in vertex1.links:
                    print("1 ", end="")
                elif vertex2 not in vertex1.links:
                    print("0 ", end="")
            print("\n")

    def depthFirstSearch(self, label):
        T = q.DSAQueue()
        S = s.DSAStack()
        for vertex in self.vertices:
            vertex.clearVisited()
        v = self.getVertex(label)
        v.setVisited()
        S.push(v)
        while(S.isEmpty() == False):
            #w = iter(v.links)
            #while(w.getVisited() == True):
            #    next(w)
            for w in v.links:
                if(w.getVisited() == False):
                    T.enqueue(v)
                    T.enqueue(w)
                    w.setVisited()
                    S.push(w)
                    v = w
            v = S.pop()
        return T

    def breadthFirstSearch(self, label):
        T = q.DSAQueue()
        Q = q.DSAQueue()
        for vertex in self.vertices:
            vertex.clearVisited()
        v = self.getVertex(label)
        v.setVisited()
        Q.enqueue(v)
        while(Q.isEmpty() == False):
            v = Q.dequeue()
            for w in v.links:
                if(w.getVisited() == False):
                    T.enqueue(v)
                    T.enqueue(w)
                    w.setVisited()
                    Q.enqueue(w)
        return T
        
if __name__ == "__main__":
    graph = DSAGraph()
    graph.addVertex("A", 1)
    graph.addVertex("B", 2)
    graph.addVertex("C", 3)
    graph.addVertex("D", 4)
    graph.addVertex("E", 5)
    graph.addVertex("F", 6)
    graph.addVertex("G", 7)
    graph.addVertex("H", 8)
    graph.addVertex("I", 9)
    graph.addVertex("J", 10)
    graph.addEdge("A", "B")
    graph.addEdge("A", "D")
    graph.addEdge("A", "C")
    graph.addEdge("B", "E")
    graph.addEdge("D", "H")
    graph.addEdge("C", "F")
    graph.addEdge("H", "J")
    graph.addEdge("F", "I")
    graph.addEdge("G", "J")
    graph.addEdge("I", "J")
    
   
    #graph.displayGraph()
    #graph.displayList()
    #graph.displayMatrix()
    #bfs = graph.breadthFirstSearch('A')
    #bfs.display()
    dfs = graph.depthFirstSearch('A')
    dfs.display()