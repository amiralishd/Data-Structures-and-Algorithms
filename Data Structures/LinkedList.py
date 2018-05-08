class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
 
       
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    # O(1)
    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
            
    # O(1)       
    def size1(self):
        return self.size
    
    # O(N)
    def size2(self):
        s = 0
        countNode = self.head
        while countNode is not None:
            s += 1
            countNode = countNode.nextNode            
        return s
    
    # O(N)
    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        countNode = self.head
        while countNode.nextNode is not None:
            countNode = countNode.nextNode
        countNode.nextNode = newNode
        
    # O(N)
    def traverseList(self):
        countNode = self.head
        while countNode.nextNode is not None:
            print(countNode.data)
            countNode = countNode.nextNode
        print(countNode.data)    
            
    # O(N)
    def remove(self, data):
        if self.head == None:
            return
        self.size -= 1
        currentNode = self.head
        previousNode = None        
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if previousNode is None:
            self.head = currentNode.nextNode
            currentNode = None
        else:
            previousNode.nextNode = currentNode.nextNode
            currentNode = None
            

#%% 

Ali = LinkedList()

Ali.insertStart('C')
Ali.insertStart('B')
Ali.insertStart('A')
Ali.insertEnd('D')
Ali.insertEnd('E')
Ali.traverseList()
print(Ali.size1())
print('')
Ali.remove('C')
Ali.traverseList()
print(Ali.size2())
