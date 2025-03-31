MAX_SIZE_STACK = 5

class stack:
    def __init__(self):
        self.stack = [None] * MAX_SIZE_STACK
        self.top = -1
    
    def is_empty(self):
        if(self.top == -1):
            return True
        else:
            return False
    
    def push(self, item):
        if(self.top == MAX_SIZE_STACK):
            print("overflow")
        self.stack[self.top+1] = item
        print(self.stack[self.top+1])
        self.top += 1

    def pop(self):
        if(self.top == -1):
            print("underflow")
        print(self.stack[self.top])
        self.stack[self.top] = None
        self.top -= 1
    
    def show(self):
        for i in self.stack:
            print(i)
    
    


s =stack()
s. push(3)
s.push(5)
s.show()