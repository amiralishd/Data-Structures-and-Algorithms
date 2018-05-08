class Heap(object):
    
    def __init__(self, size):
         self.heapSize = size
         self.heap = [0] * self.heapSize
         self.currentPosition = -1
         
    def isFull (self):
        if self.currentPosition == self.heapSize-1:
            return True
        else:
            return False
         
    def insert(self, data):
        if self.isFull():
            print('Heap is full...')
            return
        #
        self.currentPosition = self.currentPosition + 1
        self.heap[self.currentPosition] = data
        self.fixUp(self.currentPosition)
        
    def fixUp(self, index):
        parentIndex = (index-1)//2
        while parentIndex >= 0 and self.heap[index] > self.heap[parentIndex]:
            #
            tempData = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = tempData
            #
            index = (index-1)//2
            parentIndex = (parentIndex-1)//2
            
    def Print(self):
        print(self.heap)
        
    def heapSort(self):
        for i in range(0, self.currentPosition):
            head = self.heap[0]
            # print("%d " % head)
            self.heap[0] = self.heap[self.currentPosition-i]
            self.heap[self.currentPosition-i] = head
            self.fixDown(0, self.currentPosition-i)   
        # print the result
        print(self.heap)
            
    def fixDown(self, index, uptoIndex):
        #
        while index < uptoIndex:
            LCI = 2 * index + 1
            RCI = 2 * index + 2
            # choosing the child to be swapped
            if LCI < uptoIndex:
                if RCI < uptoIndex:
                    if self.heap[LCI] > self.heap[RCI]:
                        toSwapCI = LCI
                    else:
                        toSwapCI = RCI
                else:
                    toSwapCI = LCI
                # see if swapping is needed
                if self.heap[toSwapCI] > self.heap[index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[toSwapCI]
                    self.heap[toSwapCI] = temp
                else:
                    break # breaks because there's no need to swap further down
            else:
                break # breaks because we are at the uptoIndex node
            # update the index
            index = toSwapCI
             
#%% 
""" Try it out """

import random
num = 20
Ali = Heap(num)

#Ali.insert(18)
#Ali.insert(11)
#Ali.insert(16)
#Ali.insert(5)
#Ali.insert(0)
#Ali.insert(8)

for i in range(num):
    Ali.insert(random.randint(0,20))


Ali.Print()
Ali.heapSort()
        
#%%
""" Import Heap library """
from heapq import heappush, heappop, heapify

heap = []
nums = [12,3,5,0,7,9,6]

for num in nums:
    heappush(heap, num)
    
while heap:
    print(heappop(heap))

print(nums)    
heapify(nums)
print(nums)     
