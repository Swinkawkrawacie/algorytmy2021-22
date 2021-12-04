#!/usr/bin/env python 

import os.path

class stack():

    def __init__(self):
        self.list_of_items = []
    
    def push(self, item):
        self.list_of_items.append(item)
    
    def pop(self):
        return self.list_of_items.pop()
    
    def peek(self):
        return self.list_of_items[len(self.list_of_items)-1]
    
    def isEmpty(self):
        return self.list_of_items == []
    
    def size(self):
        return len(self.list_of_items)

def checking_HTML_correctness(filename):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    if not os.path.exists(filename):
        raise ValueError('given file does not exist')
    file_obj = open(filename, 'r')
    text = file_obj.read()
    single = ['!DOCTYPE', 'meta', 'link', 'img', 'br', 'hr']
    indicators = stack()

    text_comments = str(text).split('-->')
    for i in range(len(text_comments)-1):
        if text_comments[i].count('<!--') != 1:
            return False
        else:
            index = text_comments[i].find('<!--')
            text_comments[i] = text_comments[i][:index]
    text_no_comments = ''.join(text_comments)

    
    text = str(text_no_comments).split('>')[:-1]
    for i in text:
        if i.count('<') != 1:
            return False
    for i in text:
        position = i.find('<')
        if position+1<len(i):
            if i[position+1] == '/':
                if position+2<len(i):
                    if ' ' in i[position+1:]:
                        end = i[position+1:].find(' ')
                        word = i[position+1:position+end+1]
                        if not (word in single):
                            if indicators.isEmpty():
                                return False
                    else:
                        word = i[position+1:]
                    
                    if not (word in single):
                        if not (word == '/' + indicators.peek()):
                            return False
                        else:
                            indicators.pop()
                else:
                    return False
            else:
                if ' ' in i[position+1:]:
                    end = i[position+1:].find(' ')
                    word = i[position+1:position+end+1]
                else:
                    word = i[position+1:]
                if not (word in single):
                    indicators.push(word)
        else:
            return False
    
    if indicators.isEmpty():
        return True
    else:
        return False
