#!/usr/bin/env python

class parse_tree():
    """
    Tree created from a string
    """
    def __init__(self, text, operand):
        if not isinstance(operand, str):
            raise TypeError('operand should be a string')
        if isinstance(text,str):
            operand_list = []
            while len(text)>0:
                for j in ['sin', 'cos', 'exp']:
                    if text[:3] == j:
                        operand_list.append(j)
                        text = text[3:]
                if text[:2] == 'ln':
                    operand_list.append('ln')
                    text = text[2:]
                operand_list.append(text[0])
                text = text[1:]
        elif isinstance(text, list):
            operand_list = text
        else:
            raise TypeError('incorrect type of the text')
        
        self.operand = operand
        self.text = operand_list
        self.data = None
        self.left = None
        self.right = None
        self.leftover_text = operand_list
        self.build_tree()

    def build_tree(self):
        """
        Build a tree from the text
        """
        while len(self.leftover_text)>0:
            if self.leftover_text[0] == '(':
                self.left = parse_tree(self.leftover_text[1:], self.operand)
                self.leftover_text = self.left.leftover_text
            elif self.leftover_text[0] in ['+','-','*','/','^']:
                self.data = self.leftover_text[0]
                self.right = parse_tree(self.leftover_text[1:], self.operand)
                self.leftover_text = self.right.leftover_text
            elif self.leftover_text[0] in ['sin', 'cos', 'exp', 'ln']:
                self.data = self.leftover_text[0]
                self.left = parse_tree(self.leftover_text[1:], self.operand)
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

class diff_tree():
    """
    Binary tree with the base of a parse_tree and ability to calculate a differential of a expression on a parse_tree
    """
    def __init__(self, base_tree:parse_tree, operand):
        self.base = base_tree
        self.data = None
        self.left = None
        self.right = None
        self.operand = operand
    
    def put(self):
        """
        Translate a base tree to a diff_tree
        """
        current = self.base
        while current != None:
            if current.data == None:
                return
            self.data = current.data
            if current.left != None:
                left_child = diff_tree(current.left, self.operand)
                left_child.put()
                self.left = left_child
            if current.right != None:
                right_child = diff_tree(current.right, self.operand)
                right_child.put()
                self.right = right_child
            return


    def diff(self):
        """
        Calculate a differential of a expression on a base tree
        """
        current = self.base
        if current.data in ['+', '-']:
            self.data = current.data
            left_child = diff_tree(current.left, self.operand)
            left_child.diff()
            self.left = left_child
            right_child = diff_tree(current.right, self.operand)
            right_child.diff()
            self.right = right_child
        elif current.data == '*':
            self.data = '+'
            self.left = diff_tree(current, self.operand)
            self.left.data = '*'
            left_child = diff_tree(current.left, self.operand)
            left_child.diff()
            self.left.left = left_child
            normal_right = diff_tree(current.right, self.operand)
            normal_right.put()
            self.left.right = normal_right
            
            self.right = diff_tree(current, self.operand)
            self.right.data = '*'
            right_child = diff_tree(current.right, self.operand)
            right_child.diff()
            self.right.right = right_child
            normal_left = diff_tree(current.left, self.operand)
            normal_left.put()
            self.right.left = normal_left
        elif current.data == '/':
            self.data = current.data
            self.left = diff_tree(current, self.operand)

            self.left.data = '-'
            self.left.left = diff_tree(current, self.operand)

            self.left.left.data = '*'
            left_child = diff_tree(current.left, self.operand)
            left_child.diff()
            self.left.left.left = left_child
            normal_right = diff_tree(current.right, self.operand)
            normal_right.put()
            self.left.left.right = normal_right

            self.left.right = diff_tree(current, self.operand)
            self.left.right.data = '*'
            normal_left = diff_tree(current.left, self.operand)
            normal_left.put()
            self.left.right.left = normal_left
            right_child = diff_tree(current.right, self.operand)
            right_child.diff()
            self.left.right.right = right_child

            self.right = diff_tree(current, self.operand)
            self.right.data = '^'
            normal_right = diff_tree(current.right, self.operand)
            normal_right.put()
            self.right.left = normal_right
            self.right.right = '2'
        elif current.data == '^':
            self.data = '*'
            normal_right = diff_tree(current.right, self.operand)
            normal_right.put()
            self.left = normal_right
            self.right = diff_tree(current, self.operand)
            self.right.data = '^'
            left_child = diff_tree(current.left, self.operand)
            left_child.diff()
            self.right.left = left_child
            normal_right = diff_tree(current.right, self.operand)
            normal_right.put()
            self.right.right = normal_right
            try:
                int(self.right.right.data)
            except:
                raise ValueError('incorrect expression')
            self.right.right.data = str(int(self.right.right.data)-1)
        elif current.data == 'sin':
            self.data = '*'
            self.left = diff_tree(current, self.operand)
            self.left.data = 'cos'
            normal_left = diff_tree(current.left, self.operand)
            normal_left.put()
            self.left.left = normal_left
            self.left.right = None
            right_child = diff_tree(current.left, self.operand)
            right_child.diff()
            self.right = right_child
        elif current.data == 'cos':
            self.data = '*'
            self.left = diff_tree(current, self.operand)
            self.left.data = '-1'
            self.right = diff_tree(current, self.operand)
            self.right.data = '*'
            self.right.left = diff_tree(current, self.operand)
            self.right.left.data = 'sin'
            normal_left = diff_tree(current.left, self.operand)
            normal_left.put()
            self.right.left.left = normal_left
            self.right.left.right = None
            right_child = diff_tree(current.left, self.operand)
            right_child.diff()
            self.right.right = right_child  
        elif current.data == 'ln':
            self.data = '*'
            self.left = diff_tree(current, self.operand)
            self.left.data = '/'
            self.left.left = diff_tree(current, self.operand)
            self.left.left.data = '1'
            normal_left = diff_tree(current.left, self.operand)
            normal_left.put()
            self.left.right = normal_left
            right_child = diff_tree(current.left, self.operand)
            right_child.diff()
            self.right = right_child
        elif current.data == 'exp':
            self.data = '*'
            normal = diff_tree(current, self.operand)
            normal.put()
            self.left = normal
            right_child = diff_tree(current.left, self.operand)
            right_child.diff()
            self.right = right_child
        elif current.data == self.operand:
            self.data = '1'
        else:
            self.data = '0'
    
    def __str__(self):
        return 'N'+str(self.data) + '\n L' + str(self.left) + '\t R' + str(self.right)
    
    def printexp(self):
        """
        Get the final expression

        @return: (str) the final expression
        """
        result = []
        if self == None:
            return result
        result.append('(')
        if self.data in ['sin', 'cos', 'ln', 'exp']:
            result.append(self.data)
            result.extend(self.left.printexp())
        else:
            if self.left != None:
                result.extend(self.left.printexp())
            result.append(self.data)
            if self.right != None:
                result.extend(self.right.printexp())
        result.append(')')
        return result

