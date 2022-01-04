#!/usr/bin/env python 

class MaxBinHeap:
    def __init__(self, max_size):
        self.elements = [0]
        self.heap_size = 0
        self.max_size = max_size
        
    def percUp(self,index):
        """
        index - starting index
        """
        while index // 2 > 0:
            if self.elements[index] < self.elements[index // 2]:
                old = self.elements[index // 2]
                self.elements[index // 2] = self.elements[index]
                self.elements[index] = old
            index = index // 2      
        
    def insert(self,value):
        """
        value to insert
        """
        if self.heap_size < self.max_size:
            self.elements.append(value)
            self.heap_size = self.heap_size + 1
            self.percUp(self.heap_size)
        else:
            if self.findMin() < value:
                self.delMin()
                self.insert(value)     
        
    def findMin(self):
        return self.elements[1]

    def percDown(self,index):
        """
        index - starting index
        """
        while (index * 2) <= self.heap_size:
            smaller_child = self.minChild(index)
            if self.elements[index] > self.elements[smaller_child]:
                old = self.elements[index]
                self.elements[index] = self.elements[smaller_child]
                self.elements[smaller_child] = old
            index = smaller_child

    def minChild(self,index):
        if index * 2 + 1 > self.heap_size:
            return index * 2
        else:
            if self.elements[index*2] < self.elements[index*2+1]:
                return index * 2
            else:
                return index * 2 + 1    
            
    def delMin(self):
        min_value = self.elements[1]
        self.elements[1] = self.elements[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.elements.pop()
        self.percDown(1)
        return min_value           
    
    def buildHeap(self,data_list):
        if len(data_list) > self.max_size:
            self.buildHeap(data_list[:self.max_size])
            for i in data_list[self.max_size:]:
                self.insert(i)
        else:
            index = len(data_list) // 2
            self.heap_size = len(data_list)
            self.elements = [0] + data_list[:]
            while index > 0:
                self.percDown(index)
                index = index - 1    
            
    def size(self):
        return self.heap_size
    
    def isEmpty(self):
        return self.heap_size == 0
    
    def __str__(self):
        return str(self.elements[1:])

if __name__ == "__main__":
    heap = MaxBinHeap(7)
    heap.buildHeap([4,7,2,8,0,6,3,12,7,5])
    print(heap)