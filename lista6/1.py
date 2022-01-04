#!/usr/bin/env python 

class BinaryTree():
    def __init__(self):
        self.data = None
        self.count = 0
        self.left = None
        self.right = None
    
    def set_data(self, value):
        self.data = value
    def set_count(self, value):
        self.count = value
    def set_left(self, item):
        self.left = item
    def set_right(self, item):
        self.right = item
    
    def __str__(self):
        return str(self.data) + '\n' + str(self.left) + '\t' + str(self.right)
    
    def insert(self, value):
        new = BinaryTree()
        new.set_data(value)
        new.set_count(1)

        if self.data != None:
            if self.data < value:
                if self.right != None:
                    self.right.insert(value)
                else:
                    self.set_right(new)
            elif self.data > value:
                if self.left != None:
                    self.left.insert(value)
                else:
                    self.set_left(new)
            else:
                self.set_count(self.count+1)
        else:
            self.set_data(value)
            self.set_count(1)
    
    def get_min(self):
        if self.left == None:
            return self.data
        else:
            return self.left.get_min()
    
    def get_max(self, last=None):
        if self.right == None:
            return self.data
        else:
            return self.right.get_max()
    
    def exists(self, value):
        found = False
        current = self
        while current.data != None and not found:
            if current.data < value:
                current = current.right
            elif current.data > value:
                current = current.left
            else:
                found = True
        return found
    
    def get_successor(self, value):
        current = self
        if self.exists(value):
            while current.data != None:
                if current.data < value:
                    current = current.right
                elif current.data > value:
                    current = current.left
                else:
                    if current.right != None:
                        current = current.right
                        return current.get_min()
                    else:
                        if current.left == None:
                            return None
                        else:
                            return current.left.data
        else:
            return None
    
    def get_item(self, value):
        current = self
        if self.exists(value):
            while current.data != None:
                if current.data < value:
                    current = current.right
                elif current.data > value:
                    current = current.left
                else:
                    return current
    
    def delete(self, value):
        current = self
        if self.exists(value):
            while current.data != None:
                if current.data < value:
                    previous = current
                    current = current.right
                elif current.data > value:
                    previous = current
                    current = current.left
                elif current.count != 1:
                    current.set_count(current.count-1)
                else:
                    if current.left == None:
                        if current.right == None:
                            if previous.right == current:
                                previous.set_right(None)
                                return self
                            else:
                                previous.set_left(None)
                                return self
                        else:
                            if previous.right == current:
                                previous.set_right(current.right)
                                return self
                            else:
                                previous.set_left(current.right)
                                return self
                    elif current.right == None:
                        if previous.right == current:
                            previous.set_right(current.left)
                            return self
                        else:
                            previous.set_left(current.left)
                            return self
                    else:
                        new_value = self.get_successor(value)
                        new = self.get_item(new_value)
                        new_count = new.count
                        new.set_count(1)
                        tree = self.delete(new_value)
                        current = tree.get_item(current.data)
                        current.set_data(new_value)
                        current.set_count(new_count)
                        return tree
    
    def preorder(self):
        if self != None:
            print(self.data)
            self.left.preorder()
            self.right.preorder()
    
    def postorder(self):
        if self != None:
            self.left.postorder()
            self.right.postorder()
            print(self.data)
    
    def inorder(self):
        if self != None:
            self.left.inorder()
            print(self.data)
            self.right.inorder()


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(7)
    tree.insert(3)
    tree.insert(1)
    tree.insert(4)
    tree.insert(12)
    tree.insert(19)
    tree.insert(8)
    tree.insert(7)
    print(tree)
    print('----------------------')
    tree.delete(5)
    print(tree)
    print('----------------------')
    print(tree.delete(3))
    print('----------------------')
    tree.preorder()
    tree.postorder()
    tree.inorder()