#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:21:45 2017

@author: amirali
"""

#%%
class HashTable(object):
    
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def hashfunction(self, key):
        sum = 0
        # summing the ascii number of all the letters
        for letter in key:
            sum = sum + ord(letter)
        # returning the remainder of the sum divided by the hashtable size
        return sum%self.size
    
    def insert(self, key, data):
        # finding the index
        index = self.hashfunction(key)
        # in case of collision
        while self.keys[index]:
            # in case of having the same key in that index:
            if self.keys[index] == key:
                self.values[index] = data # update the values
                return
            # rehash and try to find another slot
            index = (index+1) % self.size
        # when the empty slot found
        self.keys[index] = key
        self.values[index] = data
        
    def get(self, key):
        # finding the index
        index = self.hashfunction(key)
        # notice that this index might not be the one used when inserting the
        # key in the hashtable and it might have been moved
        while self.keys[index]:
            if self.keys[index] == key:
                return self.values[index]
            index = (index+1) % self.size
        # if the key was not found
        return None
    
#%%

fruits = HashTable(10)
fruits.insert('apple',14)
fruits.insert('orange',18)
fruits.insert('berry',12)
fruits.insert('banana',7)

print(fruits.get('apple'))
print(fruits.get('orange'))
print(fruits.get('watermelon'))
        

        