#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:45:33 2017

@author: amirali
"""
#%% Insertion Sort

def insertionSort(list):
    # goes over all items
    for i in range(0, len(list)):
        # start "j" from "i+1"
        j = i
        # goes over all before if needed
        while j > 0 and  list[j-1] > list[j]:
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j -= 1
    print(list)
               
#%% Testing
      
myList = [ -4, 6, 8, 1, 0, 10, 9, 5, -14]
insertionSort(myList)