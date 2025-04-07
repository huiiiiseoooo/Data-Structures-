class Node:
    def __init__(self, element, next = None):
        self.element = element
        self.next = next

class LinkList:
    
    head = None
    tail = None
    size = 0

    def add_first(self,e):
        newnode = Node(e)
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def add_last(self,e):
        newnode = Node(e)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.size += 1

    def remove_first(self):
        if(self.head is None):
            print("error is empty")
        else:
            self.head = self.head.next
            self.size -= 1
    
    def printAll(self):
        current = self.head
        while current is not None:
            print(current.element, end=" -> ")
            current = current.next
        print("None")

            
    
L = LinkList()
L.add_last(10)
L.add_last(20)
L.add_first(5)
L.printAll()  # 출력: 5 -> 10 -> 20 -> None

L.remove_first()
L.printAll()  # 출력: 10 -> 20 -> None

