#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:44:22 2017

@author: amirali
"""

#%% Quick Sort

def quickSort(list, lowIndex, highIndex):
    # checks to exit the loop [recursion base]
    if lowIndex >= highIndex:
        return
    # does the quick sort recursively on each sub-array
    else:
        pivotIndex = partition(list, lowIndex, highIndex)
        quickSort(list, lowIndex, pivotIndex-1)
        quickSort(list, pivotIndex+1, highIndex)
        
def partition(list, lowIndex, highIndex):
    # this function returns the pivot index with the sub-array divided with
    # respect to the pivot item
    # assumes the pivot to be in the middle of the sub-array
    pivotIndex = (lowIndex+highIndex)//2
    # swaps the pivot item witht the last item [temporarily until division is final]
    swap(list, pivotIndex, highIndex)
    # "i" will be returned as the ultimate location of the pivot item
    # for now initilaized to be in the beginning of the sub-array
    i = lowIndex
    # loop over the whole sub-array
    for j in range(lowIndex, highIndex):
        # compare with the last item in the sub-array [the pivot item actually!]
        if list[j] < list[highIndex]:
            # puts the new found smaller item (than pivot) in the "i"th location
            swap(list, i, j)
            # updates the position of the pivot item [to be inserted]
            i += 1 
    # put back the pivot item at the right location from the end of the sub-array
    swap(list, i, highIndex)
    # return the ultimate location of the pivot item    
    return i
                        
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    
#%% Testing
      
myList = [ -4, 6, 8, 1, 0, 10, 9, 5, -14]
quickSort(myList, 0, len(myList)-1)
print(myList)
