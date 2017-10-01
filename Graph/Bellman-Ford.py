#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:07:30 2017

@author: amirali
"""

import math

class Vertex(object):
    
    def __init__(self, name):
        self.name  = name
        self.visited = False
        self.predecessor = None
        self.minDistance = math.inf
        self.adjList = []
        
        
class Edge(object):
    
    def __init__(self, weight, startVertex, endVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.endVertex = endVertex
        
        
class BellmanFord(object):
    
    def __init__ (self):
        self.HAS_CYCLE = False
    
    def calcShortestPath(self, vertexList, edgeList, sourceVertex):
        # source vertex with zero distance
        sourceVertex.minDistance = 0
        # loop over the vertices
        for i in range(0,len(vertexList)-1):
            # loop over the edges
            for edge in edgeList:
                u = edge.startVertex
                v = edge.endVertex
                tempDistance = u.minDistance + edge.weight
                # do the check
                if tempDistance < v.minDistance:
                    v.minDistance = tempDistance
                    v.predecessor = u
        # one last loop over the edges to check the existence of a cycle            
        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected!")
                self.HAS_CYCLE = True
                return
            
    def hasCycle(self, edge):
        # checks if there is a negative cycle
        if (edge.startVertex.minDistance + edge.weight) < edge.endVertex.minDistance:
            return True
        else:
            return False

    def getShortestPath(self, vertex):
        if not self.HAS_CYCLE:
            print('The shortest path to node ' + vertex.name + ' is ' + 
                  str(vertex.minDistance) + ' units long.')
            # find the predecessors
            temp = vertex
            while temp:
                print(temp.name, end = ' < ')
                temp = temp.predecessor
        else:
            print("Negative cycle detected!");

        
#%% Testing

V1 = Vertex("A");
V2 = Vertex("B");
V3 = Vertex("C");
V4 = Vertex("D");
V5 = Vertex("E");
V6 = Vertex("F");
V7 = Vertex("G");
V8 = Vertex("H");

E1 = Edge(5,V1,V2);
E2 = Edge(8,V1,V8);
E3 = Edge(9,V1,V5);
E4 = Edge(15,V2,V4);
E5 = Edge(12,V2,V3);
E6 = Edge(4,V2,V8);
E7 = Edge(7,V8,V3);
E8 = Edge(6,V8,V6);
E9 = Edge(5,V5,V8);
E10 = Edge(4,V5,V6);
E11 = Edge(20,V5,V7);
E12 = Edge(1,V6,V3);
E13 = Edge(13,V6,V7);
E14 = Edge(3,V3,V4);
E15 = Edge(11,V3,V7);
E16 = Edge(9,V4,V7);

E17 = Edge(1,V1,V2);
E18 = Edge(1,V2,V3);
E19 = Edge(-3,V3,V1);

vertexList = (V1, V2, V3, V4, V5, V6, V7, V8)
edgeList = (E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,E16)
#edgeList = (E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19)

myAlg = BellmanFord()
myAlg.calcShortestPath(vertexList, edgeList, V1)
myAlg.getShortestPath(V7)     
        
        