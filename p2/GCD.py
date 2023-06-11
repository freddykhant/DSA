def GCDiterative(x, y): # Calculates greatest common denominator of two arguments iteratively
    if (x < 0 or y < 0):
        raise ValueError("Arguments must be positive")
    elif (x > y):
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

def GCDrecursive(x, y): # Wrapper Method
    if (x < 0 or y < 0):
        raise Exception("Arguments must be positive")
    else:
        return _GCDrecursive(x, y)

def _GCDrecursive(x, y): # Calculates Greatest Common Denominator of two arguments recursively
    if (y == 0):
        recursive = x
    else:
        recursive = GCDrecursive(y, x % y)
    return recursive