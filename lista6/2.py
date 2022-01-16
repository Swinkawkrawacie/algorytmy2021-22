#!/usr/bin/env python 

import time
import random
import os
import  math
from matplotlib import pyplot as plt

class BinHeap:
    """
    Binary heap
    """
    def __init__(self):
        self.elements = [0]
        self.heap_size = 0
        
    def percUp(self,index):
        """
        Get newly added element in the proper position (from the bottom)

        @param index (int) starting index
        """
        #------------------checking data--------------------
        if not isinstance(index, int):
            raise TypeError('index should be an integer')
        if index > self.heap_size:
            raise ValueError('index out of range')
        #---------------------------------------------------
        while index // 2 > 0:
            if self.elements[index] < self.elements[index // 2]:
                old = self.elements[index // 2]
                self.elements[index // 2] = self.elements[index]
                self.elements[index] = old
            index = index // 2      
        
    def insert(self,value):
        """
        Insert value

        @param value: (int) value to insert
        """
        #------------------checking data--------------------
        if not isinstance(value, int):
            raise TypeError('value should be an integer')
        #---------------------------------------------------
        self.elements.append(value)
        self.heap_size = self.heap_size + 1
        self.percUp(self.heap_size)        
        
    def findMin(self):
        """
        Find minimal element on the tree

        @return: (int) the minimal value
        """
        return self.elements[1]

    def percDown(self,index):
        """
        Get newly added element in the proper position (from the top)

        @param index (int) starting index
        """
        #------------------checking data--------------------
        if not isinstance(index, int):
            raise TypeError('index should be an integer')
        if index < 0:
            raise ValueError('index out of range')
        #---------------------------------------------------
        while (index * 2) <= self.heap_size:
            smaller_child = self.minChild(index)
            if self.elements[index] > self.elements[smaller_child]:
                old = self.elements[index]
                self.elements[index] = self.elements[smaller_child]
                self.elements[smaller_child] = old
            index = smaller_child

    def minChild(self,index):
        """
        Find an index of a smaller child of the element with the given index

        @return: (int) the index of the smaller child
        """
        #------------------checking data--------------------
        if not isinstance(index, int):
            raise TypeError('index should be an integer')
        if index < 0 or index > self.heap_size:
            raise ValueError('index out of range')
        #---------------------------------------------------
        if index * 2 + 1 > self.heap_size:
            return index * 2
        else:
            if self.elements[index*2] < self.elements[index*2+1]:
                return index * 2
            else:
                return index * 2 + 1    
            
    def delMin(self):
        """
        Delete the minimal element

        @return: (int) the deleted minimal value
        """
        min_value = self.elements[1]
        self.elements[1] = self.elements[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.elements.pop()
        self.percDown(1)
        return min_value           
    
    def buildHeap(self,data_list):
        """
        Build heap from the list

        @param data_list: (list) list to build the heap from
        """
        #------------------checking data--------------------
        if not isinstance(data_list, list):
            raise TypeError('data_list should be a list')
        #---------------------------------------------------
        index = len(data_list) // 2
        self.heap_size = len(data_list)
        self.elements = [0] + data_list[:]
        while index > 0:
            self.percDown(index)
            index = index - 1    
            
    def size(self):
        """
        Get size of the heap

        @return: (int) size of the heap
        """
        return self.heap_size
    
    def isEmpty(self):
        """
        Check if the heap is empty

        @return: (bool) True/False if the heap is empty/not empty
        """
        return self.heap_size == 0
    
    def __str__(self):
        return str(self.elements[1:])
    
def heap_sort(data_list):
    """
    Sort the list using a heap

    @param data_list: (list) list to sort
    @return: (list) sorted list
    """
    #------------------checking data--------------------
    if not isinstance(data_list, list):
        raise TypeError('data_list should be a list')
    #---------------------------------------------------
    sorted_list = []
    heap = BinHeap()
    heap.buildHeap(data_list)
    for i in range(len(data_list)):
        sorted_list.append(heap.delMin())
    return sorted_list

def time_sort(n):
    """
    Measure time of sorting

    @param n: (int) amount of elements on the list

    @return: (float) time of the operation
    """
    if not isinstance(n, int):
        raise TypeError('amount of elements on the list needs to be an integer')
    if n <= 0:
        raise ValueError('amount of elements on the list needs to be positive')
    data = [random.randint(-100,100) for i in range(n)]
    start = time.process_time()
    heap_sort(data)
    end = time.process_time()
    return end-start

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
    data_time = [time_sort(i) for i in base]
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

if __name__ == "__main__":
    #-----------------------sorting----------------------------------
    print([2,0,9,7,0,8,5,8,2,3,1])
    print(heap_sort([2,0,9,7,0,8,5,8,2,3,1]))
    print([20,10,-9,-7,0,-8,5,8,2,3,100])
    print(heap_sort([20,10,-9,-7,0,-8,5,8,2,3,100]))
    #-----------------------trial data-------------------------------
    data_size1 = [10000, 15000, 20000, 30000, 35000, 40000, 45000, 50000]
    data_time1 = get_data(data_size1, 'data1.txt')
    for i in range(len(data_size1)):
        print(data_size1[i], ': \t', data_time1[i])
  
    plt.scatter(data_size1, data_time1)
    plt.yticks([0,1,1.5,2,3,3.5,4,4.5,5])
    plt.title('trial data and time')
    plt.show()
    
    plt.loglog(data_size1, data_time1,'ro')
    plt.title('log trial data and time')
    plt.show()

    #-----------------------double data-------------------------------
    #-------------------------///1\\\---------------------------------
    data_size2_1 = [2**(8+i) for i in range(10)]
    data_time2_1 = get_data(data_size2_1, 'data2_1.txt')

    ratio = [None]*len(data_time2_1)
    for i in range(1,len(data_time2_1)):
        if data_time2_1[i-1] != 0:
            ratio[i] = data_time2_1[i]/data_time2_1[i-1]
    log_ratio = [None]*len(ratio)
    for i in range(len(ratio)):
        if ratio[i] != None:
            log_ratio[i] = math.log(ratio[i],2)
    
    print('\n N \t T \t \t Ratio \t \t \t Log')
    for i in range(len(data_size2_1)):
        print(data_size2_1[i], '\t', data_time2_1[i], '\t', ratio[i], '\t', log_ratio[i])
    
    #-----------------------factors (a and b)-------------------
    count = 0
    sum1 = 0
    for i in log_ratio:
        if i != None:
            sum1 += i
            count += 1
    b1 = sum1/count
    print('\nb: \t', b1)
    a1 = 0
    a1 = data_time2_1[-1]/(data_size2_1[-1]**b1)
    print('a: \t', a1)
    #-----------------------fitting a curve-------------------------
    plt.scatter(data_size2_1, data_time2_1)
    plt.plot(range(1,140000), [a1*i**b1 for i in range(1,140000)])
    plt.title('fitting a curve')
    plt.show()

    plt.loglog(data_size2_1, data_time2_1,'ro')
    plt.loglog(range(100,160000), [a1*i**b1 for i in range(100,160000)])
    plt.title('log fitting a curve')
    plt.show()
    #-------------------------///2\\\---------------------------------
    data_size2_2 = [2**(12+i) for i in range(10)]
    data_time2_2 = get_data(data_size2_2, 'data2_2.txt')

    ratio = [None]*len(data_time2_2)
    for i in range(1,len(data_time2_2)):
        if data_time2_2[i-1] != 0:
            ratio[i] = data_time2_2[i]/data_time2_2[i-1]
    log_ratio = [None]*len(ratio)
    for i in range(len(ratio)):
        if ratio[i] != None:
            log_ratio[i] = math.log(ratio[i],2)
    
    print('\n N \t T \t \t Ratio \t \t \t Log')
    for i in range(len(data_size2_2)):
        print(data_size2_2[i], '\t', data_time2_2[i], '\t', ratio[i], '\t', log_ratio[i])
    
    #-----------------------factors (a and b)-------------------
    count = 0
    sum1 = 0
    for i in log_ratio:
        if i != None:
            sum1 += i
            count += 1
    b2 = sum1/count
    print('\nb: \t', b2)
    a2 = 0
    a2 = data_time2_2[-1]/(data_size2_2[-1]**b2)
    print('a: \t', a2)
    #-----------------------fitting a curve-------------------------
    plt.scatter(data_size2_2, data_time2_2)
    plt.plot(range(1,2500000), [a2*i**b2 for i in range(1,2500000)])
    plt.title('fitting a curve')
    plt.show()

    plt.loglog(data_size2_2, data_time2_2,'ro')
    plt.loglog(range(100,2500000), [a2*i**b2 for i in range(100,2500000)])
    plt.title('log fitting a curve')
    plt.show()
    #-------------------------///3\\\---------------------------------
    data_size3 = [2**(12+i) for i in range(10)]
    data_time3 = get_data(data_size3, 'data3.txt')

    ratio = [None]*len(data_time3)
    for i in range(1,len(data_time3)):
        if data_time3[i-1] != 0:
            ratio[i] = data_time3[i]/data_time3[i-1]
    log_ratio = [None]*len(ratio)
    for i in range(len(ratio)):
        if ratio[i] != None:
            log_ratio[i] = math.log(ratio[i],2)
    
    print('\n N \t T \t \t Ratio \t \t \t Log')
    for i in range(len(data_size3)):
        print(data_size3[i], '\t', data_time3[i], '\t', ratio[i], '\t', log_ratio[i])
    
    #-----------------------factors (a and b)-------------------
    count = 0
    sum1 = 0
    for i in log_ratio:
        if i != None:
            sum1 += i
            count += 1
    b3 = sum1/count
    print('\nb: \t', b3)
    a3 = 0
    a3 = data_time3[-1]/(data_size3[-1]**b2)
    print('a: \t', a3)
    #-----------------------fitting a curve-------------------------
    plt.scatter(data_size3, data_time3)
    plt.plot(range(1,2500000), [a3*i**b3 for i in range(1,2500000)])
    plt.title('fitting a curve')
    plt.show()

    plt.loglog(data_size3, data_time3,'ro')
    plt.loglog(range(100,2500000), [a3*i**b3 for i in range(100,2500000)])
    plt.title('log fitting a curve')
    plt.show()