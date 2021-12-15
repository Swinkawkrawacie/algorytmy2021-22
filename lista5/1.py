#!/usr/bin/env python 

import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg
import random
import time
import math

def solve_random(n, numbers=5):
    """
    Time linalg.solve for n variables
    """
    A = np.array([[random.randint(2,numbers) for j in range(n)] for i in range(n)])
    B = np.array([random.randint(2, numbers) for i in range(n)])
    start = time.time()
    linalg.solve(A,B)
    end = time.time()
    time1= end-start
    if time1<=0:
        solve_random(n)
    return time1

if __name__=='__main__':

    data_size = [2**(4+i) for i in range(10)]
    data_time = [solve_random(i) for i in data_size]
    ratio = [None]*len(data_time)
    for i in range(1,len(data_time)):
        ratio[i] = data_time[i]/data_time[i-1]
    log_ratio = [None]
    for i in range(1, len(ratio)):
        log_ratio.append(math.log(ratio[i]))
    
    print('N \t T \t \t Ratio \t Log')
    for i in range(len(data_size)):
        print(data_size[i], '\t', data_time[i], '\t \t', ratio[i], '\t', log_ratio[i])