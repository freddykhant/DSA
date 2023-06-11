import DSALinkedList as ll
import DSAGraphVertex as vertex
import DSAGraphEdge as edge
import DSAStack as s
import DSAQueue as q

## DSAGraph Class implemented in Week 6 of DSA Practicals ##
## Utilised for keyMeUp class ##
## Dependencies: DSALinkedList, DSAGraphVertex, DSAGraphEdge, DSAStack, DSAQueue ##

class DSAGraph():

    # Constructor initialising list of vertices and edges as an instance of linked list ##
    def __init__(self):
        self.vertices = ll.DSALinkedList()
        self.edges = ll.DSALinkedList()
    
    # Adds vertex given a label #
    def addVertex(self, label):
        if self.hasVertex(label): # If the vertex already exists: error #
            raise Exception("Vertex " + str(label) + " already exists")
        else: # else if vertex doesn't exist
            newVertex = vertex.DSAGraphVertex(label) # Create new vertex object
            self.vertices.insertLast(newVertex) # Add vertex vertices list
            return newVertex

    # Adds edge given two labels, to and from
    def addEdge(self, label1, label2):
        if self.hasEdge(label1+label2): # If edge already exists, error
            raise Exception("Edge " + str(label1) + " to " + str(label2) + " already exists")
        elif self.hasEdge(label2+label1): # Check inverse label
            raise Exception("Edge " + str(label2) + " to " + str(label1) + " already exists")
        else: # Else if edge doesn't already exist
            # If verticies with given labels doesn't already exist: error
            if not self.hasVertex(label1):
                raise Exception("Vertex " + str(label1) + " does not exist")
            elif not self.hasVertex(label2):
                raise Exception("Vertex " + str(label2) + " does not exist")
                # If verticies exist, add edges, add edges to edges list
            elif self.hasVertex(label1) and self.hasVertex(label2):
                self.getVertex(label1).addEdge(self.getVertex(label2))
                self.getVertex(label2).addEdge(self.getVertex(label1))
                newEdge = edge.DSAGraphEdge(self.getVertex(label1), self.getVertex(label2))
                self.edges.insertLast(newEdge)
                return newEdge

    # Delete a vertex given the label
    def delVertex(self, label):
        if self.hasVertex(label):
            v = self.getVertex(label)
            self.vertices.removeNode(v)
            for vertex in self.vertices:
                if v in vertex.links:
                    vertex.links.removeNode(v)
            return v
        else:
            raise Exception("Vertex: " + str(label) + "does not exist")

    # Delete an edge given the to and from labels
    def delEdge(self, label1, label2):
        if self.hasEdge(label1+label2):
            delEdge = self.edges.removeNode(self.getEdge(label1+label2))
            return delEdge
        else:
            raise Exception("Edge: " + str(label1+label2) + "does not exist")

    # Deletes vertices from eachother's adjacency list given the two vertice's labels
    def delAdjacent(self, label1, label2):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        v1.links.removeNode(v2)
        v2.links.removeNode(v1)
            
    # Checks if vertex with given label exists
    def hasVertex(self, label):
        # If vertex is in list of vertices, return true, else return false
        if self.getVertex(label) in self.vertices:
            return True
        else:
            return False
    
    # Checks if edge with given label exists
    def hasEdge(self, label):
        # If edge is in list of edges, return true, else return false
        if self.getEdge(label) in self.edges:
            return True
        else:
            return False

    # Iteratively counts verticies and returns count
    def getVertexCount(self):
        vertexCount = 0
        for vertex in self.vertices:
            vertexCount += 1
        return vertexCount

    # Iteratively counts edges and returns count
    def getEdgeCount(self):
        edgeCount = 0
        for edge in self.edges:
            edgeCount += 1
        return edgeCount

    # Returns vertex given a label
    def getVertex(self, label):
        for vertex in self.vertices:
            if vertex.label == label:
                    return vertex

    # Returns edge given a label
    def getEdge(self, label):
        for edge in self.edges:
            if edge.getLabel() == label:
                return edge

    # Displays list of adjacent vertices given a label of a specific vertex
    def getAdjacent(self, label):
        if self.hasVertex(label):
            return self.getVertex(label).getAdjacent()
        else:
            raise Exception("Vertex " + str(label) + " does not exist")

    # Returns true or false depending on if a vertex is adjacent to another vertex
    def isAdjacent(self, label1, label2):
        if self.hasVertex(label1) and self.hasVertex(label2):
            if self.hasEdge(label1+label2) or self.hasEdge(label2+label1):
                return True
            else:
                return False
        else:
            raise Exception("Vertices " + str(label1) + str(label2) + " do not exist")

    # Displays all verticies in graph
    def displayGraph(self):
        self.vertices.display()
    
    # Displays all edges in graph
    def displayEdges(self):
        self.edges.display()

    # Displays graph's adjacency list
    def displayList(self):
        for vertex in self.vertices:
            print(str(vertex) + " links: ")
            vertex.getAdjacent()
            print("\n")

    # Displays graph's adjacency matrix
    def displayMatrix(self):
        for vertex1 in self.vertices:
            for vertex2 in self.vertices:
                if vertex2 in vertex1.links:
                    print("1 ", end="")
                elif vertex2 not in vertex1.links:
                    print("0 ", end="")
            print("\n")

    # Performs a depth first search, returns dfs queue
    def depthFirstSearch(self, label):
        T = q.DSAQueue() # Creates dfs queue
        S = s.DSAStack() # Creates stack for keeping track of v
        # Sets all vertices as unvisited
        for vertex in self.vertices:
            vertex.clearVisited()
        # Initialises starting vertex
        v = self.getVertex(label)
        v.setVisited()
        # Push v onto stack
        S.push(v)
        # While stack is not empty
        while(S.isEmpty() == False):
            # Loop through the adjacency list of v
            for w in v.links:
                # If given adjacent vertex is unvisited
                if(w.getVisited() == False):
                    T.enqueue(v) # Enqueue v
                    T.enqueue(w) # Enqueue adjacent vertex w
                    w.setVisited() # Set adjacent vertex as visited
                    S.push(w) # Push adjacent vertex onto stack
                    v = w # Set v as the adjacent vertex
            v = S.pop() # Set v as the top element in stack and pop the element
        return T # Return dfs queue

    # Performs a breadth first search, returns bfs queue
    def breadthFirstSearch(self, label):
        T = q.DSAQueue() # Creates queue for keeping track of v
        Q = q.DSAQueue() # Creates bfs queue
        # Sets all vertices as unvisited
        for vertex in self.vertices:
            vertex.clearVisited()
        # Initialises starting vertex
        v = self.getVertex(label)
        v.setVisited() 
        Q.enqueue(v) # Enqueues v
        while(Q.isEmpty() == False): # While queue is not empty
            v = Q.dequeue() # v is the first element in Q
            for w in v.links: # Loop through the adjacency list of v 
                if(w.getVisited() == False): # If the adjacent matrix is unvisited
                    T.enqueue(v) # Enqueue v onto bfs queue
                    T.enqueue(w) # Enqueue w onto bfs queue
                    w.setVisited() # Set adjacent vertex as unvisited
                    Q.enqueue(w) # Enqueue adjacent vertex onto Q
        return T # Returns bfs queue
