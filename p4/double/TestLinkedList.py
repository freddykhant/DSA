import DSALinkedList as ll
import unittest

class testLinkedList(unittest.TestCase):

    def test_isEmpty(self):
        list = ll.DSALinkedList()
        self.assertEqual(True, list.isEmpty(), "Linked list empty")
        list.insertLast(1)
        self.assertEqual(False, list.isEmpty(), "Linked list not empty")

    def test_peekFirst(self):
        list = ll.DSALinkedList()
        with self.assertRaises(Exception):
            list.peekFirst()
        list.insertFirst(1)
        self.assertEqual(1, list.peekFirst(), "First = 1")
        list.insertFirst(2)
        self.assertEqual(2, list.peekFirst(), "First = 2")

    def test_peekLast(self):
        list = ll.DSALinkedList()
        with self.assertRaises(Exception):
            list.peekLast()
        list.insertLast(1)
        self.assertEqual(1, list.peekLast(), "Last = 1")
        list.insertLast(2)
        self.assertEqual(2, list.peekLast(), "Last = 2")

    def test_insertFirst(self):
        list = ll.DSALinkedList()
        list.insertFirst(1)
        self.assertEqual(1, list.peekFirst(), "First = 1")
        list.insertLast(2)
        self.assertEqual(1, list.peekFirst(), "First = 1")
        list.insertFirst(0)
        self.assertEqual(0, list.peekFirst(), "First = 0")

    def test_insertLast(self):
        list = ll.DSALinkedList()
        list.insertLast(1)
        self.assertEqual(1, list.peekLast(), "Last = 1")
        list.insertLast(2)
        self.assertEqual(2, list.peekLast(), "Last = 2")
        list.insertFirst(3)
        self.assertEqual(2, list.peekLast(), "Last = 2")

    def test_removeFirst(self):
        list = ll.DSALinkedList()
        with self.assertRaises(Exception):
            list.removeFirst()
        list.insertFirst(1)
        self.assertEqual(1, list.removeFirst(), "Removed 1")
        list.insertFirst(1)
        list.insertFirst(2)
        self.assertEqual(2, list.removeFirst(), "Removed 2")

    def test_removeLast(self):
        list = ll.DSALinkedList()
        with self.assertRaises(Exception):
            list.removeLast()
        list.insertLast(1)
        self.assertEqual(1, list.removeLast(), "Removed 1")
        list.insertLast(1)
        list.insertLast(2)
        self.assertEqual(2, list.removeLast(), "Removed 2")


if __name__ == "__main__":
    unittest.main()