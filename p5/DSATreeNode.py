class DSATreeNode():

    def __init__(self, inKey, inValue):
        self._key = inKey
        self._value = inValue
        self._left = None
        self._right = None

    def __str__(self):
        return ("Key: " + str(self._key) + " Value: " + str(self._value))
    
    def getKey(self):
        return self._key
    
    def getValue(self):
        return self._value
    
    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right
    
    def setLeft(self, newLeft):
        self._left = newLeft
    
    def setRight(self, newRight):
        self._right = newRight
        