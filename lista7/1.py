#!/usr/bin/env python 

from gettext import find
import sys

class Queue(object):
    def __init__(self):
        self.list_of_items = []
    
    def enqueue(self, item):
        self.list_of_items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('the queue is empty')
        return self.list_of_items.pop(0)
    
    def is_empty(self):
        return self.list_of_items == []
        
    def size(self):
        return len(self.list_of_items) 

class BinHeap:
    def __init__(self):
        self.elements = [0]
        self.atributes = [0]
        self.heap_size = 0
        
    def percUp(self,index):
        #------------------checking data--------------------
        if not isinstance(index, int):
            raise TypeError('index should be an integer')
        if index > self.heap_size:
            raise ValueError('index out of range')
        #---------------------------------------------------
        while index // 2 > 0:
            if self.elements[index] < self.elements[index // 2]:
                old1 = self.elements[index // 2]
                old2 = self.atributes[index // 2]
                self.elements[index // 2] = self.elements[index]
                self.atributes[index // 2] = self.atributes[index]
                self.elements[index] = old1
                self.atributes[index] = old2
            index = index // 2      
        
    def insert(self,value):
        #------------------checking data--------------------
        if not isinstance(value, tuple):
            raise TypeError('value should be an tuple')
        #---------------------------------------------------
        self.elements.append(value[0])
        self.atributes.append(value[1])
        self.heap_size = self.heap_size + 1
        self.percUp(self.heap_size)        
        
    def findMin(self):
        return (self.elements[1],self.atributes[1])

    def percDown(self,index):
        #------------------checking data--------------------
        if not isinstance(index, int):
            raise TypeError('index should be an integer')
        if index < 0:
            raise ValueError('index out of range')
        #---------------------------------------------------
        while (index * 2) <= self.heap_size:
            smaller_child = self.minChild(index)
            if self.elements[index] > self.elements[smaller_child]:
                old1 = self.elements[index]
                old2 = self.atributes[index]
                self.elements[index] = self.elements[smaller_child]
                self.atributes[index] = self.atributes[smaller_child]
                self.elements[smaller_child] = old1
                self.atributes[smaller_child] = old2
            index = smaller_child

    def minChild(self,index):
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
        min_value = self.elements[1]
        min_atribute = self.atributes[1]
        self.elements[1] = self.elements[self.heap_size]
        self.atributes[1] = self.atributes[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.elements.pop()
        self.atributes.pop()
        self.percDown(1)
        return (min_value,min_atribute)
    
    def buildHeap(self,data_list):
        #------------------checking data--------------------
        if not isinstance(data_list, list):
            raise TypeError('data_list should be a list')
        #---------------------------------------------------
        index = len(data_list) // 2
        self.heap_size = len(data_list)
        self.elements = [0]
        self.atributes = [0]
        for i in data_list:
            self.elements.append(i[0])
        for i in data_list:
            self.atributes.append(i[1])
        while index > 0:
            self.percDown(index)
            index = index - 1    
            
    def size(self):
        return self.heap_size
    
    def isEmpty(self):
        return self.heap_size == 0
    
    def __str__(self):
        return str([(self.elements[i],self.atributes[i]) for i in range(1,self.heap_size)])
    
    def decreaseKey(self, element, new_key):
        if element in self.atributes:
            idx = self.atributes.index(element)
            self.elements[idx] = new_key
            data = []
            for i in range(1,len(self.elements)):
                data.append((self.elements[i],self.atributes[i]))
            self.buildHeap(data)

class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'       
        self.dist = sys.maxsize    
        self.pred = None           
        self.disc = 0              
        self.fin = 0               

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def getEdges(self):
        result = []
        if self.vertList == {}:
            return
        for i in self.vertList.keys():
            for j in self.vertList[i].connectedTo.keys():
                result.append((i,j.id))
        return result

    def graph_dot(self):
        base = self.getEdges()
        result = 'digraph G{'
        for i in base:
            result += str(i[0]) + '->' + str(i[1]) + ';'
        return result + '}'

    def bfs(self,start:Vertex):
        for i in self:
            i.setColor('white')
            i.setDistance(0)
            i.setPred(None)
        start.setDistance(0)                            
        start.setPred(None)                             
        vertQueue = Queue()
        vertQueue.enqueue(start)                        
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()           
            for nbr in currentVert.getConnections():    
                if (nbr.getColor() == 'white'):         
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)   
                    nbr.setPred(currentVert)                         
                    vertQueue.enqueue(nbr)                           
            currentVert.setColor('black')
        
    def traverse(self, y):
        result = []
        if isinstance(y,Vertex):
            x = y
            while x.getPred():
                result.append(x.getId())
                x = x.getPred()
            result.append(x.getId())
            return result[::-1]
        else:
            return  
    
    def dfs(self):
        self.time = 0
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
    
    def sort_top(self):
        self.dfs()
        possible = True
        times = [(i,self.vertList[i].getFinish()) for i in self.vertList.keys()]
        times.sort(reverse=True, key = lambda x: x[1])
        result = []
        for i in times:
            result.append(i[0])
        for i in range(1,len(result)):
            for j in result[:i]:
                if j in [p.id for p in list(self.vertList[result[i]].connectedTo)]:
                    possible = False
        if possible:
            return result
        else:
            raise ValueError('graph is not linear')

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def dijkstra(self,start):
        for i in self:
            i.setDistance(sys.maxsize)
            i.setPred(None)
        pq = BinHeap()
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(),v) for v in self])
        while not pq.isEmpty():
            currentVert = pq.delMin()[1]
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    nextVert.setDistance( newDist )
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert,newDist)

def find_fastest(graph1:Graph, start):
    """
    Find fastest paths to every element from the start

    @graph1: (Graph) graph to analyze
    @start: key to start from
    @return: (dict) dictionary of pairs the key and the path
    """
    if not (start in graph1.vertList.keys()):
        raise ValueError()
    graph1.dijkstra(graph1.getVertex(start))
    result={}
    for i in list(graph1.vertList.keys()):
        if i != start:
            short_path = graph1.traverse(graph1.getVertex(i))
            if len(short_path)>1:
                result[i] = short_path
    if result == {}:
        raise ValueError('there are no connections from this element')
    return result

def mis_can(mis = 3, can = 3):
    """
    Solve the missioniaries and cannibals problem

    @mis: (int) number of missionaries
    @can: (int) number of cannibals
    @return: (list) list of moves to solve the problem
    """
    if not (isinstance(mis,int) and isinstance(can, int)):
        raise TypeError('number of people has to be an integer')
    if mis <=0 or can <=0:
        raise ValueError('number of people has to be positive')
    graph_mis_can = Graph()
    for i in range(4):
        for j in range(4):
            for k in range(2):
                graph_mis_can.addVertex((i,j,k))
    for i in list(graph_mis_can.vertList.keys()):
        if i[2]==1:
            if (i[0]>i[1] and i[0]-1>=0) or i[0]==1:
                graph_mis_can.addEdge(i, (mis+1-i[0],can-i[1],0))
            if (i[0]-1>i[1] and i[0]-2>=0) or i[0]==2:
                    graph_mis_can.addEdge(i, (mis+2-i[0],can-i[1],0))
            if (i[0]>=i[1] and i[0]-1>=0 and i[1]-1>=0) or i[0]==1:
                graph_mis_can.addEdge(i, (mis+1-i[0],can+1-i[1],0))
            if i[1]>0:
                graph_mis_can.addEdge(i, (mis-i[0],can+1-i[1],0))
                if i[1]-1>0:
                    graph_mis_can.addEdge(i, (mis-i[0],can+2-i[1],0))
        else:
            if (i[0]>i[1] and i[0]-1>=0) or i[0]==1:
                graph_mis_can.addEdge(i, (mis+1-i[0],can-i[1],1))
            if (i[0]-1>i[1] and i[0]-2>=0) or i[0]==2:
                    graph_mis_can.addEdge(i, (mis+2-i[0],can-i[1],1))
            if (i[0]>=i[1] and i[0]-1>=0 and i[1]-1>=0) or i[0]==1:
                graph_mis_can.addEdge(i, (mis+1-i[0],can+1-i[1],1))
            if i[1]>0:
                graph_mis_can.addEdge(i, (mis-i[0],can+1-i[1],1))
                if i[1]-1>0:
                    graph_mis_can.addEdge(i, (mis-i[0],can+2-i[1],1))
    graph_mis_can.bfs(graph_mis_can.getVertex((mis,can,1)))
    move_list = graph_mis_can.traverse(graph_mis_can.getVertex((mis,can,0)))
    if len(move_list) <= 1:
        raise ValueError('can\'t calculate from this number')
    
    return move_list

def litres(base1 = 3, base2 = 4, goal = 2):
    """
    Measure given amount of litres

    @base1: (int) capacity of the first container
    @base2: (int) capacity of the second container
    @goal: (int) amount to measure
    @return: (list) list of moves to solve the problem
    """
    graph_litres = Graph()
    for i in range(base1+1):
        for j in range(base2+1):
            graph_litres.addVertex((i,j))
    for i in list(graph_litres.vertList.keys()):
        if i[0]>0:
            graph_litres.addEdge(i, (0,i[1]))
            graph_litres.addEdge(i, (base1,i[1]))
            if i[0]+i[1]<=base2:
                graph_litres.addEdge(i, (0,i[0]+i[1]))
            else:
                graph_litres.addEdge(i, (i[0]+i[1]-base2,base2))
        if i[0]==0:
            graph_litres.addEdge(i, (base1,i[1]))
        if i[1]>0:
            graph_litres.addEdge(i, (i[0],0))
            graph_litres.addEdge(i, (i[0],base2))
            if i[0]+i[1]<=base1:
                graph_litres.addEdge(i, (i[0]+i[1],0))
            else:
                graph_litres.addEdge(i, (base1,i[0]+i[1]-base1))
        if i[1]==0:
            graph_litres.addEdge(i, (i[0],base2))
    graph_litres.bfs(graph_litres.getVertex((0,0)))
    move_list = []
    for i in range(base2+1):
        move_list.append(graph_litres.traverse(graph_litres.getVertex((goal,i))))
    for i in range(base1+1):
        move_list.append(graph_litres.traverse(graph_litres.getVertex((i,goal))))
    move_list.sort(key=lambda x: len(x))
    found = False
    n = 0
    while not found and n<len(move_list):
        if len(move_list[n])>1:
            found = True
            result = move_list[n]
        n += 1

    if found:
        return result
    else:
        raise ValueError('can\'t measure this amount')


if __name__ == '__main__':
    gr1 = Graph()
    for i in range(6):
        gr1.addVertex(i)
    gr1.addEdge(0,1,5)
    gr1.addEdge(0,5,2)
    gr1.addEdge(1,2,4)
    gr1.addEdge(2,3,9)
    gr1.addEdge(3,4,1)
    gr1.addEdge(3,5,3)
    gr1.addEdge(4,0,1)
    gr1.addEdge(4,5,1)
    gr1.addEdge(5,2,1)

    gr2 = Graph()
    for i in range(1,9):
        gr2.addVertex(i)
    gr2.addEdge(1,4)
    gr2.addEdge(2,4)
    gr2.addEdge(3,4)
    gr2.addEdge(4,6)
    gr2.addEdge(4,9)
    gr2.addEdge(5,6)
    gr2.addEdge(6,7)
    gr2.addEdge(7,8)
    gr2.addEdge(9,8)

    #---------------DOT------------------
    print('\ngraph 1:\n')
    print(gr1.graph_dot())
    print('\ngraph 2:\n')
    print(gr2.graph_dot())
    print('\n')
    #---------topological sort-----------
    print('\ngraph 2:\n')
    print(gr2.sort_top())
    print('\ngraph 1:\n')
    print(gr1.sort_top())
    #-------finding short paths----------
    print('\ngraph 1:\nbase: 2\n')
    result1 = find_fastest(gr1, 2)
    for i in result1.keys():
        print(i, ': ', result1[i])
    print('\nbase: 5\n')
    result2 = find_fastest(gr1,5)
    for i in result2.keys():
        print(i, ': ', result2[i])
    print('\ngraph 2:\nbase: 3\n')
    result3 = find_fastest(gr2, 3)
    for i in result3.keys():
        print(i, ': ', result3[i])
    print('\nbase: 8\n')
    result4 = find_fastest(gr2,8)
    for i in result4.keys():
        print(i, ': ', result4[i])
    #----missionaries and cannibals-----
    print('\n')
    print(mis_can())
    #------------measure 2l-------------
    print('\n')
    print(litres())
    
    
