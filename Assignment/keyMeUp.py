import DSAGraph as graph
import DSAQueue as queue
import keyMeUpMenu as menu
import sys

## keyMeUp Class for DSA Assignment 1 ##
# Student: Freddy Khant, 20618166 #
# Dependencies: DSAGraph, DSAQueue, keyMeUpMenu, sys module #

class keyMeUp():

    # Initialises keys as a DSAGraph object #
    def __init__(self):
        self.keys = graph.DSAGraph()

    # Loads a keyboard file
    def loadKeyboard(self, filename):
        try:
            file = open(filename) # Opens file
            line = file.readline() # Reads one line
            while line: # While not EOF
                line = line.strip('\n') # Strip newline token
                self.processLine(line) # Process each line, creating keyboard
                line = file.readline() # Read next line
            file.close() # Close file
        except IOError as e: # Raise IOError if invalid filename is given
            print("Error in file processing: " + str(e))

    # Processes each row and creates corresponding keyboard(graph)
    def processLine(self, row):
        # Splits the space to process characters
        edge = row.split(" ")
        key1 = edge[0] # First element = first key
        key2 = edge[1] # Second element = second key
        try:
            if not self.keys.hasVertex(key1): # If the key doesn't already exist: add Key
                self.addKey(key1)
            if not self.keys.hasVertex(key2):
                self.addKey(key2)
            self.keys.addEdge(key1, key2)
        except:
            # Raise TypeError if otherwise
            raise TypeError("Row had invalid format")

    # Loads a string file
    def loadStrings(self, filename):
        # Opens file and returns a list of strings from the file 
        try:
            with open(filename) as file:
                lines = [line.rstrip() for line in file]
            return lines
        except IOError as e:
            print("Error in file processing: " + str(e))

    # Gets size of graph
    def getSize(self):
        return self.keys.getVertexCount()

    # Gets a key given the label
    def getKey(self, label):
        return self.keys.getVertex(label)

    # Gets an edge given the label
    def getEdge(self, label):
        return self.keys.getEdge(label)

    # Adds a key given a label
    def addKey(self, label):
        return self.keys.addVertex(label)

    # Adds an edge given a label
    def addEdge(self, label1, label2):
        return self.keys.addEdge(label1, label2)

    # Deletes a key given a label
    def deleteKey(self, label):
        return self.keys.delVertex(label)

    # Deletes an edge given the to and from labels
    def deleteEdge(self, label1, label2):
        self.keys.delAdjacent(label1, label2)
        return self.keys.delEdge(label1, label2)

    # Updates a key with a new label
    def updateKey(self, label1, label2):
        if not self.keys.hasVertex(label2):
            self.getKey(label1).setLabel(label2)
            return self.getKey(label2)
        else:
            raise Exception("Key: " + str(label2) + " already exists")

    # Updates an edge given old and new to and from labels
    def updateEdge(self, label1, label2, label3, label4): 
        if not self.keys.hasEdge(label1+label2) and not self.keys.hasEdge(label2+label1):
            raise Exception("Edge: " + str(label1+label2) + " does not exist")
        elif self.keys.hasEdge(label1+label2):
            self.getEdge(label1+label2).setFrom(self.getKey(label3))
            self.getEdge(label1+label2).setTo(self.getKey(label4))
            self.getEdge(label1+label2).setLabel(label3, label4)
            self.getKey(label3).addEdge(self.getKey(label4))
            self.getKey(label4).addEdge(self.getKey(label3))
            self.keys.delAdjacent(label1, label2)
            return self.getEdge(label3+label4)
        elif self.keys.hasEdge(label2+label1):
            self.getEdge(label2+label1).setFrom(self.getKey(label3))
            self.getEdge(label2+label1).setTo(self.getKey(label4))
            self.getEdge(label2+label1).setLabel(label3, label4)
            self.getKey(label3).addEdge(self.getKey(label4))
            self.getKey(label4).addEdge(self.getKey(label3))
            self.keys.delAdjacent(label2, label1)
            return self.getEdge(label3+label4)
        
    # Displays all the key (vertices)
    def displayKeys(self):
        self.keys.displayGraph()

    # Displays all relevant information
    def displayInfo(self):
        # Displays all keys 
        print("\nGraph vertices: \n")
        self.displayKeys()  
        # Displays all edges
        print("\nGraph edges: \n")
        self.keys.displayEdges()
        # Displays vertex and edge count
        print("\nVertices count: " + str(self.keys.getVertexCount()))
        print("\nEdges count: " + str(self.keys.getEdgeCount()))
        # Displays corresponding adjacency list and matrix
        print("\nGraph Adjacency list: \n")
        self.keys.displayList()
        print("\nGraph Adjacency matrix: \n")
        self.keys.displayMatrix()

    # Takes string argument and returns it as a queue
    def findString(self, inString):
        string = queue.DSAQueue() # Creates new queue object
        # Enqueues every character in the string into the queue
        for character in inString:
            string.enqueue(character)
        return string # Returns string queue

    # Generates all paths from a string
    def getAllPaths(self, stringQueue):
        # Queue representing all possible paths in a string
        allPaths = queue.DSAQueue()
        # While the first and last character are not equal
        while(stringQueue.peek() != stringQueue.last()): 
            pathList = queue.DSAQueue() # Queue representing the path from one key to another
            paths = queue.DSAQueue()# Queue representing various possible paths from one key to another
            fromLabel = stringQueue.dequeue() # start key 
            toLabel = stringQueue.peek() # destination key
            
            # Mark all keys as unvisited
            for key in self.keys.vertices:
                key.clearVisited()

            self.getPaths(fromLabel, toLabel, pathList, paths) # Get paths from one key to another
            #self.rankPaths(paths)
            allPaths.enqueue(paths) # Enqueue updated list of paths to final queue

        return allPaths

    # Generates paths from one key to another
    def getPaths(self, label1, label2, pathList, paths):
        tempList = queue.DSAQueue() # Temporary list
        start = self.getKey(label1) # start key
        end = self.getKey(label2) # end key

        start.setVisited() # set current key as visited
        pathList.enqueue(start) # enqueue current key

        if(start == end): # if the current key is the end key:
            # queue paths into temporary list, queue whole temporary list into paths queue
            for path in pathList:
                tempList.enqueue(path)
            paths.enqueue(tempList)

        else: # if current key is not end key
            for adj in start.links: # search through adjacent keys
                if(adj.getVisited() == False and pathList.length() <= 4): # if adjacent is unvisited, and pathList has length of 5 or less:
                    self.getPaths(adj.getLabel(), label2, pathList, paths) # use recursion to get all possible (limited) paths from start to end keys
    
        pathList.remove(start) 
        start.clearVisited()

    # Ranks all the paths
    # def rankPaths(self, paths):
    #     shortest = paths.peek().length()
    #     for path in paths:
    #         if path.length() < shortest:
    #             shortest = path.length()
    #             remove = paths.remove(path)
    #             paths.jump(remove)

    # Displays all the paths
    def displayPaths(self, allPaths):
        print()
        for paths in allPaths:
            for path in paths:
                path.display()
            print()

    # Saves all paths to a file
    def savePaths(self, filename, allPaths):
        try:
            # Opens file and writes every path inside allPaths to file 
            with open(filename, 'w') as file:
                for paths in allPaths:
                    for path in paths:
                        for p in path:
                            file.write(str(p) + "\n")
                        file.write('\n')
                    file.write('\n')
        except IOError as e: # Raises IOError if error in processing
            print("Error in file processing: " + str(e))

    def saveKeyboard(self, filename):
        try:
            with open(filename, 'w') as file:
                for edge in self.keys.edges:
                    file.write(str(edge.getFrom().getLabel()) + " " + str(edge.getTo().getLabel()) + "\n")
        except IOError as e: # Raises IOError if error in processing
            print("Error in file processing: " + str(e))

