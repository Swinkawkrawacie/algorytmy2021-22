#!/usr/bin/env python 
"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność implementacji kolejek QueueBaB i QueueBaE.
"""
import time
from matplotlib import pyplot as plt
from L4_ZAD1 import QueueBaB
from L4_ZAD1 import QueueBaE

if __name__ == "__main__":

    xaxis = range(1000,2000,5)
    BaB = QueueBaB()
    BaE = QueueBaE()
    
    #--------------adding to the queue------------------------
    on_list_time1 = []
    on_list_time2 = []

    for i in xaxis:
        start = time.time()
        for j in range(i):
            BaB.enqueue(j)
        end = time.time()
        on_list_time1.append(end-start)

    for i in xaxis:
        start = time.time()
        for j in range(i):
            BaE.enqueue(j)
        end = time.time()
        on_list_time2.append(end-start)
    
    plt.scatter(xaxis,on_list_time1, label = "BaB")
    plt.scatter(xaxis,on_list_time2, label = "BaE")
    plt.title("Adding to the queue")
    plt.legend()
    plt.show()

    plt.plot(xaxis,on_list_time1, label = "BaB")
    plt.plot(xaxis,on_list_time2, label = "BaE")
    plt.title("Adding to the queue")
    plt.legend()
    plt.show()

    #--------------removing from the queue---------------------
    of_list_time1 = []
    of_list_time2 = []

    for i in xaxis:
        start = time.time()
        for j in range(i):
            BaB.dequeue()
        end = time.time()
        of_list_time1.append(end-start)

    for i in xaxis:
        start = time.time()
        for j in range(i):
            BaE.dequeue()
        end = time.time()
        of_list_time2.append(end-start)

    plt.scatter(xaxis,of_list_time1, label = "BaB")
    plt.scatter(xaxis,of_list_time2, label = "BaE")
    plt.title("removing from the queue")
    plt.legend()
    plt.show()

    plt.plot(xaxis,of_list_time1, label = "BaB")
    plt.plot(xaxis,of_list_time2, label = "BaE")
    plt.title("removing from the queue")
    plt.legend()
    plt.show()

    #-----------adding and removing the queue------------------
    list_time1 = []
    list_time2 = []

    for i in xaxis:
        start = time.time()
        for j in range(i):
            BaB.enqueue(j)
        for j in range(i):
            BaB.dequeue()
        end = time.time()
        list_time1.append(end-start)
    
    for i in xaxis:
        start = time.time()
        for j in range(i):
            BaE.enqueue(j)
        for j in range(i):
            BaE.dequeue()
        end = time.time()
        list_time2.append(end-start)
    
    plt.scatter(xaxis,list_time1, label = "BaB")
    plt.scatter(xaxis,list_time2, label = "BaE")
    plt.title("adding and removing from the queue")
    plt.legend()
    plt.show()

    plt.plot(xaxis,list_time1, label = "BaB")
    plt.plot(xaxis,list_time2, label = "BaE")
    plt.title("adding and removing from the queue")
    plt.legend()
    plt.show()

    #-------------difference between BaB and BaE------------------
    plt.scatter(xaxis,[list_time1[i]-list_time2[i] for i in range(len(list_time1))], label = "BaB")
    plt.title("comparison (BaB time - BaE time)")
    plt.show()

    plt.plot(xaxis,[list_time1[i]-list_time2[i] for i in range(len(list_time1))], label = "BaB")
    plt.title("comparison (BaB time - BaE time)")
    plt.show()

    # maybe add some functions???