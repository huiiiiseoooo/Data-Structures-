import DoublyLinkedList

class Position:
    def __init__(self, container, node):
        self.container = container
        self.node = node

    def element(self):
        return self.node.element

class PositionalList(DoublyLinkedList):
    def __init__(self):
        self.header = None
        self.trailer = None



    def validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next is None:
            raise ValueError('p is no longer valid')
        return p.node
    
    def make_position(self, node):
        if node is self.header or node is self.trailer:
            return None
        else:
            return self.Position(self, node)
        
    def first(self):
        return self.make_position(self.header.next)
    
    # 미구현 맨 마지막에 구현 예정