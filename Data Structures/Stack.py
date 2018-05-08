class Stack(object):
    
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def sizeStack(self):
        return len(self.stack)
    
    
#%% 

Haji = Stack()
Haji.push(3)
Haji.push(2)
Haji.push(1)
print('Haji = ', Haji.stack)
print('Pop = ', Haji.pop())
print('Size = ', Haji.sizeStack())
print('Peek = ', Haji.peek())
print('Size = ', Haji.sizeStack())  
