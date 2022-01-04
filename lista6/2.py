#!/usr/bin/env python 

class BinHeap:
    def __init__(self):
        self.elements = [0]
        self.heap_size = 0
        
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
        self.elements.append(value)
        self.heap_size = self.heap_size + 1
        self.percUp(self.heap_size)        
        
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
    
def heap_sort(data_list):
    sorted_list = []
    heap = BinHeap()
    heap.buildHeap(data_list)
    for i in range(len(data_list)):
        sorted_list.append(heap.delMin())
    return sorted_list

if __name__ == "__main__":
    new_list = heap_sort([9,3,1,4,0,2])
    print(new_list)