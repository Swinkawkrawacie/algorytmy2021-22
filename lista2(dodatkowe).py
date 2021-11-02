#!/usr/bin/env python

import math
from matplotlib import pyplot as plt
import numpy as np

def f1(x):
    return (x**0.999999)*math.log(x)

def f2(x):
    return 10000000*x

def f3(x):
    return 1.000001**x

def f4(x):
    return x**2

def f5(x):
    return 2**(100*x)

def f6(x):
    return math.factorial(x)/(2*math.factorial(x-2))

def f7(x):
    return x*math.sqrt(x)

def f8(x):
    return x**(math.sqrt(x))

def f9(x):
    return 2**x

def f10(x):
    return x**10*2**(x/2)

def f11(x):
    return sum(i+1 for i in range(x+1))

if __name__ == '__main__':
    #first group
    x = np.arange(100000.,100000000.,100)
    
    plt.plot(x, [f1(i) for i in x], "r", label="f1")
    plt.plot(x, [f2(i) for i in x], "b", label="f2")
    plt.plot(x, [f3(i) for i in x], "g", label="f3")
    plt.plot(x, [f4(i) for i in x], "y", label="f4")
    
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(x, [f1(i) for i in x], "r", label="f1")
    plt.plot(x, [f2(i) for i in x], "b", label="f2")
    plt.plot(x, [f4(i) for i in x], "y", label="f4")

    plt.legend()
    plt.grid()
    plt.show()

    #second group
    x = range(2,10)

    plt.plot(x, [f5(i) for i in x], "r", label="f1")
    plt.plot(x, [f6(i) for i in x], "b", label="f2")
    plt.plot(x, [f7(i) for i in x], "g", label="f3")

    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(x, [f6(i) for i in x], "b", label="f2")
    plt.plot(x, [f7(i) for i in x], "g", label="f3")

    plt.legend()
    plt.grid()
    plt.show()

    #third group
    x = range(400,500)

    plt.plot(x, [f8(i) for i in x], "r", label="f1")
    plt.plot(x, [f9(i) for i in x], "b", label="f2")
    plt.plot(x, [f10(i) for i in x], "g", label="f3")
    plt.plot(x, [f11(i) for i in x], "y", label="f4")

    plt.legend()
    plt.grid()
    plt.show()

    x = range(1,30)

    plt.plot(x, [f8(i) for i in x], "r", label="f1")
    plt.plot(x, [f10(i) for i in x], "b", label="f3")
    plt.plot(x, [f11(i) for i in x], "y", label="f4")

    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(x, [f1(i) for i in x], "r", label="f1")
    plt.plot(x, [f4(i) for i in x], "y", label="f4")

    plt.legend()
    plt.grid()
    plt.show()