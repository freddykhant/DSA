import unittest
import DSABinarySearchTree as t

class testBinarySearchTree(unittest.TestCase):

    def test_find(self):
        tree = t.DSABinarySearchTree()
        with self.assertRaises(Exception):
            tree.find(50)
        tree.insert(50, 1)
        self.assertEqual(1, tree.find(50))
        tree.insert(16, 2)
        self.assertEqual(2, tree.find(16))
    
    def test_insert(self):
        tree = t.DSABinarySearchTree()
        tree.insert(50, 1)
        tree.insert(16, 2)
        self.assertEqual(1, tree.find(50))
        self.assertEqual(2, tree.find(16))

    def test_delete(self):
        tree = t.DSABinarySearchTree()
        tree.insert(10, 10)
        tree.insert(3, 3)
        tree.insert(16, 16)
        tree.delete(16)
        with self.assertRaises(ValueError):
            tree.find(16)

    def test_min(self):
        tree = t.DSABinarySearchTree()
        tree.insert(50, 50)
        tree.insert(16, 16)
        tree.insert(89, 89)
        tree.insert(7, 7)
        self.assertEqual(7, tree.min())

    def test_max(self):
        tree = t.DSABinarySearchTree()
        tree.insert(10, 10)
        tree.insert(3, 3)
        tree.insert(16, 16)
        tree.insert(1, 1)
        tree.insert(7, 7)
        self.assertEqual(16, tree.max())

    def test_height(self):
        tree = t.DSABinarySearchTree()
        tree.insert(50, 50)
        tree.insert(16, 16)
        tree.insert(89, 89)
        tree.insert(7, 7)
        self.assertEqual(3, tree.height())
    
    def test_balance(self):
        tree = t.DSABinarySearchTree()
        tree.insert(50, 50)
        tree.insert(16, 16)
        tree.insert(89, 89)
        tree.insert(7, 7)
        tree.insert(90, 90)
        self.assertEqual(100, tree.balance()) # left is higher than right 
    
if __name__ == "__main__":
    unittest.main()