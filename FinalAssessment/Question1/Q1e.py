#
# DSA Final Assessment Question 3 - Q1e.py
#
# Name : Freddy Khant
# ID   : 20618166
#
# 

### Method from GCD.py of Week 2 DSA Practicals ###

def GCDrecursive(x, y, recur): # Calculates Greatest Common Denominator of two arguments recursively
    if (y == 0):
        recursive = x
    else:
        print("x = " + str(x) + " y = " + str(y) + ", Depth: " + str(recur))
        recursive = GCDrecursive(y, x % y, recur+1)
    return recursive

if __name__ == "__main__":
    print(GCDrecursive(2061, 8166, 0))
    print()
    print(GCDrecursive(8166, 2061, 0))