import DSAQueue as q
import unittest

class testQueue(unittest.TestCase):

    def test_getCount(self):
        shuffle = q.shufflingQueue()
        circle = q.circularQueue()
        self.assertEqual(0, shuffle.getCount(), "Queue empty")
        self.assertEqual(0, circle.getCount(), "Queue empty")
        circle.enqueue(1)
        shuffle.enqueue(1)
        self.assertEqual(1, shuffle.getCount(), "Queue count > 0")
        self.assertEqual(1, circle.getCount(), "Queue count > 0")
    
    def test_isEmpty(self):
        shuffle = q.shufflingQueue()
        circle = q.circularQueue()
        self.assertEqual(True, shuffle.isEmpty(), "Queue empty")
        self.assertEqual(True, circle.isEmpty(), "Queue empty")
        shuffle.enqueue(1)
        circle.enqueue(1)
        self.assertEqual(False, shuffle.isEmpty(), "Queue not empty")
        self.assertEqual(False, circle.isEmpty(), "Queue not empty")

    def test_isFull(self):
        shuffle = q.shufflingQueue()
        circle = q.circularQueue()
        self.assertEqual(False, shuffle.isFull(), "Queue not full")
        self.assertEqual(False, circle.isFull(), "Queue not full")
        for i in range(shuffle.size):
            shuffle.enqueue(i)
            circle.enqueue(i)
        self.assertEqual(True, shuffle.isFull(), "Queue full")
        self.assertEqual(True, circle.isFull(), "Queue full")

    def test_peek(self):
        shuffle = q.shufflingQueue()
        circle = q.circularQueue()
        with self.assertRaises(Exception):
            shuffle.peek()
            circle.peek()
        shuffle.enqueue(1)
        circle.enqueue(1)
        self.assertEqual(1, shuffle.peek(), "First = 1")
        self.assertEqual(1, circle.peek(), "First = 1")
    
    def test_enqueue(self):
        shuffle = q.shufflingQueue()
        circle = q.circularQueue()
        shuffle.enqueue(1)
        circle.enqueue(1)
        self.assertEqual(1, shuffle.getCount())
        self.assertEqual(1, shuffle.peek())
        self.assertEqual(1, circle.getCount())
        self.assertEqual(1, circle.peek())
        with self.assertRaises(Exception):
            for i in range(shuffle.size):
                shuffle.enqueue(i)
        for i in range(circle.size):
            circle.enqueue(i)
        self.assertEqual(100, circle.getCount())
        self.assertEqual(1, circle.rear)

    def test_dequeue(self):
        shuffle = q.shufflingQueue()
        circle = q.circularQueue()
        for i in range(2):
            shuffle.enqueue(i)
            circle.enqueue(i)
        shuffle.dequeue
        circle.dequeue
        self.assertEqual(2, shuffle.getCount())
        self.assertEqual(2, circle.getCount())


if __name__ == '__main__':
    unittest.main()