#
# DSA Final Assessment Question 3 - Q3TreeTest.py
#
# Name : 
# ID   :
#
# 
from Q3BSTree import *
import timeit

print("\n##### Question 3: Testing Trees #####\n")

shouldLoop = True
movies = Q3BSTree()
actors = Q3BSTree()
roles = Q3BSTree()

readFile('6degrees.csv', movies, actors, roles)

while(shouldLoop):
    print("\nWELCOME TO THE DSA MOVIE TREE DATABASE: \n")
    print("Choose an option to search: ")
    print("> 1. Movies")
    print("> 2. Actors")
    print("> 3. Roles")
    print("> 0. Exit")

    try:
        option = int(input("\nEnter your choice: "))
    except:
        raise PracExamException("Invalid input, try again")

    if option == 0:
        print("Exiting program...")
        shouldloop = 1
        exit()

    elif option == 1:
        try:
            searchVal = int(input("\nSearch Movies: "))
        except:
            raise PracExamException("Invalid input, try again")
        ### Query time calculation code from SortsTestHarness.py from Week 1 of Practicals ###
        startTime = timeit.default_timer()
        print(movies.find(searchVal))
        endTime = timeit.default_timer()
        runningTotal = endTime - startTime
        print("Query time: " + str(runningTotal))

    elif option == 2:
        try:
            searchVal = int(input("\nSearch Actors: "))
        except:
            raise PracExamException("Invalid input, try again")
        ### Query time calculation code from SortsTestHarness.py from Week 1 of Practicals ###
        startTime = timeit.default_timer()
        print(actors.find(searchVal))
        endTime = timeit.default_timer()
        runningTotal = endTime - startTime
        print("Query time: " + str(runningTotal))

    elif option == 3:
        try:
            searchVal = int(input("\nSearch Roles: "))
        except:
            raise PracExamException("Invalid input, try again")
        ### Query time calculation code from SortsTestHarness.py from Week 1 of Practicals ###
        startTime = timeit.default_timer()
        print(roles.find(searchVal))
        endTime = timeit.default_timer()
        runningTotal = endTime - startTime
        print("Query time: " + str(runningTotal))

print("\n##### Tests Complete #####\n")


