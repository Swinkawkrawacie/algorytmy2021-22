#!/usr/bin/env python

class parse_tree():
    def __init__(self, text:str):
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
            elif self.leftover_text[0] == ')':
                self.leftover_text = self.leftover_text[1:]
                return
            else:
                self.data = self.leftover_text[0]
                self.leftover_text = self.leftover_text[1:]
                return
    
    def __str__(self):
        return 'N'+str(self.data) + '\n L' + str(self.left) + '\t R' + str(self.right)

class diff_tree():
    def __init__(self, base_tree:parse_tree):
        self.base = base_tree
        self.new_data = None
        self.new_left = None
        self.new_right = None

    def diff(self):
        current = self.base
        if current.data in ['+', '-']:
            self.new_data = current.data
            left_child = diff_tree(current.left)
            left_child.diff()
            self.new_left = left_child
            right_child = diff_tree(current.right)
            right_child.diff()
            self.new_right = right_child
        elif current.data == '*':
            self.new_data = '+'
            self.new_left = diff_tree(current)
            self.new_left.new_data = '*'
            left_child = diff_tree(current.left)
            left_child.diff()
            self.new_left.new_left = left_child
            self.new_left.new_right = current.right
            
            self.new_right = diff_tree(current)
            self.new_right.new_data = '*'
            right_child = diff_tree(current.right)
            right_child.diff()
            self.new_right.new_right = right_child
            self.new_right.new_left = current.left
        elif current.data == '/':
            self.new_data = current.data
            self.new_left = diff_tree(current)

            self.new_left.new_data = '-'
            self.new_left.new_left = diff_tree(current)

            self.new_left.new_left.new_data = '*'
            left_child = diff_tree(current.left)
            left_child.diff()
            self.new_left.new_left.new_left = left_child
            self.new_left.new_left.new_right = current.right

            self.new_left.new_right = diff_tree(current)
            self.new_left.new_right.new_data = '*'
            self.new_left.new_right.new_left = current.left
            right_child = diff_tree(current.right)
            right_child.diff()
            self.new_left.new_right.new_right = right_child

            self.new_right = diff_tree(current)
            self.new_right.new_data = '^'
            self.new_right.new_left = current.right
            self.new_right.new_right = '2'
        elif current.data == 'x':
            self.new_data = 1
        else:
            self.new_data = 0
    
    def __str__(self):
        return 'N'+str(self.new_data) + '\n L' + str(self.new_left) + '\t R' + str(self.new_right)

if __name__ == "__main__":
    tree = parse_tree('(((3+5)*4)*sin(x+1))')
    print(tree)
    print('----------------------------------------')
    tree1 = parse_tree('((3+5)*4)')
    diff = diff_tree(tree1)
    diff.diff()
    print(diff)