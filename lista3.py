#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np

#Horner's method
def calc_value(factors, x):
    """
    Calculate value of polynomial for x

    @param factors: (list) factors in the polynomial (from x^0 to x^n)
    @param x: (int/float) a value to calculate the polynomial for
    @return: (list) the value of the polynomial for x and the amount of multiplications needed to complete the task in a form of a list
    """
    if not isinstance(factors,list) or not (isinstance(x, int) or isinstance(x, float)):
        raise TypeError('given data is incorrect')
    
    factors = factors[::-1]
    result = 0
    k = 0
    for i in factors[:-1]:
        result = (result+i)*x
        k += 1
    result += factors[-1]
    return [result,k]
    
def text_read(name):
    """
    Count the characters in the given text

    @name: (str) name of the file
    @return: (dict) cout of the occurrence of every character in the text in a form of a dictionary
    """
    #checking if the file exists
    try:
        file = open(name,'r')
    except:
        raise ValueError('given file does not exist')
    
    text = file.read()
    characters = set(str(text))
    
    #removing spaces and blanks
    try:
        characters.remove(' ')
    except:
        pass

    try:
        characters.remove("\n")
    except:
        pass

    try:
        characters.remove("\t")
    except:
        pass

    char_dict = {}

    for i in characters:
        char_dict[i]=text.count(i)

    for i in range(ord('A'), ord('Z')+1):
        try:
            char_dict[chr(i)] += char_dict.get(chr(i+32))
            char_dict.__delitem__(chr(i+32))
        except:
            try:
                p = char_dict[chr(i+32)]
                char_dict[chr(i)] = p
                char_dict.__delitem__(chr(i+32))
            except:
                pass

    return char_dict


if __name__ == '__main__':
    
    #first exercise
    
    #second exercise    
    print(calc_value([1,2,3,4,5,6],1))
    print(calc_value([1,2,3,4,5,6,7],7))

    #the amount of multiplications needed = n-1

    #third exercise
    x = text_read('narniaeng.txt')
    a = sorted(x.keys())
    b = []
    for i in a:
        b.append(x[i])
    plt.bar(a, b)
    plt.show()
