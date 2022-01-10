#!/usr/bin/env python 

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

if __name__ == "__main__":
    new_list = heap_sort([9,3,1,4,0,2])
    print(new_list)