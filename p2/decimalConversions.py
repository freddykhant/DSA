def getbinary(number): # https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/ #
    if (number == 0):
        return 0
    
    smallans = getbinary(number // 2)
    result = number % 2 + 10 * smallans
    
    return result
