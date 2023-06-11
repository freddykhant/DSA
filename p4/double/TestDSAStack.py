import DSAStack as s
import unittest

class testStack(unittest.TestCase):

    def test_top(self):
        stack = s.DSAStack()
        with self.assertRaises(Exception):
            stack.top()
        stack.push(1)
        self.assertEqual(1, stack.top(), "Top = 1")
    
    def test_push(self):
        stack = s.DSAStack()
        stack.push(1)
        self.assertEqual(1, stack.top(), "Top = 1")
        stack.push(2)
        self.assertEqual(2, stack.top(), "Top = 2")
        stack.push(3)
        self.assertEqual(3, stack.top(), "Top = 3")
    
    def test_pop(self):
        stack = s.DSAStack()
        with self.assertRaises(Exception):
            stack.pop()
        stack.push(1)
        self.assertEqual(1, stack.pop(), "Removed 1")
        stack.push(2)
        self.assertEqual(2, stack.pop(), "Removed 2")
        stack.push(3)
        self.assertEqual(3, stack.pop(), "Removed 3")


if __name__ == '__main__':
    unittest.main()