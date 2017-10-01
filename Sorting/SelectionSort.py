#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:51:57 2017

@author: amirali
"""

#%% Selection Sort

def selectionSort(list):
    # goes over all the elements from the first to one before the last
    for i in range(len(list)-1):
        # initialize the index of the minimum
        index = i
        # goes over all the elements from the one after "i" to the last one
        for j in range(i+1, len(list)):
            # checks to see if it is the minimum and then changes the index
            if list[j] < list[index]:
                index = j
        # swaps if needed    
        if index != i:
            temp = list[i]
            list[i] = list[index]
            list[index] = temp
    # print the sorted list
    print(list)
        
#%% Testing
      
myList = [ -4, 6, 8, 1, 0, 10, 9, 5, -14]
selectionSort(myList)
        