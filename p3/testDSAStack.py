import DSAStack as s
import unittest

class testStack(unittest.TestCase):

    def test_getCount(self):
        stack = s.DSAStack()
        self.assertEqual(0, stack.getCount(), "Stack empty")
        stack.push(1)
        self.assertEqual(1, stack.getCount(), "Stack count > 0")

    def test_isEmpty(self):
        stack = s.DSAStack()
        self.assertEqual(True, stack.isEmpty(), "Stack empty")
        stack.push(1)
        self.assertEqual(False, stack.isEmpty(), "Stack not empty")

    def test_isFull(self):
        stack = s.DSAStack()
        self.assertEqual(False, stack.isFull(), "Stack not full")
        for i in range(stack.size):
            stack.push(i)
        self.assertEqual(True, stack.isFull(), "Stack full")
    
    def test_top(self):
        stack = s.DSAStack()
        with self.assertRaises(Exception):
            stack.top()
        stack.push(1)
        self.assertEqual(1, stack.top(), "Top value = 1")
    
    def test_push(self):
        stack = s.DSAStack()
        stack.push(1)
        self.assertEqual(1, stack.getCount(), "Count = 1")
        self.assertEqual(1, stack.top(), "Top = 1")
        stack.push(2)
        self.assertEqual(2, stack.getCount(), "Count = 2")
        self.assertEqual(2, stack.top(), "Top = 2")
    
    def test_pop(self):
        stack = s.DSAStack()
        with self.assertRaises(Exception):
            stack.pop()
        stack.push(1)
        stack.pop()
        self.assertEqual(0, stack.getCount(), "Count = 0")

if __name__ == '__main__':
    unittest.main()