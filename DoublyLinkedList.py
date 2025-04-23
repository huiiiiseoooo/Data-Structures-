class Node:
    def __init__(self,element, previ = None,next = None):
        self.element = element
        self.previ = previ
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0

    def insert_between(self, e, num):
        newnode = Node(e)
        if(self.size == 0):
            self.head.next = newnode
            newnode.previ = self.head
            self.tail.previ = newnode
            newnode.next = self.tail
        else:
            current = self.head
            previous = None
            for i in range(0, num):
                current = current.next
            previous = current.previ

            newnode.next = previous.next
            previous.next = newnode
            newnode.previ = current.previ
            current.previ = newnode
        self.size += 1
    
    def delete_node(self, num):
        if(self.is_empty() == True):
            print("error is empty")
        else:
            current = self.head
            previous = None
            for i in range(0, num):
                current = current.next
            previous = current.previ.previ

            previous.next = current
            current.previ = previous
            self.size -= 1

    def is_empty(self):
        if (self.size == 0):
            return True
            
    def __len__(self):
        current = self.head
        for i in range(0, self.size):
            current = current.next
            print(current.element)
        print(self.size)


DLL = DoublyLinkedList()
DLL.insert_between(3,1)
DLL.insert_between(6,2)
DLL.insert_between(7,3)
DLL.insert_between(8,2)
DLL.delete_node(3)
DLL.insert_between(10,3)

DLL.__len__()           