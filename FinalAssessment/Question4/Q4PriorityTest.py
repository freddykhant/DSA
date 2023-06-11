#
# DSA Final Assessment Question 5 - Q4PriorityTest.py
#
# Name : Freddy Khant
# ID   : 20618166
#
#

import queue
import unittest 

class Q4PriorityTest(unittest.TestCase):

    def test_empty(self):
        q = queue.PriorityQueue()
        self.assertEqual(True, q.empty(), "Queue empty")
        q.put(1)
        self.assertEqual(False, q.empty(), "Queue not empty")

    def test_full(self):
        q = queue.PriorityQueue(5)
        self.assertEqual(False, q.full(), "Queue not full")
        for i in range(5):
            q.put(i)
        self.assertEqual(True, q.full(), "Queue full")

    def test_qsize(self):
        q = queue.PriorityQueue(5)
        self.assertEqual(0, q.qsize(), "Initially empty")
        q.put(1)
        self.assertEqual(1, q.qsize(), "After adding an item")
        q.get()
        self.assertEqual(0, q.qsize(), "After removing item")

    def test_put(self):
        integerQueue = queue.PriorityQueue(5)
        stringQueue = queue.PriorityQueue(5)
        integerQueue.put(20618166)
        self.assertEqual(20618166, integerQueue.get(), "Put integer")
        stringQueue.put("Freddy")
        self.assertEqual("Freddy", stringQueue.get(), "Put string")

    def test_fullEx(self):
        q = queue.PriorityQueue(5)
        with self.assertRaises(queue.Full):
            for i in range(6):
                q.put(i, timeout=1)

    def test_get(self):
        integerQueue = queue.PriorityQueue(3)
        stringQueue = queue.PriorityQueue(3)
        for i in range(1, 4):
            integerQueue.put(i)
        self.assertEqual(1, integerQueue.get(), "Gets top priority int")
        self.assertEqual(2, integerQueue.get(), "Gets second priority int")
        self.assertEqual(3, integerQueue.get(), "Gets third priority int")
        stringQueue.put("A")
        stringQueue.put("B")
        stringQueue.put("C")
        self.assertEqual("A", stringQueue.get(), "Gets top priority string")
        self.assertEqual("B", stringQueue.get(), "Gets second priority string")
        self.assertEqual("C", stringQueue.get(), "Gets third priority string")

    def test_emptyEx(self):
        q = queue.PriorityQueue(5)
        with self.assertRaises(queue.Empty):
            q.get(timeout=1)

if __name__ == '__main__':
    unittest.main()