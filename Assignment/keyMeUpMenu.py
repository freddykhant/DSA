### keyMeUpMenu program for keyMeUp's interactive menu ###
## No dependencies #

def loadMenu(keyboard):
    loop = True

    while(loop == True):
        print("\nInteractive Menu for keyMeUp\n")
        print("Choose an option: ")
        print("> 1. Load keyboard file")
        print("> 2. Vertex operations")
        print("> 3. Edge operations")
        print("> 4. Display graph")
        print("> 5. Display graph information")
        print("> 6. Enter string for finding path")
        print("> 7. Generate paths")
        print("> 8. Display paths")
        print("> 9. Save keyboard")
        print("> 0. Exit")
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
            keyboard.loadKeyboard(filename)

        elif option == 2:
            print("\nKey operations\n")
            print("> 1. find")
            print("> 2. insert")
            print("> 3. delete")
            print("> 4. update")
            try:
                op = int(input("Enter desired Key operation: "))
            except:
                raise Exception("Invalid input, try again")

            if op == 1:
                try:
                    label = input("Enter label of Key to find: ")
                except:
                    raise Exception("Invalid input, try again")
                if keyboard.keys.hasVertex(label):
                    print(keyboard.getKey(label))
                else:
                    raise Exception("Key: " + label + " does not exist")

            elif op == 2:
                try:
                    label = input("Enter label of new Key: ")
                except:
                    raise Exception("Invalid input, try again")
                keyboard.addKey(label)

            elif op == 3:
                try:
                    label = input("Enter label of Key to delete: ")
                except:
                    raise Exception("Invalid input, try again")
                keyboard.deleteKey(label)

            elif op == 4:
                try:
                    label = input("Enter label of Key to update: ")
                    newLabel = input("Enter new label of Key: ")
                    value = int(input("Enter new value of Vertex: "))
                except:
                    raise Exception("Invalid input, try again")
                keyboard.updateKey(label, newLabel, value)

        elif option == 3:
            print("\nEdge Operations\n")
            print("> 1. find")
            print("> 2. insert")
            print("> 3. delete")
            print("> 4. update")
            try:
                op = int(input("Enter desired edge operation: "))
            except:
                raise Exception("Invalid input, try again")

            if op == 1:
                try:
                    label = input("Enter label of edge to find: ")
                except:
                    raise Exception("Invalid input, try again")
                if keyboard.keys.hasEdge(label):
                    print(keyboard.getEdge(label))
                else:
                    raise Exception("Edge: " + label + " does not exist")

            elif op == 2:
                try:
                    fromLabel = input("Enter label of source Vertex: ")
                    toLabel = input("Enter label of destination Vertex: ")
                except:
                    raise Exception("Invalid input, try again")
                keyboard.addEdge(fromLabel, toLabel)

            elif op == 3:
                try:
                    label = input("Enter label of edge to delete: ")
                except:
                    raise Exception("Invalid input, try again")
                keyboard.deleteEdge(label)

            elif op == 4:
                try:
                    label = input("Enter label of edge to update: ")
                    newFrom = input("Enter new source label: ")
                    newTo = input("Enter new destination label: ")
                except:
                    raise Exception("Invalid input, try again")
                keyboard.updateEdge(label, newFrom, newTo)

        elif option == 4:
            keyboard.displayKeys()

        elif option == 5:
            keyboard.displayInfo()

        elif option == 6:
            try:
                inString = input("Enter string for finding path: ")
            except:
                raise Exception("Invalid input, try again")
            stringQueue = keyboard.findString(inString)

        elif option == 7:
            allPaths = keyboard.getAllPaths(stringQueue)

        elif option == 8:
            keyboard.displayPaths(allPaths)
            try:
                choice = input("Save paths? Y/N\n")
            except:
                raise Exception("Invalid input, try agian")
            if choice == "Y" or choice == "y":
                try:
                    pathFile = input("Enter file name to write: ")
                except:
                    raise Exception("Invalid filename, try again")
                keyboard.savePaths(pathFile, allPaths)
            else:
                continue

        elif option == 9:
            try:
                keyFile = input("Enter file name to save keyboard to: ")
            except:
                raise Exception("Invalid filename, try again")
            keyboard.saveKeyboard(keyFile)
