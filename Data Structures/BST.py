#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:19:41 2017

@author: amirali
"""
##########################
### Binary Search Tree ###
##########################

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)
    
    #O(logN)       
    def insertNode(self, data, node):
        if data == node.data:
            return
        elif data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)
                
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)
            
    def removeNode(self, data, node):
        if not node:
            return node
        #######################################################################
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            ###################################################################
            if not node.rightChild and not node.leftChild:
                # Deleting a leaf...
                print("Deleting a leaf node...")
                del node
                return None
            if not node.rightChild:
                # Deleting a node with only left child...
                print("Deleting a node with only left child...")
                tempNode = node.leftChild
                del node
                return tempNode
            elif not node.leftChild:
                # Deleting a node with only right child...
                print("Deleting a node with only right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            ###################################################################
            print("Deleting a node with both left and right child...") 
            # Finding the largest of the predecessors in the left wing...
            tempNode = self.getPredecessor(node.leftChild)
            # replacing the node with the value of largest predecessor...
            node.data = tempNode.data
            # Removing the largest predecessor in the right wing...
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        return node
        #######################################################################
        
    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node
                
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
        
    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        else:
            return node.data
            
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
        
    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        else:
            return node.data
            
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
            
    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("%s " % node.data, end ='')
            
        if node.rightChild:
            self.traverseInOrder(node.rightChild)
            
    def traverse__(self):
        if self.root:
            self.traverseInOrder__(self.root)
            
    def traverseInOrder__(self, node):
        print('c: ', end ='')
        print("%s " % node.data, end ='')        
        if node.leftChild:
            print('l: ', end ='')
            print("%s " % node.leftChild.data, end ='')            
        if node.rightChild:
            print('r: ', end ='')
            print("%s " % node.rightChild.data, end ='')           
        print('')
        
        if node.leftChild:
            self.traverseInOrder__(node.leftChild)
            
        if node.rightChild:
            self.traverseInOrder__(node.rightChild)
            
#%%
import random
Asb = BinarySearchTree()

Asb.insert(5)

print('')   
print("IOT: ", end='')
print(Asb.traverse(), end='')
print('')

for i in range(20):
    num = random.randint(0,20)
    print(num, end=' ')
    Asb.insert(num)
    
print('')
print(Asb.traverse__(), end='')

print('')   
print("IOT: ", end='')
print(Asb.traverse(), end='')
print('')

Asb.remove(5)
 
print("Min =", Asb.getMinValue())
print("Max =", Asb.getMaxValue())
print("IOT: ", end='')
print(Asb.traverse(), end='')

    