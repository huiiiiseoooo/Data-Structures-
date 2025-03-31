import sys

MAX_SIZE_STACK = 5

class stack:
    def __init__(self):
        self.stack = [None] * MAX_SIZE_STACK
        self.tops = -1
    
    def empty(self):
        if(self.tops == -1):
            print(1)
        else:
            print(0)
    
    def push(self, item):
        if(self.tops == MAX_SIZE_STACK):
            print("overflow")
        self.stack[self.tops+1] = item
        print(self.stack[self.tops+1])
        self.tops += 1

    def pop(self):
        if(self.tops == -1):
            print(-1)
        print(self.stack[self.tops])
        self.stack[self.tops] = None
        self.tops -= 1
    
    def top(self):
        print(self.stack[self.tops])
    
    def size(self):
        print(self.tops+1)
    
s= stack()  
n= int(sys.stdin.readline())
for i in range(n):
    num = sys.stdin.readline().split()

    if(num[0] == "push"):
        s.push(num[1])
    elif(num[0] == "pop"):
        s.pop()
    elif(num[0] == "empty"):
        s.empty()
    elif(num[0] == "top"):
        s.top()
    elif(num[0] == "size"):
        s.size()