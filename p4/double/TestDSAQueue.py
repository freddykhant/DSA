import DSAQueue as q
import unittest

class testQueue(unittest.TestCase):

    def test_peek(self):
        queue = q.DSAQueue()
        with self.assertRaises(Exception):
            queue.peek()
        queue.enqueue(1)
        self.assertEqual(1, queue.peek(), "First = 1")
        queue.enqueue(2)
        self.assertEqual(1, queue.peek(), "First = 1")
    
    def test_enqueue(self):
        queue = q.DSAQueue()
        queue.enqueue(1)
        self.assertEqual(1, queue.peek(), "Enqueued 1")
        
    def test_dequeue(self):
        queue = q.DSAQueue()
        queue.enqueue(1)
        self.assertEqual(1, queue.dequeue(), "Dequeued 1")
        queue.enqueue(2)
        self.assertEqual(2, queue.dequeue(), "Dequeued 2")
        queue.enqueue(3)
        self.assertEqual(3, queue.dequeue(), "Dequeued 3")

if __name__ == '__main__':
    unittest.main()