class Node(object):
    
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        
        
        
class BreadthFirstSearch(object):
    
    def __init__(self):
        self.queue = []
    
    def bfsprint(self, startNode):
        # start with the startNode
        self.queue.append(startNode)
        startNode.visited = True
        # BFS -> Queue -> FIFO
        while self.queue:
            # print the mother node
            currentNode = self.queue.pop(0)
            print(currentNode.name)
            # 
            for adjc in currentNode.adjacencyList:
                if not adjc.visited:
                    adjc.visited = True
                    self.queue.append(adjc)
                
#%% Try it out

#      ---------A---------
#  ----B----    F        G
#  C       D             H
#          E

myBFS = BreadthFirstSearch()

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

myBFS.bfsprint(A)


#%% Try it out

#  --------A--------
#  B               C
#  ----D------E-----

myBFS = BreadthFirstSearch()

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

myBFS.bfsprint(A)
