class Vertex(object):
    
    def __init__(self, name):
        self.name = name
        self.node = None
        
        
class Edge(object):
    
    def __init__(self, weight, startVertex, endVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.endVertex = endVertex
        
    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)
    
    def __lt__(self, other):
        return self.weight < other.weight;
        
    
class Node(object):
    def __init__(self, height, nodeID, parentNode):
        self.height = height
        self.nodeID = nodeID
        self.parentNode = parentNode
        
        
class DisjointSet(object):
    
    def __init__(self, vertexList):
        self.vertexList = vertexList
        self.rootNodes = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)
        
    def makeSets(self, vertexList):
        for V in vertexList:
            self.makeSet(V)
            
    def makeSet(self, vertex):
        node = Node(0, self.nodeCount, None)
        vertex.node = node
        self.rootNodes.append(node)
        self.nodeCount += 1
        self.setCount += 1
        
    def find(self, node):
        ########## FINDING THE ROOT NODE ##########
        currentNode = node
        # finds the root
        while currentNode.parentNode is not None:
            currentNode = currentNode.parentNode
        # determines the root node and the node started with    
        rootNode = currentNode
        currentNode = node
        ######## UNIFYING THE ROOT NODE FOR EVERY NODE IN THE SAME SET ########
        while currentNode is not rootNode:
            temp = currentNode.parentNode
            currentNode.parentNode = rootNode
            currentNode = temp
        # return the ID of the root node    
        return rootNode.nodeID
    
    def merge(self, node1, node2):
        # finding the IDs for each node
        ID1 = self.find(node1)
        ID2 = self.find(node2)
        # if have the same roots
        if ID1 == ID2:
            return
        # finding the root nodes
        root1 = self.rootNodes[ID1]
        root2 = self.rootNodes[ID2]
        
        if root1.height > root2.height:
            root2.parentNode = root1
        elif root2.height > root1.height:
            root1.parentNode = root2
        else:
            root2.parentNode = root1
            root1.height += 1
            

class Kruskal(object):
    
    def spanningTree(self, vertexList, edgeList):
        # create a base disjoint set
        disjointSet = DisjointSet(vertexList)
        # initialize the spanning tree
        spanningTree = []
        # sort the list of edges based on the weights
        edgeList.sort()
        # goes over all the sorted edges
        for edge in edgeList:
            u = edge.startVertex
            v = edge.endVertex
            # in case the start and end node do not belong to the same set
            if disjointSet.find(u.node) is not disjointSet.find(v.node):
                spanningTree.append(edge)
                disjointSet.merge(u.node, v.node)
                
        for edge in spanningTree:
            print(edge.startVertex.name, ' [', edge.weight, '] ',
                  edge.endVertex.name)
        
#%% TESTING

V1 = Vertex("A")
V2 = Vertex("B")
V3 = Vertex("C")
V4 = Vertex("D")
V5 = Vertex("E")
V6 = Vertex("F")
V7 = Vertex("G")

E1 = Edge(2,V1,V2)
E2 = Edge(6,V1,V3)
E3 = Edge(5,V1,V5)
E4 = Edge(10,V1,V6)
E5 = Edge(3,V2,V4)
E6 = Edge(3,V2,V5)
E7 = Edge(1,V3,V4)
E8 = Edge(2,V3,V6)
E9 = Edge(4,V4,V5)
E10 = Edge(5,V4,V7)
E11 = Edge(5,V6,V7)


vertexList = [V1, V2, V3, V4, V5, V6, V7]

edgeList = [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11]

myAlg = Kruskal()
myAlg.spanningTree(vertexList, edgeList)	
