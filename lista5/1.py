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

    @param n: (int) size of the array
    @param numbers: (int) positive range of the random numbers
    @return: (float) time taken to solve
    """
    #--------------------checking data--------------------------
    if not isinstance(n, int) or not isinstance(numbers, int):
        raise TypeError('type of given data is incorrect')
    if n<2 or numbers<=2:
        raise ValueError('value of given data is incorrect')
    #-----------------------------------------------------------
    A = np.array([[random.randint(2,numbers) for j in range(n)] for i in range(n)])
    B = np.array([random.randint(2, numbers) for i in range(n)])
    start = time.process_time()
    linalg.solve(A,B)
    end = time.process_time()
    time1= end-start
    return time1

def no_file(base, name):
    """
    Create a file

    @param base: (list) data to calculate from (timing it) 
    @param name: (str) name of the file to be created
    """
    #--------------------checking data--------------------------
    if not isinstance(base, list) and not isinstance(name, str):
        raise TypeError('type of given data is incorrect')
    for i in base:
        if not isinstance(i, int) and not isinstance(i, float):
            raise TypeError('type of given data is incorrect')
    if not name[-4:] == '.txt':
        raise ValueError('name of the file is incorrect')
    #-----------------------------------------------------------
    data_time = [solve_random(i) for i in base]
    file = open(name,'w')
    file.write(str(data_time))

def get_data(base, name):
    """
    Get data from file
    @param base: (list) data to calculate from (only needed if file does not exist) 
    @param name: (str) name of the file to get data from
    @return: (list) wanted data (time)
    """
    #--------------------checking data--------------------------
    if not isinstance(base, list) and not isinstance(name, str):
        raise TypeError('type of given data is incorrect')
    for i in base:
        if not isinstance(i, int) and not isinstance(i, float):
            raise TypeError('type of given data is incorrect')
    if not name[-4:] == '.txt':
        raise ValueError('name of the file is incorrect')
    #-----------------------------------------------------------
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
    #-------------------trial data----------------------------
    data_size1 = [100, 200, 500, 1000, 1500, 2000, 3000, 3500]
    data_time1 = get_data(data_size1, 'data1.txt')
    
    for i in range(len(data_size1)):
        print(data_size1[i], ': \t', data_time1[i])
  
    plt.scatter(data_size1, data_time1)
    plt.yticks([0,1,2,5,10,15,20,30,35])
    plt.title('trial data and time')
    plt.show()
    
    plt.loglog(data_size1, data_time1,'ro')
    plt.title('log trial data and time')
    plt.show()
    #------------------double data-----------------------------
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
    
    print('\n N \t T \t \t Ratio \t \t \t Log')
    for i in range(len(data_size2)):
        print(data_size2[i], '\t', data_time2[i], '\t', ratio[i], '\t', log_ratio[i])
    #-----------------------factors (a and b)-------------------
    b = (sum(log_ratio[1:])-log_ratio[3])/(len(log_ratio)-2)
    print('\nb: \t', b)
    a = data_time2[-1]/(data_size2[-1]**1.1)
    print('a: \t', a)
    #-----------------------fitting a curve-------------------------
    plt.scatter(data_size2, data_time2)
    plt.plot(range(1,9000), [a*i**1.1 for i in range(1,9000)])
    plt.title('fitting a curve')
    plt.show()

    plt.loglog(data_size2, data_time2,'ro')
    plt.loglog(range(100,9000), [a*i**1.1 for i in range(100,9000)])
    plt.title('log fitting a curve')
    plt.show()

    plt.scatter(data_size1, data_time1)
    plt.plot(range(1,4000), [a*i**1.1 for i in range(1,4000)])
    plt.yticks([0,1,2,5,10,15,20,30,35])
    plt.title('checking the curve for trial data')
    plt.show()