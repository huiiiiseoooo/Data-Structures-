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
        newnode = Node(k, v)
        if(self.size == 0):
            self.head = newnode
            self.size += 1
            return
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def find_min(self):
        temp = self.head
        min = temp
        while temp.next is not None:
            if temp.next.key < min.key:
                min = temp.next
            temp = temp.next
        return min
    
    def min(self):
        p = self.find_min()
        return (p.key, p.value)
    
    def remove_min(self):
        p = self.find_min()
        if self.head == p:
            self.head = self.head.next
            self.size-=1
            return
        prev = self.head
        while prev.next != p:
                prev = prev.next
        prev.next = p.next
        self.size -= 1




p = PriorityQueue()
p.additem(3,9)
p.additem(4,10)
p.additem(5,1)
p.additem(1,3)
p.additem(2,4)

p.remove_min()

print(p.min())