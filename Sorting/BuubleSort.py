#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:22:49 2017

@author: amirali
"""
#%% Buuble Sort

def BubbleSort(list):
    # loop of [len(list)-1] times
    for i in range(0,len(list)-1):
        # will be changed to False later if swapping occurs
        noSwap = True
        # loop of [len(list)-1-i] times
        for j in range(0,len(list)-i-1):
            # swap
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                # swapping occured
                noSwap = False
        # in case of tracking
        #print(i)
        # if no swapping occured --> sorted list is ready
        if noSwap:
            break
    print(list)

#%% Testing
myList = [0,0,0,-1,-0,1,2,3,2,1]
BubbleSort(myList)
