import unittest
import keyMeUp as k
import DSAQueue as q

class testKeyMeUp(unittest.TestCase):
    
    def test_loadKeyboard(self):
        netflix = k.keyMeUp()
        netflix.loadKeyboard("netflix.txt")
        print("\nNetflix: \n")
        netflix.displayKeys()
        stan = k.keyMeUp()
        stan.loadKeyboard("stan.txt")
        print("\nStan: \n")
        stan.displayKeys()
        
    def test_loadStrings(self):
        kb = k.keyMeUp()
        self.assertEqual(["face"], kb.loadStrings("strFile"))
        self.assertEqual(["freddy", "khant", "20618166"], kb.loadStrings("strFile2"))

    def test_getKey(self):
        kb = k.keyMeUp()
        kb.addKey('a')
        kb.addKey('b')
        kb.addKey('c')
        self.assertEqual('a', kb.getKey('a').getLabel())
        self.assertEqual('b', kb.getKey('b').getLabel())
        self.assertEqual('c', kb.getKey('c').getLabel())

    def test_getEdge(self):
        kb = k.keyMeUp()
        kb.addKey('a')
        kb.addKey('b')
        kb.addKey('c')
        kb.addEdge('a', 'b')
        kb.addEdge('b', 'c')
        kb.addEdge('a', 'c')
        self.assertEqual('ab', kb.getEdge('ab').getLabel())
        self.assertEqual('bc', kb.getEdge('bc').getLabel())
        self.assertEqual('ac', kb.getEdge('ac').getLabel())

    def test_addKey(self):
        kb = k.keyMeUp()
        self.assertEqual('a', kb.addKey('a').getLabel())
        self.assertEqual('b', kb.addKey('b').getLabel())
        self.assertEqual('c', kb.addKey('c').getLabel())

    def test_addEdge(self):
        kb = k.keyMeUp()
        kb.addKey('a')
        kb.addKey('b')
        kb.addKey('c')
        self.assertEqual('ab', kb.addEdge('a', 'b').getLabel())
        self.assertEqual('bc', kb.addEdge('b', 'c').getLabel())
        self.assertEqual('ac', kb.addEdge('a', 'c').getLabel())

    def test_deleteKey(self):
        kb = k.keyMeUp()
        kb.addKey('a')
        kb.addKey('b')
        kb.addKey('c')
        self.assertEqual('a', kb.deleteKey('a').getLabel())
        self.assertEqual('b', kb.deleteKey('b').getLabel())
        self.assertEqual('c', kb.deleteKey('c').getLabel())

    def test_deleteEdge(self):
        kb = k.keyMeUp()
        kb.addKey('a')
        kb.addKey('b')
        kb.addKey('c')
        kb.addEdge('a', 'b')
        kb.addEdge('b', 'c')
        kb.addEdge('a', 'c')
        self.assertEqual('ab', kb.deleteEdge('a', 'b').getLabel())
        self.assertEqual('bc', kb.deleteEdge('b', 'c').getLabel())
        self.assertEqual('ac', kb.deleteEdge('a', 'c').getLabel())

    def test_updateKey(self):
        kb = k.keyMeUp()
        kb.addKey('a')
        self.assertEqual('z', kb.updateKey('a', 'z').getLabel())
        self.assertEqual('space', kb.updateKey('z', 'space').getLabel())
        self.assertEqual(1 , kb.updateKey('space', 1).getLabel())

    def test_updateEdge(self):
        kb = k.keyMeUp()
        kb.addKey('a')
        kb.addKey('b')
        kb.addKey('c')
        kb.addEdge('a', 'b')
        self.assertEqual('ac', kb.updateEdge('a', 'b', 'a', 'c').getLabel())

    def test_findString(self):
        kb = k.keyMeUp()
        print("String queue contents: ")
        kb.findString("freddy").display()

    def test_generatePaths(self):
        netflix = k.keyMeUp()
        netflixPaths = q.DSAQueue()
        netflix.loadKeyboard("netflix.txt")
        print("\nNetflix paths: \n")
        netflix.generatePaths(netflix.findString("face"), netflixPaths)
        netflix.displayPaths(netflixPaths)
        print()
        stan = k.keyMeUp()
        stanPaths = q.DSAQueue()
        stan.loadKeyboard("stan.txt")
        print("\nStan paths: \n")
        stan.generatePaths(stan.findString("face"), stanPaths)
        stan.displayPaths(stanPaths)
        print()

        

if __name__ == "__main__":
    unittest.main()