if __name__ == "__main__":

    # If the number of arguments given are less than 1 or more than 5, raise exception
    if(len(sys.argv) < 1 or len(sys.argv) > 5):
        raise Exception("Invalid number of arguments")

    # If the number of arguments given are exactly 1, (class file), display usage information
    elif(len(sys.argv) == 1):
        # Usage information from DSA Assignment 1 Specifications #
        print("\n Usage Information for keyMeUp \n")
        print("No command line arguments: provides usage information")
        print("-i : Interactive Testing Environment (python3 keyMeUp.py -i)")
        print("-s : Silent Mode (python3 keyMeUp.py -s keyFile strFile pathFile")
        print("\nWhen running silent mode: give input and output files on command line")
        print(" - keyFile : the file representing the keyboard")
        print(" - strFile : the file containing one or more strings to generate paths for")
        print(" - pathFile : output the [ranked] paths to a file, with score/rating\n")

    # If "-i" is specified in the command line, load interactive mode
    elif(sys.argv[1] == "-i"):
        keyboard = keyMeUp()
        menu.loadMenu(keyboard)

    # If "-s" is specified:
    elif(sys.argv[1] == "-s"):
        
        # If less than 5 or more than 5 arguments given, raise exception
        if(len(sys.argv) < 5 or len(sys.argv) > 5):
            raise Exception("Invalid number of arguments, see usage information for help")

        # Else if 3 additional arguments for keyFile, strFile, and pathFile are given: load silent mode
        else:
            keyFile = sys.argv[2]
            strFile = sys.argv[3]
            pathFile = sys.argv[4]
            keyboard = keyMeUp()
            keyboard.loadKeyboard(keyFile)
            stringList = keyboard.loadStrings(strFile)
            stringQueue = keyboard.findString(stringList[0])             
            allPaths = keyboard.getAllPaths(stringQueue)
            keyboard.displayPaths(allPaths)
            keyboard.savePaths(pathFile, allPaths)