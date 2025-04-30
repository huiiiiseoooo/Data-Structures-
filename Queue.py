MAX_SIZE_QUEUE = 5

class Queue:
    def __init__(self):
        self.queue = [None] * MAX_SIZE_QUEUE
        self.top = 0
        self.first = 0
    
    def enqueue(self, item):
        self.top = (self.top+1) % MAX_SIZE_QUEUE
        self.queue[self.top] = item
        
    def dequeue(self):
        self.first = (self.first+1)%MAX_SIZE_QUEUE
        self.queue[self.first] = None
        
    def is_empty(self):
        if(self.top == self.first):
            return True
        else:
            return False

    def len(self):
        print(self.top - self.first)

    def firsts(self):
        print(self.queue[self.first+1])

q = Queue()
q.enqueue(5)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.dequeue()
q.len()
print(q.is_empty())
q.firsts()