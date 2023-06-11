import DSALinkedList as ll
import pickle

def printMenu():
    print("\nInteractive Menu for DSALinkedList\n")
    print("Choose an option: ")
    print("> 1. InsertFirst")
    print("> 2. InsertLast")
    print("> 3. RemoveFirst")
    print("> 4. RemoveLast")
    print("> 5. Display list")
    print("> 6. Read serialised file")
    print("> 7. Write serialised file")
    print("> 0. Exit")

def menu():

    loop = 0
    linkedList = ll.DSALinkedList()
    while(loop != 1):
        printMenu()
        try:
            option = int(input("\nEnter your choice: "))
        except:
            raise Exception("Invalid input, try again ")
        if option == 0:
            loop = 1
            print("Exiting program...")
            exit()
        elif option == 1:
            try:
                value = int(input("Enter value to insert: "))
            except:
                raise Exception("Invalid input, try again ")
            linkedList.insertFirst(value)
        elif option == 2:
            try:
                value = int(input("Enter value to insert: "))
            except:
                raise Exception("Invalid input, try again ")
            linkedList.insertLast(value)
        elif option == 3:
            linkedList.removeFirst()
        elif option == 4:
            linkedList.removeLast()
        elif option == 5:
            myiter = iter(linkedList)
            value = next(myiter)
            for value in linkedList:
                print(value)
            loop = 1
        elif option == 6:
            try:
                file = input("Enter file name to be loaded: ")
            except:
                raise Exception("Invalid input, try again ")
            try:
                with open(file, "rb") as dataFile:
                    linkedList = pickle.load(dataFile)
            except:
                print("Error: object file does not exist")
        elif option == 7:
            file = input("Enter file name to be loaded: ")
            print("Saving object to file...")
            try:
                with open(file, "wb") as dataFile:
                    pickle.dump(linkedList, dataFile)
            except:
                print("Error: problem with pickling object")

if __name__ == "__main__":
    menu()