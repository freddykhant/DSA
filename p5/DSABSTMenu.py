import DSABinarySearchTree as t
import pickle

def menu():
    
    loop = True
    tree = t.DSABinarySearchTree()
    values = []
    keys = []

    while(loop != False):
        printMenu()
        try:
            option = int(input("\nEnter your choice: "))
        except:
            raise Exception("Invalid input, try again")
        if option == 0:
            loop = 1
            print("Exiting program...")
            exit()
        elif option == 1:
            try:
                filename = input("Enter .csv filename to read: ")
            except:
                raise Exception("Invalid filename, try again")
            readFile(filename, keys, values)
            for i in range(len(keys)):
                tree.insert(keys[i], values[i])
        elif option == 2:
            try:
                file = input("Enter filename to be loaded: ")
            except:
                raise Exception("Invalid input, try again")
            try:
                with open(file, "rb") as dataFile:
                    tree = pickle.load(dataFile)
            except:
                print("Error: object file does not exist")
        elif option == 3:
            print("How would you like to display your tree?")
            print("> 1. Inorder")
            print("> 2. Preorder")
            print("> 3. Postorder")
            try:
                traversalOption =  int(input("Enter desired method of traversal: "))
            except:
                raise Exception("Invalid entry, try again")
            if traversalOption == 1:
                tree.inorder().display()
            elif traversalOption == 2:
                tree.preorder().display()
            elif traversalOption == 3:
                tree.postorder().display()
        elif option == 4:
            print("How would you like to write your tree?")
            print("> 1. Inorder")
            print("> 2. Preorder")
            print("> 3. Postorder")
            try:
                traversalOption =  int(input("Enter desired method of traversal: "))
                filename = input("Enter .csv filename to read: ")
            except:
                raise Exception("Invalid entry, try again")
            if traversalOption == 1:
                try:
                    file = open(filename, 'w')
                    inorderQueue = tree.inorder().queue
                    myiter = iter(inorderQueue)
                    node = next(myiter)
                    for node in inorderQueue:
                        file.write(str(node))
                        file.write('\n')
                    file.close()
                except IOError as e:
                    print("Error in file writing: " + str(e))
            if traversalOption == 2:
                try:
                    file = open(filename, 'w')
                    preorderQueue = tree.preorder().queue
                    myiter = iter(preorderQueue)
                    node = next(myiter)
                    for node in preorderQueue:
                        file.write(str(node))
                        file.write('\n')
                    file.close()
                except IOError as e:
                    print("Error in file writing: " + str(e))
            if traversalOption == 3:
                try:
                    file = open(filename, 'w')
                    postorderQueue = tree.postorder().queue
                    myiter = iter(postorderQueue)
                    node = next(myiter)
                    for node in postorderQueue:
                        file.write(str(node))
                        file.write('\n')
                    file.close()
                except IOError as e:
                    print("Error in file writing: " + str(e))
        elif option == 5:
            file = input("Enter file name to be loaded: ")
            print("Saving object to file...")
            try:
                with open(file, "wb") as dataFile:
                    pickle.dump(tree, dataFile)
            except:
                print("Error: problem with pickling tree")

def printMenu():

    print("\nInteractive Menu for DSABinarySearchTree\n")
    print("Choose an option: ")
    print("> 1. Read a .csv file")
    print("> 2. Read a serialised file")
    print("> 3. Display the tree")
    print("> 4. Write a .csv file")
    print("> 5. Write a serialised file")
    print("> 0. Exit")

def processLine(row, keyArray, valueArray):
    data = row.split(",")
    try:
        keyArray.append(int(data[0]))
        valueArray.append(int(data[1]))
    except:
        raise TypeError("CSV row had invalid format")

def readFile(filename, keyArray, valueArray):
    try:
        file = open(filename)
        lineNum = 0
        line = file.readline()
        while line:
            lineNum += lineNum
            processLine(line, keyArray, valueArray)
            line = file.readline()
        file.close()
    except IOError as e:
        print("Error in file processing: " + str(e))
    
if __name__ == "__main__":
    menu()