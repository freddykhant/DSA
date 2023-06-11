#
# DSA Final Assessment Question 3 - Q3HashTest.py
#
# Name : Freddy Khant
# ID   : 20618166
#
# 
from Q3HashTable import *
from PracExamException import *
import timeit

print("\n##### Question 3: Testing Hash Tables #####\n")

shouldLoop = True
movies = Q3HashTable(1063)
actors = Q3HashTable(1063)
roles = Q3HashTable(1063)
readFile('6degrees.csv', movies, actors, roles)

while(shouldLoop):
	print("\nWELCOME TO THE DSA MOVIE HASH DATABASE: \n")
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
			searchKey = input("\nSearch Movies: ")
		except:
			raise PracExamException("Invalid input, try again")

		### Query time calculation code from SortsTestHarness.py from Week 1 of Practicals ###
		startTime = timeit.default_timer()
		print("\nMovie: " + searchKey + ", Value: " + str(movies.get(searchKey)))
		endTime = timeit.default_timer()
		runningTotal = endTime - startTime
		print("Query time: " + str(runningTotal))

	elif option == 2:
		try:
			searchKey = input("\nSearch Actors: ")
		except:
			raise PracExamException("Invalid input, try again")
		startTime = timeit.default_timer()
		print("\nActor: " + searchKey + ", Value: " + str(actors.get(searchKey)))
		endTime = timeit.default_timer()
		runningTotal = endTime - startTime
		print("Query time: " + str(runningTotal))

	elif option == 3:
		try:
			searchKey = input("\nSearch Roles: ")
		except:
			raise PracExamException("Invalid input, try again")
		startTime = timeit.default_timer()
		print("\nRole: " + searchKey + ", Value: " + str(roles.get(searchKey)))
		endTime = timeit.default_timer()
		runningTotal = endTime - startTime
		print("Query time: " + str(runningTotal))

print("\n##### Tests Complete #####\n")
