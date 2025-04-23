class Node:
    def __init__(self,key,value, next =None):
        self.key = key
        self.value = value
        self.next = next

class PriorityQueue:
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def is_empty(self):
        return self.size == 0 
    

    def additem(self,k,v):
        newnode = Node(k,v)
        if self.head is None or newnode.key < self.head.key:
            newnode.next = self.head
            self.head = newnode
            self.size += 1
            return
        temp = self.head
        while temp.next is not None and newnode.key > temp.next.key:
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
        self.size += 1
        
    def min(self):
        return (self.head.key, self.head.value)
        
    
    def remove_min(self):
        self.head = self.head.next




p = PriorityQueue()
p.additem(3,9)
p.additem(4,10)
p.additem(5,1)
p.additem(1,3)
p.additem(2,4)

p.remove_min()
p.remove_min()

print(p.min())