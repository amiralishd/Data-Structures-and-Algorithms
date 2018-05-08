#%% Merge Sort

def mergeSort(list):
########## DIVIDE PART ########## 
    # recursion base   
    if len(list) == 1:
        return
    # middle index:
    mid = len(list)//2
    # temporary left and right sub-arrays
    leftList = list[:mid]       # NOTE: We can now overwrite the main array
    rightList = list[mid:]      # with it items saved in the sub-arrays!
    # recursion on merge sort for sub-arrays
    mergeSort(leftList)
    mergeSort(rightList)

########## CONQUER PART ##########
# initialize the indices
    i = 0
    j = 0
    k = 0
    # runs until one of the sub-arrays runs out of items
    while i < len(leftList) and j < len(rightList):
        # pop one item out of left sub-array
        if leftList[i] < rightList [j]:
            list[k] = leftList[i]
            # increase the index in the left sub-array
            i += 1    
        # pop one item out of right sub-array
        else:
            list[k] = rightList[j]
            # increase the index in the right sub-array
            j += 1
        # increase the index in main array
        k += 1        
    # in case items are left in the left sub-array
    while i < len(leftList):
        list[k] = leftList[i]
        i += 1
        k += 1    
    # in case items are left in the right sub-array
    while j < len(rightList):
        list[k] = rightList[j]
        j += 1
        k += 1     
    # return the merged list    
    return list

#%% Testing
nums = [-3, -2, -1, 1, 2, 1, 0, -1, -2, -3]
mergeSort(nums)
print(nums)
