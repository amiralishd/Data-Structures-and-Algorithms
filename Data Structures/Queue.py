class Queue(object):
    
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]
    
    def sizeQueue(self):
        return len(self.queue)
    
    
#%% 

Haji = Queue()
Haji.enqueue(3)
Haji.enqueue(2)
Haji.enqueue(1)
print('Haji = ', Haji.queue)
print('Dequeue = ', Haji.dequeue())
print('Size = ', Haji.sizeQueue())
print('Peek = ', Haji.peek())
print('Size = ', Haji.sizeQueue())
