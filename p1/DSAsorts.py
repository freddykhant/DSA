#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

from re import I


def bubbleSort(A):
    n = len(A)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                swapped = True
        if not swapped:
            return

def insertionSort(A):
    n = len(A)
    for i in range(1, n-1):
        j = i-1
        while j >= 0 and A[i] < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = A[i]

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        min_index = i  
        for j in range(i+1, n-1):
            if A[j] < A[min_index]:
                min_index = j
        
        temp = A[min_index]
        A[min_index] = A[i]
        A[i] = temp

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...
