class Node(object):
    
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False

        
class DepthFirstSearch(object):
    
    def dfsprint(self, node):
        # DFS -> Stack -> FILO
        node.visited = True
        print(node.name)
        # 
        for adjc in node.adjacencyList:
            if not adjc.visited:
                self.dfsprint(adjc)
                
#%% Try it out

#      ---------A---------
#  ----B----    F        G
#  C       D             H
#          E

myBFS = DepthFirstSearch()

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')

# node A
A.adjacencyList.append(B)
A.adjacencyList.append(F)
A.adjacencyList.append(G)
# node B
B.adjacencyList.append(C)
B.adjacencyList.append(D)
# node D
D.adjacencyList.append(E)
# node G
G.adjacencyList.append(H)

myBFS.dfsprint(A)


#%% Try it out

#  --------A--------
#  B               C
#  ----D------E-----

myDFS = DepthFirstSearch()

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

# node A
A.adjacencyList.append(B)
A.adjacencyList.append(C)
# node B
B.adjacencyList.append(D)
# node C
C.adjacencyList.append(E)
# node D
D.adjacencyList.append(E)

myDFS.dfsprint(A)
