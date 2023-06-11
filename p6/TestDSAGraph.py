import unittest
import DSAGraph as g

class testDSAGraph(unittest.TestCase):

    def test_addVertex(self):
        graph = g.DSAGraph()
        graph.addVertex("A", 1)
        graph.addVertex("B", 2)
        graph.addVertex("C", 3)
        self.assertEqual(True, graph.hasVertex("A"))
        self.assertEqual(True, graph.hasVertex("B"))
        self.assertEqual(True, graph.hasVertex("C"))
        self.assertEqual(False, graph.hasVertex("D"))

    def test_addEdge(self):
        graph = g.DSAGraph()
        graph.addVertex("A", 1)
        graph.addVertex("B", 2)
        graph.addVertex("C", 3)
        graph.addVertex("D", 4)
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.addEdge("A", "C")
        self.assertEqual(True, graph.hasEdge("A", "B"))
        self.assertEqual(True, graph.hasEdge("B", "C"))
        self.assertEqual(True, graph.hasEdge("B", "A"))
        self.assertEqual(False, graph.hasEdge("A", "D"))

    def test_hasVertex(self):
        graph = g.DSAGraph()
        graph.addVertex("A", 1)
        self.assertEqual(True, graph.hasVertex("A"))

    def test_hasEdge(self):
        graph = g.DSAGraph()
        graph.addVertex("A", 1)
        graph.addVertex("B", 2)
        graph.addEdge("A", "B")
        self.assertEqual(True, graph.hasEdge("A", "B"))

    def test_getVertexCount(self):
        graph = g.DSAGraph()
        graph.addVertex("A", 1)
        graph.addVertex("B", 2)
        graph.addVertex("C", 3)
        self.assertEqual(3, graph.getVertexCount())

    def test_getEdgeCount(self):
        graph = g.DSAGraph()
        graph.addVertex("A", 1)
        graph.addVertex("B", 2)
        graph.addVertex("C", 3)
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.addEdge("A", "C")
        self.assertEqual(3, graph.getEdgeCount())

    def test_isAdjacent(self):
        graph = g.DSAGraph()
        graph.addVertex("A", 1)
        graph.addVertex("B", 2)
        graph.addVertex("C", 3)
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.addEdge("A", "C")
        self.assertEqual(True, graph.isAdjacent("A", "B"))

if __name__ == "__main__":
    unittest.main()