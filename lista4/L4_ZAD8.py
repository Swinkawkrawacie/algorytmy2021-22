#!/usr/bin/env python

"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność listy jednokierunkowej i listy wbudowanej w Pythona.
"""

import time
from matplotlib import pyplot as plt
from L4_ZAD5 import UnorderedList

if __name__ == "__main__":
    xaxis = range(1000,2000,5)
    python_list = []
    my_list = UnorderedList()

    #---------------------adding elements to the list (at the end)------------------------
    on_list_time1 = []
    on_list_time2 = []
    #python list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            python_list.append(j)
        end = time.time()
        on_list_time1.append(end-start)
    #my list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            my_list.append(j)
        end = time.time()
        on_list_time2.append(end-start)
    
    plt.scatter(xaxis,on_list_time1, label = "python list")
    plt.scatter(xaxis,on_list_time2, label = "my list")
    plt.title("Adding to the list")
    plt.legend()
    plt.show()

    plt.plot(xaxis,on_list_time1, label = "python list")
    plt.plot(xaxis,on_list_time2, label = "my list")
    plt.title("Adding to the list")
    plt.legend()
    plt.show()

    #---------------------popping elements from the list------------------------
    on_list_time1 = []
    on_list_time2 = []
    #python list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            python_list.pop()
        end = time.time()
        on_list_time1.append(end-start)
    #my list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            my_list.pop()
        end = time.time()
        on_list_time2.append(end-start)
    
    plt.scatter(xaxis,on_list_time1, label = "python list")
    plt.scatter(xaxis,on_list_time2, label = "my list")
    plt.title("Popping from the list")
    plt.legend()
    plt.show()

    plt.plot(xaxis,on_list_time1, label = "python list")
    plt.plot(xaxis,on_list_time2, label = "my list")
    plt.title("Popping from the list")
    plt.legend()
    plt.show()

    #---------------------adding elements to the list (at the beggining)------------------------
    #---------------------popping elements from the beggining of the list------------------------
    #best cominations for both