def diff_exp(base_tree, operand):
    """
    Calculate the differential of the expression from a given tree

    @param base_tree: (parse_tree) tree to calculate from
    @param operand: (str) opertator of the 
    @return: (str) the final differential
    """
    #------------------checking data--------------------
    if not (isinstance(base_tree, parse_tree) and isinstance(operand, str)):
        raise TypeError('incorrect type of given data')
    #---------------------------------------------------
    new_tree = diff_tree(base_tree, operand)
    new_tree.diff()
    text = new_tree.printexp()
    final_form = ''
    n = 0
    while n < len(text):
        try:
            int(text[n])
            if int(text[n]) >= 0:
                final_form = final_form[:-1]+text[n]
                n += 2
            else:
                final_form += text[n]
                n += 1
        except:
            if text[n] == operand:
                final_form = final_form[:-1]+text[n]
                n += 2
            elif text[n] in ['sin', 'cos', 'exp', 'ln']:
                current = text[n:].index(')') + n
                start_count = text[n:current].count('(')
                while start_count > 0:
                    previous = current
                    current += text[current:].index(')')+1
                    start_count -= 1
                    start_count += text[previous:current].count('(')
                text[current] = ''
                final_form = final_form[:-1]+text[n]
                n += 1
            else:
                final_form += text[n]
                n += 1
    return final_form

if __name__ == "__main__":
    print('(((3+5)*4)*sin(x+1))', '\nx')
    tree = parse_tree('(((3+5)*4)*sin(x+1))', 'x')
    print(diff_exp(tree, 'x'))
    print('----------------------------------------')
    print('(exp(a+5)*4)', '\na')
    tree1 = parse_tree('(exp(a+5)*4)', 'a')
    print(diff_exp(tree1, 'a'))
    print('----------------------------------------')
    print('(4*cos(y+5))', '\ny')
    tree2 = parse_tree('(4*cos(y+5))', 'y')
    print(diff_exp(tree2, 'y'))
    print('--------------------')
    print('ln(5*n)', '\nn')
    tree3 = parse_tree('ln(5*n)', 'n')
    print(diff_exp(tree3, 'n'))