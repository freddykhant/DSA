def fibIterative(n): # Calculates the nth Fibonacci value iteratively
    fibVal = 0
    currVal = 1
    lastVal = 0

    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        for i in range(2, n):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal

def fibRecursive(n): # Wrapper Method

    if (n < 0):
        raise Exception("Input must not be negative")
    elif (n > 998):
        raise Exception("Input creates stack overflow") # Maximum recursion depth exceeded at n = 999 causing stack overflow
    else:
        return _fibRecursive(n)

def _fibRecursive(n): # Calculates the nth Fibonacci value recursively 
    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2)
    return fibVal