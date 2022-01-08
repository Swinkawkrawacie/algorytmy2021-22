#!/usr/bin/env python

class parse_tree():
    def __init__(self, text):
        if isinstance(text,str):
            operator_list = []
            while len(text)>0:
                for j in ['sin', 'cos', 'exp']:
                    if text[:3] == j:
                        operator_list.append(j)
                        text = text[3:]
                if text[:2] == 'ln':
                    operator_list.append('ln')
                    text = text[2:]
                operator_list.append(text[0])
                text = text[1:]
        else:
            operator_list = text
        
        self.text = operator_list
        self.data = None
        self.left = None
        self.right = None
        self.leftover_text = operator_list
        self.build_tree()

    def build_tree(self):

        while len(self.leftover_text)>0:
            if self.leftover_text[0] == '(':
                self.left = parse_tree(self.leftover_text[1:])
                self.leftover_text = self.left.leftover_text
            elif self.leftover_text[0] in ['+','-','*','/','^']:
                self.data = self.leftover_text[0]
                self.right = parse_tree(self.leftover_text[1:])
                self.leftover_text = self.right.leftover_text
            elif self.leftover_text[0] in ['sin', 'cos', 'exp', 'ln']:
                self.data = self.leftover_text[0]
                self.left = parse_tree(self.leftover_text[1:])
                self.right = None
                self.leftover_text = self.left.leftover_text
                return
            elif self.leftover_text[0] == ')':
                self.leftover_text = self.leftover_text[1:]
                return
            else:
                self.data = self.leftover_text[0]
                self.leftover_text = self.leftover_text[1:]
                return
    
    def __str__(self):
        return 'N'+str(self.data) + '\n L' + str(self.left) + '\t R' + str(self.right) 
    
    def printexp(self):
        result = ''
        if self == None:
            return result
        if self.data in ['sin', 'cos', 'ln', 'exp']:
            result = '(' + self.data + self.left.printexp()
        else:
            result = '('
            if self.left != None:
                result += self.left.printexp()
            result += self.data
            if self.right != None:
                result += self.right.printexp()+')'
        return result

class diff_tree():
    def __init__(self, base_tree:parse_tree):
        self.base = base_tree
        self.data = None
        self.left = None
        self.right = None
    
    def put(self):
        current = self.base
        while current != None:
            if current.data == None:
                return
            self.data = current.data
            if current.left != None:
                left_child = diff_tree(current.left)
                left_child.put()
                self.left = left_child
            if current.right != None:
                right_child = diff_tree(current.right)
                right_child.put()
                self.right = right_child
            return


    def diff(self):
        current = self.base
        if current.data in ['+', '-']:
            self.data = current.data
            left_child = diff_tree(current.left)
            left_child.diff()
            self.left = left_child
            right_child = diff_tree(current.right)
            right_child.diff()
            self.right = right_child
        elif current.data == '*':
            self.data = '+'
            self.left = diff_tree(current)
            self.left.data = '*'
            left_child = diff_tree(current.left)
            left_child.diff()
            self.left.left = left_child
            normal_right = diff_tree(current.right)
            normal_right.put()
            self.left.right = normal_right
            
            self.right = diff_tree(current)
            self.right.data = '*'
            right_child = diff_tree(current.right)
            right_child.diff()
            self.right.right = right_child
            normal_left = diff_tree(current.left)
            normal_left.put()
            self.right.left = normal_left
        elif current.data == '/':
            self.data = current.data
            self.left = diff_tree(current)

            self.left.data = '-'
            self.left.left = diff_tree(current)

            self.left.left.data = '*'
            left_child = diff_tree(current.left)
            left_child.diff()
            self.left.left.left = left_child
            normal_right = diff_tree(current.right)
            normal_right.put()
            self.left.left.right = normal_right

            self.left.right = diff_tree(current)
            self.left.right.data = '*'
            normal_left = diff_tree(current.left)
            normal_left.put()
            self.left.right.left = normal_left
            right_child = diff_tree(current.right)
            right_child.diff()
            self.left.right.right = right_child

            self.right = diff_tree(current)
            self.right.data = '^'
            normal_right = diff_tree(current.right)
            normal_right.put()
            self.right.left = normal_right
            self.right.right = '2'
        elif current.data == '^':
            self.data = '*'
            normal_right = diff_tree(current.right)
            normal_right.put()
            self.left = normal_right
            self.right = diff_tree(current)
            self.right.data = '^'
            left_child = diff_tree(current.left)
            left_child.diff()
            self.right.left = left_child
            normal_right = diff_tree(current.right)
            normal_right.put()
            self.right.right = normal_right
            self.right.right.data = str(int(self.right.right.data)-1) # here can be a problem with different types maybe chcnge everything to left right and so on
        elif current.data == 'sin':
            self.data = '*'
            self.left = diff_tree(current)
            self.left.data = 'cos'
            normal_left = diff_tree(current.left)
            normal_left.put()
            self.left.left = normal_left
            self.left.right = None
            right_child = diff_tree(current.left)
            right_child.diff()
            self.right = right_child
        elif current.data == 'cos':
            self.data = '*'
            self.left = diff_tree(current)
            self.left.data = -1
            self.right = diff_tree(current)
            self.right.data = '*'
            self.right.left = diff_tree(current)
            self.right.left.data = 'sin'
            normal_left = diff_tree(current.left)
            normal_left.put()
            self.right.left.left = normal_left
            self.right.left.right = None
            right_child = diff_tree(current.left)
            right_child.diff()
            self.right.right = right_child  
        elif current.data == 'ln':
            self.data = '*'
            self.left = diff_tree(current)
            self.left.data = '/'
            self.left.left = diff_tree(current)
            self.left.left.data = '1'
            normal_left = diff_tree(current.left)
            normal_left.put()
            self.left.right = normal_left
            right_child = diff_tree(current.left)
            right_child.diff()
            self.right = right_child
        elif current.data == 'exp':
            self.data = '*'
            normal = diff_tree(current)
            normal.put()
            self.left = normal
            right_child = diff_tree(current.left)
            right_child.diff()
            self.right = right_child
        elif current.data == 'x':
            self.data = '1'
        else:
            self.data = '0'
    
    def __str__(self):
        return 'N'+str(self.data) + '\n L' + str(self.left) + '\t R' + str(self.right)
    
    def printexp(self):
        result = ''
        if self == None:
            return result
        if self.data in ['sin', 'cos', 'ln', 'exp']:
            result = '(' + self.data + self.left.printexp()
        else:
            result = '('
            if self.left != None:
                result += self.left.printexp()
            result += self.data
            if self.right != None:
                result += self.right.printexp()+')'
        return result

if __name__ == "__main__":
    tree = parse_tree('(((3+5)*4)*sin(x+1))')
    print(tree)
    print('----------------------------------------')
    tree1 = parse_tree('(sin(x+5)*4)')
    print(tree1.text)
    print(tree1)
    print('----------------------------------------')
    tree2 = parse_tree('(4*sin(x+5))')
    print(tree2)
    print('--------------------')
    diff = diff_tree(tree1)
    diff.diff()
    print(diff)
    print(diff.printexp())