import math
import heapq

class Vertex(object):
    
    def __init__(self, name):
        self.name  = name
        self.predecessor = None
        self.minDistance = math.inf
        self.adjList = []
        
    def __cmp__(self, otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance);
		
    def __lt__(self, other):
        return self.minDistance < other.minDistance
        
        
class Edge(object):
    
    def __init__(self, weight, startVertex, endVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.endVertex = endVertex
        
        
class Dijkstra(object):
    
    def calcShortestPath(self, vertexList, sourceVertex):
        # initialize the heap
        q = []
        sourceVertex.minDistance = 0
        heapq.heappush(q, sourceVertex)
        # go through all vertices untill the heap gets empty
        while q:
            # the heap with minimum minDistance pops out of the heap
            u = heapq.heappop(q)
            # explore all the edges and the neighbor vertices
            for edge in u.adjList:
                v = edge.endVertex
                tempDistance = u.minDistance + edge.weight
                
                if tempDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = tempDistance
                    heapq.heappush(q, v)
      
    def getShortestPath(self, vertex):
        print('The shortest path to node ' + vertex.name + ' is ' + 
              str(vertex.minDistance) + ' units long.')
        # find the predecessors
        temp = vertex
        while temp:
            print(temp.name, end = ' < ')
            temp = temp.predecessor
        
  #%% Testing

V1 = Vertex("A")
V2 = Vertex("B")
V3 = Vertex("C")
V4 = Vertex("D")
V5 = Vertex("E")
V6 = Vertex("F")
V7 = Vertex("G")
V8 = Vertex("H")

E1 = Edge(5,V1,V2)
E2 = Edge(8,V1,V8)
E3 = Edge(9,V1,V5)
E4 = Edge(15,V2,V4)
E5 = Edge(12,V2,V3)
E6 = Edge(4,V2,V8)
E7 = Edge(7,V8,V3)
E8 = Edge(6,V8,V6)
E9 = Edge(5,V5,V8)
E10 = Edge(4,V5,V6)
E11 = Edge(20,V5,V7)
E12 = Edge(1,V6,V3)
E13 = Edge(13,V6,V7)
E14 = Edge(3,V3,V4)
E15 = Edge(11,V3,V7)
E16 = Edge(9,V4,V7)

V1.adjList.append(E1)
V1.adjList.append(E2)
V1.adjList.append(E3)
V2.adjList.append(E4)
V2.adjList.append(E5)
V2.adjList.append(E6)
V8.adjList.append(E7)
V8.adjList.append(E8)
V5.adjList.append(E9)
V5.adjList.append(E10)
V5.adjList.append(E11)
V6.adjList.append(E12)
V6.adjList.append(E13)
V3.adjList.append(E14)
V3.adjList.append(E15)
V4.adjList.append(E16)


vertexList = (V1, V2, V3, V4, V5, V6, V7, V8)

myAlg = Dijkstra()
myAlg.calcShortestPath(vertexList, V1)
myAlg.getShortestPath(V4)
