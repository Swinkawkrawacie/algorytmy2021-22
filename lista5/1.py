#!/usr/bin/env python 

import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg
import random
import time
import math
import os

def solve_random(n, numbers=10):
    """
    Time linalg.solve for n variables
    """
    A = np.array([[random.randint(2,numbers) for j in range(n)] for i in range(n)])
    B = np.array([random.randint(2, numbers) for i in range(n)])
    start = time.process_time()
    linalg.solve(A,B)
    end = time.process_time()
    time1= end-start
    return time1

def no_file(base:list, name:str):
    data_time = [solve_random(i) for i in base]
    file = open(name,'w')
    file.write(str(data_time))
    return None

def get_data(base, name):
    
    if not os.path.isfile(name):
        no_file(base, name)
    try:
        data_time = eval(open(name,'r').read())
    except:
        raise ValueError('incorrect contents of the file')
    if isinstance(data_time, list):
        return data_time
    else:
        raise ValueError('incorrect contents of the file')

if __name__=='__main__':
    data_size1 = [100, 200, 500, 1000, 1500, 2000, 3000, 3500]
    data_time1 = get_data(data_size1, 'data1.txt')
    
    for i in range(len(data_size1)):
        print(data_size1[i], ': \t', data_time1[i])
  
    plt.scatter(data_size1, data_time1)
    plt.yticks([0,1,2,5,10,15,20,30,35])
    plt.show()
    
    plt.loglog(data_size1, data_time1,'ro')
    plt.show()
    
    data_size2 = [2**(7+i) for i in range(7)]
    data_time2 = get_data(data_size2, 'data2.txt')
    ratio = [None]*len(data_time2)
    for i in range(1,len(data_time2)):
        if data_time2[i-1] != 0:
            ratio[i] = data_time2[i]/data_time2[i-1]
    log_ratio = [None]*len(ratio)
    for i in range(len(ratio)):
        if ratio[i] != None:
            log_ratio[i] = math.log(ratio[i],2)
    
    print('N \t T \t \t \t Ratio \t \t \t Log')
    for i in range(len(data_size2)):
        print(data_size2[i], '\t', data_time2[i], '\t', ratio[i], '\t', log_ratio[i])

    b = (sum(log_ratio[1:])-log_ratio[3])/(len(log_ratio)-2)
    print('b: \t', b)
    a = data_time2[-1]/(data_size2[-1]**1.1)
    print('a: \t', a)
    plt.scatter(data_size2, data_time2)
    plt.plot(range(1,9000), [a*i**1.1 for i in range(1,9000)])
    plt.show()

    plt.loglog(data_size2, data_time2,'ro')
    plt.loglog(range(100,9000), [a*i**1.1 for i in range(100,9000)])
    plt.show()

    plt.scatter(data_size1, data_time1)
    plt.plot(range(1,4000), [a*i**1.1 for i in range(1,4000)])
    plt.yticks([0,1,2,5,10,15,20,30,35])
    plt.show()