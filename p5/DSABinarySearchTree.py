import DSATreeNode as tn
import DSAQueue as q

class DSABinarySearchTree():
    
    def __init__(self):
        self._root = None
    
    def find(self, key):
        return self._findRec(key, self._root)
    
    def _findRec(self, key, curNode):
        value = None
        if curNode is None:
            raise ValueError("Key " + str(key) + " not found")
        elif key == curNode._key:
            value = curNode._value
        elif key < curNode._key:
            value = self._findRec(key, curNode._left)
        else:
            value = self._findRec(key, curNode._right)
        return value
    
    def insert(self, key, value):
        return self._insertRec(key, value, self._root)
    
    def _insertRec(self, key, value, curNode):
        updateNode = curNode
        if self._root is None:
            self._root = tn.DSATreeNode(key, value)
            updateNode = self._root
        elif curNode is None:
            newNode = tn.DSATreeNode(key, value)
            updateNode = newNode
        elif key == curNode._key:
            raise ValueError("Key " + str(key) + " already exists")
        elif key < curNode._key:
            #updateNode = self._insertRec(key, value, curNode._left)
            #curNode.setLeft(updateNode)
            curNode.setLeft(self._insertRec(key, value, curNode._left))
        else:
            #updateNode = self._insertRec(key, value, curNode._right)
            #curNode.setRight(updateNode)
            curNode.setRight(self._insertRec(key, value, curNode._right))
        return updateNode
          
    def delete(self, key):
        return self._deleteRec(key, self._root)

    def _deleteRec(self, key, curNode):
        updateNode = curNode
        if curNode is None:
            raise ValueError("Key " + str(key) + " not found")
        elif key == curNode._key:
            updateNode = self.deleteNode(curNode)
        elif key < curNode._key:
            updateNode = self._deleteRec(key, curNode._left)
            curNode.setLeft(updateNode)
        else:
            updateNode = self._deleteRec(key, curNode._right)
            curNode.setRight(updateNode)
        return updateNode

    def deleteNode(self, delNode): 
        updateNode = None
        if delNode._left == None and delNode._right == None:  
            updateNode = None
        elif delNode._left != None and delNode._right == None: 
            updateNode = delNode._left
        elif delNode._left == None and delNode._right != None: 
            updateNode = delNode._right
        else:                                                  
            updateNode = self.promoteSuccessor(delNode._right)
            if updateNode != delNode._right:
                updateNode.setRight(delNode._right)
            updateNode.setLeft(delNode._left)
        return updateNode

    def promoteSuccessor(self, curNode):
        successor = curNode
        if curNode._left != None:
            successor = self.promoteSuccessor(curNode._left)
            if successor == curNode._left:
                curNode.setLeft(successor._right)
        return successor

    def min(self):
        return self._minRec(self._root)
    
    def _minRec(self, curNode):
        if curNode._left != None:
            minKey = self._minRec(curNode._left)
        else:
            minKey = curNode._key
        return minKey
    
    def max(self):
        return self._maxRec(self._root)
    
    def _maxRec(self, curNode):
        if curNode._right != None:
            maxKey = self._maxRec(curNode._right)
        else:
            maxKey = curNode._key
        return maxKey

    def height(self):
        return self._heightRec(self._root)
    
    def _heightRec(self, curNode):
        leftHeight = -1
        rightHeight = -1
        if curNode is None:
            pass
        else:
            leftHeight = self._heightRec(curNode._left)
            rightHeight = self._heightRec(curNode._right)
        
        if leftHeight > rightHeight:
            heightSoFar = leftHeight + 1
        else:
            heightSoFar = rightHeight + 1
        return heightSoFar
    
    def balance(self):
        left = self._heightRec(self._root._left)
        right = self._heightRec(self._root._right)
        if left < right:
            balance = float((left/right)*100)
        else:
            balance = float((right/left)*100)
        return balance

    def inorder(self):
        inorder = q.DSAQueue()
        self._inorderRec(self._root, inorder)
        return inorder
    
    def _inorderRec(self, curNode, queue):
        if curNode is None:
            pass
        else:
            self._inorderRec(curNode._left, queue) 
            queue.enqueue(curNode) 
            self._inorderRec(curNode._right, queue) 

    def preorder(self):
        preorder = q.DSAQueue()
        self._preorderRec(self._root, preorder)
        return preorder
    
    def _preorderRec(self, curNode, queue):
        if curNode is None:
            pass
        else:
            queue.enqueue(curNode) 
            self._preorderRec(curNode._left, queue) 
            self._preorderRec(curNode._right, queue) 

    def postorder(self):
        postorder = q.DSAQueue()
        self._postorderRec(self._root, postorder)
        return postorder

    def _postorderRec(self, curNode, queue):
        if curNode is None:
            pass
        else:
            self._postorderRec(curNode._left, queue) 
            self._postorderRec(curNode._right, queue) 
            queue.enqueue(curNode) 

if __name__ == "__main__":
    tree = DSABinarySearchTree()
    tree.insert(50, 50)
    tree.insert(16, 16)
    tree.insert(89, 89)
    tree.insert(7, 7)
    print(tree._root)
    print(tree._root._left)
    print(tree._root._right)
    print(tree._root._left._left)
    #print(tree._heightRec(tree._root._left))
    #print(tree._heightRec(tree._root._right))
    #print(tree._root._right._left)