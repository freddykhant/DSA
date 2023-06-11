def decToBase(num, base):
    baseNum = ""
    while (num > 0):
        dig = int(num % base)
        if (dig < 10):
            baseNum += str(dig)
        else:
            baseNum += chr(ord('A') + dig - 10)
            
        num //= base
    
    baseNum = baseNum[::-1]
    return baseNum

def decToBaseRecursive(num, base):
    if (num < 0):
        raise Exception("Decimal number cannot be negative")
    elif (base > 36):
        raise Exception("Maximum base is 36")
    else:
        return _decToBaseRecursive(num, base)

def _decToBaseRecursive(num, base):
    if (num < 1):
        baseNum = ""
    else:
        baseNum = decToBaseRecursive(int(num/base), base) + (num % base)

print(decToBaseRecursive(255, 16))