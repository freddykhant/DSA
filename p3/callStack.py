import DSAStack as s

stk = s.DSAStack()

def factorialIterative(n, stack):
    stack.push(f"factorialIterative, n = {n}")
    print("Displaying contents after push")
    stack.display()

    factorial = 1
    for i in range(n, 1, -1):
        factorial *= i

    stack.pop()
    if(stk.count > 0):
        print("Displaying contents after pop")
    stack.display()
    return factorial

def factorialRecursive(n, stack): # Wrapper method
    if (n < 0):
        raise Exception("Input must not be negative")
    elif (n > 997):
        raise Exception("Input creates stack overflow") # Maximum recursion depth exceeded at n = 998 causing stack overflow
    else:
        return _factorialRecursive(n, stack)


def _factorialRecursive(n, stack): # Calculates nth factorial recursively 
    stack.push(f"factorialRecursive, n = {n}")
    print("Displaying contents after push")
    stack.display()

    if (n == 0):
        factorial = 1
    else:
        factorial = n * _factorialRecursive(n-1, stk)

    stack.pop()
    if(stk.count > 0):
        print("Displaying contents after pop")
    stack.display()
    return factorial

_factorialRecursive(3, stk)