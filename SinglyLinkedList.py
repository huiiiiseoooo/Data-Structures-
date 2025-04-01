class Node:
    size = 0
    
    def __init__(self, element, next):
        self.element = element
        self.next =  next
        self.size += 1

    def addFirst(L, e):
        newNode = Node(e)
        newNode.next = L.head
        L.head = newNode
        L.size += 1


