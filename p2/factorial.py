def calcNFactorialIterative(n):
    factorial = 1
    for i in range(n, 1, -1):
        factorial *= i
    return factorial

def calcNFactorial(n): # Wrapper method
    if (n < 0):
        raise Exception("Input must not be negative")
    elif (n > 997):
        raise Exception("Input creates stack overflow") # Maximum recursion depth exceeded at n = 998 causing stack overflow
    else:
        return _calcNFactorialRecursive(n)

def _calcNFactorialRecursive(n): # Calculates nth factorial recursively 
    if (n == 0):
        factorial = 1
    else:
        factorial = n * calcNFactorial(n-1)
    return factorial