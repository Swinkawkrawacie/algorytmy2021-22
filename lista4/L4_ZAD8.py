#!/usr/bin/env python

"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność listy jednokierunkowej i listy wbudowanej w Pythona.
"""

import time
from matplotlib import pyplot as plt
from L4_ZAD5 import UnorderedList

if __name__ == "__main__":
    xaxis = range(100,500,5)
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
    on_list_time3 = []
    on_list_time4 = []
    #python list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            python_list.insert(j,0)
        end = time.time()
        on_list_time3.append(end-start)
    #my list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            my_list.add(j)
        end = time.time()
        on_list_time4.append(end-start)
    
    plt.scatter(xaxis,on_list_time3, label = "python list")
    plt.scatter(xaxis,on_list_time4, label = "my list")
    plt.title("Adding to the list")
    plt.legend()
    plt.show()

    plt.plot(xaxis,on_list_time3, label = "python list")
    plt.plot(xaxis,on_list_time4, label = "my list")
    plt.title("Adding to the list")
    plt.legend()
    plt.show()
    #---------------------popping elements from the beggining of the list------------------------
    on_list_time3 = []
    on_list_time4 = []
    #python list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            python_list.pop(0)
        end = time.time()
        on_list_time3.append(end-start)
    #my list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            my_list.pop(0)
        end = time.time()
        on_list_time4.append(end-start)
    
    plt.scatter(xaxis,on_list_time3, label = "python list")
    plt.scatter(xaxis,on_list_time4, label = "my list")
    plt.title("Popping from the list")
    plt.legend()
    plt.show()

    plt.plot(xaxis,on_list_time3, label = "python list")
    plt.plot(xaxis,on_list_time4, label = "my list")
    plt.title("Popping from the list")
    plt.legend()
    plt.show()
    #
    #---------------------adding elements to the list (at the beggining) and popping from the beggining------------------------
    on_list_time5 = []
    on_list_time6 = []
    #python list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            python_list.insert(j,0)
        for j in range(i):
            python_list.pop(0)
        end = time.time()
        on_list_time5.append(end-start)
    #my list
    for i in xaxis:
        start = time.time()
        for j in range(i):
            my_list.add(j)
        for j in range(i):
            my_list.pop(0)
        end = time.time()
        on_list_time6.append(end-start)
    
    plt.scatter(xaxis,on_list_time5, label = "python list")
    plt.scatter(xaxis,on_list_time6, label = "my list")
    plt.title("Comparison")
    plt.legend()
    plt.show()

    plt.plot(xaxis,on_list_time5, label = "python list")
    plt.plot(xaxis,on_list_time6, label = "my list")
    plt.title("Comparison")
    plt.legend()
    plt.show()