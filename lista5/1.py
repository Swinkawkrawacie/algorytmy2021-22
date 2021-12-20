#!/usr/bin/env python 

import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg
import time
import math
import os

def solve_random(n):
    """
    Time linalg.solve for n variables

    @param n: (int) size of the array
    @param numbers: (int) positive range of the random numbers
    @return: (float) time taken to solve
    """
    #--------------------checking data--------------------------
    if not isinstance(n, int):
        raise TypeError('type of given data is incorrect')
    if n<2:
        raise ValueError('value of given data is incorrect')
    #-----------------------------------------------------------
    A = np.random.random((n,n))
    B = np.array(range(n))
    start = time.process_time()
    linalg.solve(A,B)
    end = time.process_time()
    time1= end-start
    print(time1)
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
    data_size1 = [1000, 1500, 2000, 3000, 3500, 4000, 4500, 5000]
    data_time1 = get_data(data_size1, 'data1.txt')
    
    for i in range(len(data_size1)):
        print(data_size1[i], ': \t', data_time1[i])
  
    plt.scatter(data_size1, data_time1)
    plt.yticks([0,10,15,20,30,35,40,45,50])
    plt.title('trial data and time')
    plt.show()
    
    plt.loglog(data_size1, data_time1,'ro')
    plt.title('log trial data and time')
    plt.show()
    #------------------double data-----------------------------
    #-------------///////A\\\\\\\--------------------
    data_size2a = [2**(9+i) for i in range(5)]
    data_time2a = get_data(data_size2a, 'data2a.txt')
    
    ratio = [None]*len(data_time2a)
    for i in range(1,len(data_time2a)):
        if data_time2a[i-1] != 0:
            ratio[i] = data_time2a[i]/data_time2a[i-1]
    log_ratio = [None]*len(ratio)
    for i in range(len(ratio)):
        if ratio[i] != None:
            log_ratio[i] = math.log(ratio[i],2)
    
    print('\n N \t T \t \t Ratio \t \t \t Log')
    for i in range(len(data_size2a)):
        print(data_size2a[i], '\t', data_time2a[i], '\t', ratio[i], '\t', log_ratio[i])
    #-----------------------factors (a and b)-------------------
    count = 0
    sum1 = 0
    for i in log_ratio:
        if i != None:
            sum1 += i
            count += 1
    b = sum1/count
    print('\nb: \t', b)
    a = 0
    a = data_time2a[-1]/(data_size2a[-1]**b)
    print('a: \t', a)
    #-----------------------fitting a curve-------------------------
    plt.scatter(data_size2a, data_time2a)
    plt.plot(range(1,16000), [a*i**b for i in range(1,16000)])
    plt.title('fitting a curve')
    plt.show()

    plt.loglog(data_size2a, data_time2a,'ro')
    plt.loglog(range(100,16000), [a*i**b for i in range(100,16000)])
    plt.title('log fitting a curve')
    plt.show()

    #-------------///////B\\\\\\\--------------------
    data_size2b = [2**(10+i) for i in range(5)]
    data_time2b = get_data(data_size2b, 'data2b.txt')
    
    ratio = [None]*len(data_time2b)
    for i in range(1,len(data_time2b)):
        if data_time2b[i-1] != 0:
            ratio[i] = data_time2b[i]/data_time2b[i-1]
    log_ratio = [None]*len(ratio)
    for i in range(len(ratio)):
        if ratio[i] != None:
            log_ratio[i] = math.log(ratio[i],2)
    
    print('\n N \t T \t \t Ratio \t \t \t Log')
    for i in range(len(data_size2b)):
        print(data_size2b[i], '\t', data_time2b[i], '\t', ratio[i], '\t', log_ratio[i])
    #-----------------------factors (a and b)-------------------
    count = 0
    sum1 = 0
    for i in log_ratio:
        if i != None:
            sum1 += i
            count += 1
    b = sum1/count
    print('\nb: \t', b)
    a = data_time2b[-1]/(data_size2b[-1]**b)
    print('a: \t', a)
    #-----------------------fitting a curve-------------------------
    plt.scatter(data_size2b, data_time2b)
    plt.plot(range(1,17000), [a*i**b for i in range(1,17000)])
    plt.title('fitting a curve')
    plt.show()

    plt.loglog(data_size2b, data_time2b,'ro')
    plt.loglog(range(100,16000), [a*i**b for i in range(100,16000)])
    plt.title('log fitting a curve')
    plt.show()

    #-------------///////2\\\\\\\--------------------
    plt.scatter(data_size1, data_time1, marker = 'o', color = 'r')
    plt.plot(range(1,5000), [a*i**2 for i in range(1,5000)])
    plt.title('trial for 2')
    plt.show()