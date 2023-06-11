#
# DSA Final Assessment Question 4 - Q3HashTable.py
#
# Name : Freddy Khant
# ID   : 20618166
#
# 

import numpy as np
import math
# import timeit
# from PracExamException import *

class Q3HashTable():
    # Inner class Hash Entry
    class Q4HashEntry():
        #0 = never used/free,  1 = used / not free

        def __init__(self, inKey="", value=None):
            self.key = inKey
            self.value = value
            if self.key == "":
                self.state = 0
            else:
                self.state = 1
    # End inner class
    
    def __init__(self, tableSize):

        self.actualSize = self.nextPrime(tableSize - 1)
        self.hashArray = np.zeros(self.actualSize, dtype=object)

        for i in range(0, self.actualSize):
            self.hashArray[i] = self.Q4HashEntry()
        self.hashCount = 0
    
    def put(self, inKey, inValue):
        hashIdx = self.hash(inKey)
        initIdx = hashIdx
        i = 1

        while (self.hashArray[hashIdx] != None and  not self.hashArray[hashIdx].key == inKey):
            if(not self.hashArray[hashIdx].key == inKey):
                if (self.hashArray[hashIdx].state == 1): 
                    hashIdx = (initIdx + i) % len(self.hashArray) 
                if (self.hashArray[hashIdx].state < 1): 
                    self.hashArray[hashIdx] = self.Q4HashEntry(inKey, inValue)
                    self.hashCount = self.hashCount + 1
            i += 1

    ## get Function from Week 7 of DSA Practicals ##

    def get(self, key): 
        hashIdx = self.hash(key)
        initIdx = hashIdx
        found = False
        giveUp = False
        while(not found and not giveUp):
            if(self.hashArray[hashIdx].state == 0):
                giveUp = True
            elif(self.hashArray[hashIdx].key == key):
                found = True
            else:
                hashIdx = (hashIdx + 1) % len(self.hashArray)
                if(hashIdx == initIdx):
                    giveUp = True
        if(not found):
            raise Exception("Key not found")
        retValue = self.hashArray[hashIdx].value
        return retValue


    def getLoadFactor(self):
        
       loadFactor = self.hashCount / len(self.hashArray)

       return loadFactor


    def display(self):
        for i in range(0, len(self.hashArray)): 
            if (self.hashArray[i].value != None):
                    print("\t\t" + str(i) + "\t" + str(self.hashArray[i].key))


    def hash(self, inKey):
        hashIdx = 0
        for i in range(0, len(inKey)): 
            hashIdx = hashIdx + ord(inKey[i])
        retVal = hashIdx % len(self.hashArray)
        return retVal

    def nextPrime(self, inNum):

        isPrime = False

        if (inNum % 2 == 0):
            prime = inNum - 1 
        else:
            prime = inNum

        while (not isPrime):
            prime = prime + 2
            i = 3
            isPrime = True
            rootVal = math.sqrt(prime) 
            
            
            while ((i <= rootVal) and (isPrime)):
                if ((prime % i) == 0): 
                    isPrime = False
                else:
                    i = i + 2 
            
        return prime

    def getArrayLength(self):
        return len(self.hashArray)

def readFile(filename, table1, table2, table3):
    try:
        file = open(filename)
        file.readline()
        line = file.readline()
        lineNum = 0
        while line:
            lineNum += 1
            processLine(line, lineNum, table1, table2, table3)
            line = file.readline()
        file.close()
    except IOError as e:
        print("Error in file processing: " + str(e))

def processLine(row, rowNum, table1, table2, table3):
    identifier = rowNum
    data = row.split(",")
    try:
        table1.put(data[0], identifier)
        table2.put(data[3], identifier)
        table3.put(data[5], identifier)
    except:
        raise TypeError("CSV row had invalid format")

# if __name__ == "__main__":

#     shouldLoop = True
#     movies = Q3HashTable(1063)
#     actors = Q3HashTable(1063)
#     roles = Q3HashTable(1063)
#     readFile('6degrees.csv', movies, actors, roles)

#     while(shouldLoop):
#         print("\nWELCOME TO THE DSA MOVIE HASH DATABASE: \n")
#         print("Choose an option to search: ")
#         print("> 1. Movies")
#         print("> 2. Actors")
#         print("> 3. Roles")
#         print("> 0. Exit")

#         try:
#             option = int(input("\nEnter your choice: "))
#         except:
#             raise PracExamException("Invalid input, try again")

#         if option == 0:
#             print("Exiting program...")
#             shouldloop = 1
#             exit()

#         elif option == 1:
#             try:
#                 searchKey = input("\nSearch Movies: ")
#             except:
#                 raise PracExamException("Invalid input, try again")

#             ### Query time calculation code from SortsTestHarness.py from Week 1 of Practicals ###
#             startTime = timeit.default_timer()
#             print("\nMovie: " + searchKey + ", Value: " + str(movies.get(searchKey)))
#             endTime = timeit.default_timer()
#             runningTotal = endTime - startTime
#             print("Query time: " + str(runningTotal))

#         elif option == 2:
#             try:
#                 searchKey = input("\nSearch Actors: ")
#             except:
#                 raise PracExamException("Invalid input, try again")
#             startTime = timeit.default_timer()
#             print("\nActor: " + searchKey + ", Value: " + str(actors.get(searchKey)))
#             endTime = timeit.default_timer()
#             runningTotal = endTime - startTime
#             print("Query time: " + str(runningTotal))

#         elif option == 3:
#             try:
#                 searchKey = input("\nSearch Roles: ")
#             except:
#                 raise PracExamException("Invalid input, try again")
#             startTime = timeit.default_timer()
#             print("\nRole: " + searchKey + ", Value: " + str(roles.get(searchKey)))
#             endTime = timeit.default_timer()
#             runningTotal = endTime - startTime
#             print("Query time: " + str(runningTotal))