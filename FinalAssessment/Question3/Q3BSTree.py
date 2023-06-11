#
# DSA Final Assessment Question 3 - Q3BSTree.py
#
# Name : Freddy Khant
# ID   : 20618166
# 
# Note: modified functions from original supplied code, to fit desired functionality
#

from PracExamException import *
import random
# import timeit

class Q3BSTree():
    # Inner Treenode class
    class Q2TreeNode():
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
    # End inner class

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def find(self, key):
        if (self.isEmpty()):
            raise TreeUnderflowException("Tree empty")
        else:
            return self.findRec(key, self.root)
    
    def findRec(self, key, cur):
        value = None
        if (key == cur.key):
            value = cur.value
        else:
            if (key < cur.key):
                value = self.findRec(key, cur.left)
            else:
                value = self.findRec(key, cur.right)
        return value

    def insert(self, key, value):
        if (self.isEmpty()):
            self.root = self.Q2TreeNode(key, value)
            update = self.root
        else:
            update = self.insertRec(key, value, self.root)
        return update

    def insertRec(self, key, value, cur):
        update = cur
        if (cur == None):
            new = self.Q2TreeNode(key, value)
            update = new
        else:
            if (key < cur.key):
                cur.left = self.insertRec(key, value, cur.left)
            else:
                cur.right = self.insertRec(key, value, cur.right)
        return update

# END CLASS

def processLine(row, tree1, tree2, tree3):
    data = row.split(",")
    try:
        tree1.insert(random.randint(1, 1063), data[0])
        tree2.insert(random.randint(1, 1063), data[3])
        tree3.insert(random.randint(1, 1063), data[5])
    except:
        raise TypeError("CSV row had invalid format")

def readFile(filename, tree1, tree2, tree3):
    try:
        file = open(filename)
        file.readline()
        line = file.readline()
        lineNum = 0
        while line:
            lineNum += 1
            processLine(line, tree1, tree2, tree3)
            line = file.readline()
        file.close()
    except IOError as e:
        print("Error in file processing: " + str(e))


# if __name__ == "__main__":
    # shouldLoop = True
    # movies = Q3BSTree()
    # actors = Q3BSTree()
    # roles = Q3BSTree()

    # readFile('6degrees.csv', movies, actors, roles)

    # while(shouldLoop):
    #     print("\nWELCOME TO THE DSA MOVIE TREE DATABASE: \n")
    #     print("Choose an option to search: ")
    #     print("> 1. Movies")
    #     print("> 2. Actors")
    #     print("> 3. Roles")
    #     print("> 0. Exit")

    #     try:
    #         option = int(input("\nEnter your choice: "))
    #     except:
    #         raise PracExamException("Invalid input, try again")

    #     if option == 0:
    #         print("Exiting program...")
    #         shouldloop = 1
    #         exit()

    #     elif option == 1:
    #         try:
    #             searchVal = int(input("\nSearch Movies: "))
    #         except:
    #             raise PracExamException("Invalid input, try again")
    #         ### Query time calculation code from SortsTestHarness.py from Week 1 of Practicals ###
    #         startTime = timeit.default_timer()
    #         print(movies.find(searchVal))
    #         endTime = timeit.default_timer()
    #         runningTotal = endTime - startTime
    #         print("Query time: " + str(runningTotal))

    #     elif option == 2:
    #         try:
    #             searchVal = int(input("\nSearch Movies: "))
    #         except:
    #             raise PracExamException("Invalid input, try again")
    #         ### Query time calculation code from SortsTestHarness.py from Week 1 of Practicals ###
    #         startTime = timeit.default_timer()
    #         print(actors.find(searchVal))
    #         endTime = timeit.default_timer()
    #         runningTotal = endTime - startTime
    #         print("Query time: " + str(runningTotal))

    #     elif option == 3:
    #         try:
    #             searchVal = int(input("\nSearch Movies: "))
    #         except:
    #             raise PracExamException("Invalid input, try again")
    #         ### Query time calculation code from SortsTestHarness.py from Week 1 of Practicals ###
    #         startTime = timeit.default_timer()
    #         print(roles.find(searchVal))
    #         endTime = timeit.default_timer()
    #         runningTotal = endTime - startTime
    #         print("Query time: " + str(runningTotal))