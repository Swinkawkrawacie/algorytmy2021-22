#!/usr/bin/env python

import math
from matplotlib import pyplot as plt
import numpy as np

def find_abc1(n:int):
    k=0
    existance=False
    for a in range(n):
        k+=1
        for b in range(n):
            k+=1
            for c in range(n):
                k+=14
                if a**2+b**2==c**2 and a+b+c==n and a!=b and b!=c:
                    existance = True
                    return [existance,a,b,c,k]
    a,b,c=-1,-1,-1
    return [existance,a,b,c,k]

def find_abc2(n:int):
    k=0
    existance=False
    for a in range(round(n/2)+1):
        k+=1
        for b in range(round(n/2)+1):
            k+=1
            for c in range(round(n/2)+1):
                k+=14
                if a**2+b**2==c**2 and a+b+c==n and a!=b and b!=c:
                    existance = True
                    return [existance,a,b,c,k]
    a,b,c=-1,-1,-1
    return [existance,a,b,c,k]

def find_abc3(n:int):
    k=0
    existance=False
    for a in range(round(n/2)+1):
        k+=1
        for b in range(a+1,round(n/2)+1):
            k+=1
            for c in range(b+1,round(n/2)+1):
                k+=10
                if a**2+b**2==c**2 and a+b+c==n:
                    existance = True
                    return [existance,a,b,c,k]
    a,b,c=-1,-1,-1
    return [existance,a,b,c,k]

def find_abc4(n:int):
    k=0
    existance=False
    for a in range(round(n/2)+1):
        k+=1
        for b in range(a+1,round(n/2)+1):
            c=n-a-b
            k+=10
            if a**2+b**2==c**2 and b!=c:
                existance = True
                return [existance,a,b,c,k]
    a,b,c=-1,-1,-1
    return [existance,a,b,c,k]

def find_abc5(n:int):
    k=0
    existance=False
    for c in range(math.ceil(n*math.sqrt(2)-n),round(n/2)+1):
        ab_sub = math.sqrt(c**2-n**2+2*c*n)
        k+=9
        if math.floor(ab_sub) == ab_sub:
            b = int((n-c+ab_sub)/2)
            a = int(n-c-b)
            k+=8
            if a!=0 and b!=0:
                existance = True
                return [existance,a,b,c,k]
    a,b,c=-1,-1,-1
    return [existance,a,b,c,k]

if __name__ == '__main__':
    print(find_abc1(1000))
    print(find_abc1(12))
    print(find_abc1(11))
    print('-------------')
    print(find_abc2(1000))
    print(find_abc2(12))
    print(find_abc2(11))
    print('-------------')
    print(find_abc3(1000))
    print(find_abc3(12))
    print(find_abc3(11))
    print('-------------')
    print(find_abc4(1000))
    print(find_abc4(12))
    print(find_abc4(11))
    print('-------------')
    print(find_abc5(1000))
    print(find_abc5(12))
    print(find_abc5(11))

    x = [i for i in range(1,6)]
    y = [find_abc1(1000)[4],find_abc2(1000)[4],find_abc3(1000)[4],find_abc4(1000)[4],find_abc5(1000)[4]]
    plt.scatter(x,y)
    plt.grid()
    plt.show()

    y = [find_abc1(11)[4],find_abc2(11)[4],find_abc3(11)[4],find_abc4(11)[4],find_abc5(11)[4]]
    plt.scatter(x,y)
    plt.grid()
    plt.show()

    y = [find_abc1(12)[4],find_abc2(12)[4],find_abc3(12)[4],find_abc4(12)[4],find_abc5(12)[4]]
    plt.scatter(x,y)
    plt.grid()
    plt.show()