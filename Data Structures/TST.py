class Node(object):

    def __init__(self, character):
        self.character = character
        self.leftChild = None
        self.middleChild = None
        self.rightChild = None
        self.value = None
        
class TST(object):
    
    def __init__(self):
        self.rootNode = None
        
    def insert(self, key, value):
        self.rootNode = self.insertNode(self.rootNode, key, value, 0)
        
    def insertNode(self, node, key, value, index):
        # reading the key
        c = key[index]
        # add the node if it does not exist
        if node == None:
            node = Node(c)
        # it exist now, either created or had been there already
        if c < node.character:
            node.leftChild = self.insertNode(node.leftChild, key, value, index)
        elif c > node.character:
            node.rightChild = self.insertNode(node.rightChild, key, value, index)
        # adding under the middleChild column
        elif index < len(key) - 1:
            node.middleChild = self.insertNode(node.middleChild, key, value, index+1)
        # finally at the last character put the value
        else:
            node.value = value
        #
        return node
    
    def get(self, key):
        node = self.getNode(self.rootNode, key, 0)
        # if key not found
        if node == None:
            return 'Key not found...'
        else:
            return node.value
        
    def getNode(self, node, key, index):
        # if key not found
        if not node:
            return None
        # reading the key
        c = key[index]
        #
        if c < node.character:
            return self.getNode(node.leftChild, key, index)
        elif c > node.character:
            return self.getNode(node.rightChild, key, index)
        elif index < len(key) - 1:
            return self.getNode(node.middleChild, key, index+1)
        else:
            return node
        
        
#%% try it out     
 
fruits = TST()
fruits.insert('apple',14)
fruits.insert('orange',18)
fruits.insert('berry',12)
fruits.insert('banana',7)

print(fruits.get('apple'))
print(fruits.get('orange'))
print(fruits.get('watermelon'))
