class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None
        
        
        
class AVL(object):
    
    def __init__(self):
        self.root = None
        
    def calcHeight(self, node):
        if not node:
            return -1
        else:
            return node.height
    
    def calcBalance(self, node):
    # if returns > 1  --> left heavy & right rotation
    # if returns < -1 --> right heavy & left rotation
        if not node:
            return 0
        else:
            return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)
    
    def rotateRight(self, node):
        print("Rotating to the right on node " , node.data);
        # temporary variables
        tempL = node.leftChild
        tempLtempR = tempL.rightChild
        # rotation
        tempL.rightChild = node
        node.leftChild = tempLtempR
        # update the heights
        node.height = max( self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) ) + 1
        # print(str(node.data) + ' : ' + str(node.height))
        tempL.height = max( self.calcHeight(tempL.leftChild), self.calcHeight(tempL.rightChild) ) + 1
        # replace the main node with tempL
        return tempL
    
    def rotateLeft(self, node):
        print("Rotating to the left on node " , node.data);
        # temporary variables
        tempR = node.rightChild
        tempRtempL = tempR.leftChild
        # rotation
        tempR.leftChild = node
        node.rightChild = tempRtempL
        # update the heights
        node.height = max( self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) ) + 1
        tempR.height = max( self.calcHeight(tempR.leftChild), self.calcHeight(tempR.rightChild) ) + 1
        # replace the main node with tempL
        return tempR
    
    def insert(self, data):
        self.root = self.insertNode(data, self.root)
        
    def insertNode(self, data, node):
        # until no node is there
        if not node:
            return Node(data)
        # skips if the node already exists
        if node.data == data:
            return node
        #
        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.insertNode(data, node.rightChild)
        #
        # update the node height
        node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1;
        #
        # return the node after violation settled
        return self.settleViolation(data, node)
    
    def settleViolation(self, data, node):
        ### ONLY FOR INSERTION OF NODES ###
        # calculate the balance
        balance = self.calcBalance(node)
        #
        # doubly left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Doubly left heavy situation...")
            return self.rotateRight(node)
        # left-right heavy situation
        elif balance > 1 and data > node.leftChild.data:
            print("Left-right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        # doubly right heavy situation
        elif balance < -1 and data > node.rightChild.data:
            print("Doubly right heavy situation...")
            return self.rotateLeft(node)
        # right-left heavy situation
        elif balance < -1 and data < node.rightChild.data:
            print("Right-left heavy situation...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        #
        return node
                
    def remove(self, data):
        if self.root:
           self.root = self.removeNode(data, self.root)
            
    ###########################################################################
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
                print("Removing a leaf node...")
                del node
                return None
            if not node.rightChild:
                # Deleting a node with only left child...
                print("Removing a node with only left child...")
                tempNode = node.leftChild
                del node
                return tempNode
            elif not node.leftChild:
                # Deleting a node with only right child...
                print("Removing a node with only right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            ###################################################################
            print("Removing a node with both left and right child...") 
            # Finding the largest of the predecessors in the left wing...
            tempNode = self.getPredecessor(node.leftChild)
            # replacing the node with the value of largest predecessor...
            node.data = tempNode.data
            # Removing the largest predecessor in the right wing...
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        #######################################################################
        node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1
		
        balance = self.calcBalance(node)
		
        # doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)
			
        # left-right situation
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild);
            return self.rotateRight(node)
		
        # doubly right situation
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)
			
        # right-left situation
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
			
        return node
        #######################################################################
        
    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node
    ###########################################################################
            
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
        print('[' + str(node.height) + '] ')        
        if node.leftChild:
            print('l: ', end ='')
            print("%s " % node.leftChild.data, end ='')
            print('[' + str(node.leftChild.height) + '] ')        
            
        if node.rightChild:
            print('r: ', end ='')
            print("%s " % node.rightChild.data, end ='')
            print('[' + str(node.rightChild.height) + '] ')        

        print('')
        
        if node.leftChild:
            self.traverseInOrder__(node.leftChild)
            
        if node.rightChild:
            self.traverseInOrder__(node.rightChild)
            
#%%
import random
ATA = AVL()

ATA.insert(5)

num = []
for i in range(10):
    num.append(random.randint(0,20))
    print(str(i+2) + ' : ' +  str(num[-1]))
    ATA.insert(num[-1])
    
print('')
print(ATA.traverse__(), end='')

print('')   
#print("IOT: ", end='')
#print(ATA.traverse(), end='')
#print('')
#
ATA.remove(5)
 
print("Min =", ATA.getMinValue())
print("Max =", ATA.getMaxValue())
print("Sorted: ", end='')
print(ATA.traverse(), end='')
