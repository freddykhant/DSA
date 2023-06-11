def towers(n, start, end):
    if (n == 1):
        moveDisk(n, start, end)
    else:
        other = 6 - (start + end)
        towers(n-1, start, other)
        moveDisk(n, start, end)
        towers(n-1, other, end)

def moveDisk(lvl, start, end):
    print("Recursion Level =", lvl)
    print("Moving Disk from Source", start, "to Destination", end)

towers(3, 1, 3)