import callStack 
import DSAStack 
import unittest, sys, io

class testCallStack(unittest.TestCase):

    def test_factorialIterative(self):
        stack = DSAStack.DSAStack()
        capout =  io.StringIO()
        sys.stdout = capout
        callStack.factorialIterative(2, stack)
        self.assertEqual("Displaying contents after push\nfactorialIterative, n = 2\n", capout.getvalue())
       
    def factorialRecursive(self):
        stack = DSAStack.DSAStack()
        capout =  io.StringIO()
        sys.stdout = capout
        callStack.factorialRecursive(2, stack)
        self.assertEqual("Displaying contents after push\nfactorialRecursive, n = 2\nfactorialRecursive, n = 1\nDisplaying contents after push\nfactorialRecursive, n = 2\nfactorialRecursive, n = 1\nfactorialRecursive, n = 0\nDisplaying contents after pop\nfactorialRecursive, n = 2\nfactorialRecursive, n = 1\nDisplaying contents after pop\nfactorialRecursive, n = 2\n")

if __name__ == '__main__':
    unittest.main()