import DSAGraph as g

def readFile(filename, graph):
    try:
        file = open(filename)
        line = file.readline()
        while line:
            line = line.strip('\n')
            processLine(line, graph)
            line = file.readline()
        file.close()
    except IOError as e:
        print("Error in file processing: " + str(e))

def processLine(row, graph):
    edge = row.split(" ")
    vertex1 = edge[0]
    vertex2 = edge[1]
    try:
        if not graph.hasVertex(vertex1):
            try:
                value1 = int(input("Enter value of " + vertex1 + ": "))
            except:
                raise Exception("Invalid value")
            graph.addVertex(vertex1, value1)
        if not graph.hasVertex(vertex2):
            try:
                value2 = int(input("Enter value of " + vertex2 + ": "))
            except:
                raise Exception("Invalid value")
            graph.addVertex(vertex2, value2)
        graph.addEdge(vertex1, vertex2)
    except:
        raise TypeError("Row had invalid format")

def printMenu():
    print("\nInteractive Menu for DSAGraph\n")
    print("Choose an option: ")
    print("> 1. Read a file")
    print("> 2. Display as list")
    print("> 3. Display as matrix")
    print("> 4. Display depth first search")
    print("> 5. Display breadth first search")
    print("> 0. Exit")

def menu():
    loop = True
    graph = g.DSAGraph()

    while(loop == True):
        printMenu()
        try:
            option = int(input("\nEnter your choice: "))
        except:
            raise Exception("Invalid input, try again")
        if option == 0:
            print("Exiting program...")
            loop = False
        elif option == 1:
            try:
                filename = input("Enter file name to read: ")
            except:
                raise Exception("Invalid filename, try again")
            readFile(filename, graph)
        elif option == 2:
            print(graph.displayList())
        elif option == 3:
            print(graph.displayMatrix())
        elif option == 4:
            graph.depthFirstSearch('A').display()
        elif option == 5:
            graph.breadthFirstSearch('A').display()

if __name__ == "__main__":
    menu()