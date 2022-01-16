#!/usr/bin/env python 

class TreeNode:
    def __init__(self,key,val,left=None,right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.count = 1

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                     succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    
    def __str__(self):
        if self:
            return str(self.payload) + '\n' + str(self.leftChild) + '\t' + str(self.rightChild)
        else:
            return None
    
    def print_keys(self):
        if self:
            result = str(self.key) + '\n'
            if self.leftChild:
                result += self.leftChild.print_keys() + '\t' 
            else:
                result += 'None \t'
            if self.rightChild:
                result += self.rightChild.print_keys()
            else:
                result += 'None'
            return result
        else:
            return None

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def put(self,key,val):
        if self.get(key):
            self._get(key,self.root).count += 1
            self.size -= 1
            self._get(key,self.root).payload = val
        elif self.root:
            self._put(key,val,self.root) #_put is a helper function
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v): #overloading of [] operator
        self.put(k,v) 

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key): #overloading of [] operator
        return self.get(key)        

    def __contains__(self,key):  # overloading of in operator
        if self._get(key,self.root):
            return True
        else:
            return False
       
    def delete(self,key):
        if self._get(key,self.root):
            print(self._get(key,self.root).count)
            if self._get(key,self.root).count == 1:
                if self.size > 1:
                    nodeToRemove = self._get(key,self.root)
                    if nodeToRemove:
                        self.remove(nodeToRemove)
                        self.size = self.size-1
                    else:
                        raise KeyError('Error, key not in tree')
                elif self.size == 1 and self.root.key == key:
                    self.root = None
                    self.size = self.size - 1
                else:
                    raise KeyError('Error, key not in tree')
            else:
                self._get(key,self.root).count -= 1

    def __delitem__(self,key): #overloading of del operator
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                     succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            currentNode.count = succ.count

        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)
    
    def __str__(self):
        if self.root:
            return str(self.root.payload) + '\n' + str(self.root.leftChild) + '\t' + str(self.root.rightChild)
        else:
            return None
    
    def print_keys(self):
        if self:
            result = str(self.root.key) + '\n'
            if self.root.leftChild:
                result += self.root.leftChild.print_keys() + '\t'
            else:
                result += 'None \t'
            if self.root.rightChild:
                result += self.root.rightChild.print_keys()
            else:
                result += 'None'
            return result
        else:
            return None

if __name__ == "__main__":
    tree = BinarySearchTree()
    tree[5]='kot'
    tree[7]='doggo'
    tree[-1] = 'oink'
    tree[3] = 'kwak'
    tree[7] = 'woof'
    print(tree)
    print('----------------------')
    tree.delete(5)
    print(tree[5])
    print('----------------------')
    tree.delete(7)
    print(tree[7])
    print('----------------------')
    print(tree)
    print(tree.print_keys())