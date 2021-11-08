#!/usr/bin/env python

def ordinary_polynomial_value_calc(coeff, arg):
    #---------checking-given-data----------------------------------
    if not isinstance(coeff,list) or not (isinstance(arg, int) or isinstance(arg, float)):
        raise TypeError('incorrect type of given data')
    #---------------------------------------------------------------
    value = coeff[0]
    count_mult = 0
    count_add = 0
    for i in range(1,len(coeff)):
        value += coeff[i]*arg**i
        count_mult += i
        count_add += 1
    return value, count_mult, count_add
  
def smart_polynomial_value_calc(coeff, arg):
    #---------checking-given-data----------------------------------
    if not isinstance(coeff,list) or not (isinstance(arg, int) or isinstance(arg, float)):
        raise TypeError('incorrect type of given data')
    #---------------------------------------------------------------
    coeff = coeff[::-1]
    value = 0
    count_mult = 0
    count_add = 0
    for i in coeff[:-1]:
        value = (value+i)*arg
        count_mult += 1
        count_add += 1
    value += coeff[-1]
    return value, count_mult, count_add

if __name__ == '__main__':
    
    #second exercise    
    print("-------first--------")
    print(ordinary_polynomial_value_calc([1,2,3,4,5,6],1))
    print(ordinary_polynomial_value_calc([1,2,3,4,5,6,7],7))
    print("-------second--------")
    print(smart_polynomial_value_calc([1,2,3,4,5,6],1))
    print(smart_polynomial_value_calc([1,2,3,4,5,6,7],7))