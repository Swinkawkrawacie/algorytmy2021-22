#!/usr/bin/env python

class parse_tree():
    def __init__(self, text):
        operator_list = []
        while text != '':
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
        self.build_tree()

    def build_tree(self):

        for i in range(len(self.text)):
            if self.text[i] == '(':
                self.left = parse_tree(self.text[i+1:])
            elif self.text[i] in ['+','-','*','/','^']:
                self.data = self.text[i]
                self.right = parse_tree(self.text[i+1:])
            elif self.text[i] in ['sin', 'cos', 'exp', 'ln']:
                self.data = self.text[i]
                self.left = parse_tree(self.text[i+1:])
                self.right = None
                #i need this current previous stuff


if __name__ == "__main__":
    pass