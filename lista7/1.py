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
        self.color = 'white'       #new: color of node
        self.dist = sys.maxsize    #new: distance from beginning (will be used later)
        self.pred = None           #new: predecessor
        self.disc = 0              #new: discovery time
        self.fin = 0               #new: end-of-processing time

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

    def bfs(self,start:Vertex, weights=False):
        if not weights:
            start.setDistance(0)                            #distance 0 indicates it is a start node
            start.setPred(None)                             #no predecessor at start
            vertQueue = Queue()
            vertQueue.enqueue(start)                        #add start to processing queue
            while (vertQueue.size() > 0):
                currentVert = vertQueue.dequeue()           #pop next node to process -> current node
                for nbr in currentVert.getConnections():    #check all neighbors of the current node
                    if (nbr.getColor() == 'white'):         #if the neighbor is white
                        nbr.setColor('gray')
                        nbr.setDistance(currentVert.getDistance() + 1)   #set its distance
                        nbr.setPred(currentVert)                         #current node is its predecessor
                        vertQueue.enqueue(nbr)                           #add it to the queue
                currentVert.setColor('black')
        else:
            pass
        
    def traverse(self, y):
        result = []
        if isinstance(y,Vertex):
            x = y
            while x.getPred():
                result.append(x.getId())
                x = x.getPred()
            result.append(x.getId())
            return result
        else:
            return
    
    
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
        possible = True
        times = [(i,self.vertList[i].getFinish()-self.vertList[i].getDiscovery()) for i in self.vertList.keys()]
        times.sort(key = lambda x: x[1])
        result = []
        for i in times:
            result.append(i[0])
        print(result)
        for i in range(1,len(result)):
            for j in result[:i]:
                print(j,'\t',list(map(lambda x: x.id, self.vertList[result[i]].connectedTo)))
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
    graph1.dijkstra(graph1.getVertex(start))
    #print(list(graph1.vertList.keys()))
    #graph.traverse(graph.getVertex(2))
    for i in list(graph1.vertList.keys()):
        if i != start:
            result = graph1.traverse(graph1.getVertex(i))
            result = result[::-1]
            print('\n for ',i,': ',result)


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

#    print(gr1.getEdges())
 #   print(gr1.graph_dot())
  #  print(gr1.getVertex(5))
#    gr1.bfs(gr1.getVertex(1))
 #   print(gr1.getVertex(5))
  #  print(gr1.traverse(gr1.getVertex(5)))
   # print(gr1.dfs())
    find_fastest(gr1, 2)
    
