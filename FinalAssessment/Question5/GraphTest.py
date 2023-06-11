#
# DSA Final Assessment Question 5 - Q5GraphTest.py
#
# Name : Freddy Khant
# ID   : 20618166
#
# 
from Q5Graph import *
    

print("\n##### Question 5: Testing Graphs #####\n")

g = Q5Graph(20)
g.readFile("5degrees.csv")

print("Graph in List Format: ")
g.displayAsList()

print("\n Graph in Matrix Format: ")
g.displayAsMatrix()

print("\nDisplaying all Movies: ")
g.displayMovies()

print("\nDisplaying all Actors: ")
g.displayActors()

print("\nHugh Grant Movies: \n")
g.displayActorsMovies("Hugh Grant ")

print("\nActors in Love Actually: \n")
g.displayMovieActors("Love Actually")

print()
g.displayCoStars("Hugh Grant ")


print("\n##### Tests Complete #####\n")
