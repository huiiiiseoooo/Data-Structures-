class Node:
    def __init__(self,data, parent = None, left_node = None, right_node = None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        self.parent = parent
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add_root(self,e):
        self.root = Node(e)
        self.size += 1
        return self.root
    
    def add_left(self, node, e):
        newnode = Node(e,node)
        node.left_node = newnode
        self.size+=1
        return newnode
    
    def add_right(self, node, e):
        newnode = Node(e,node)
        node.right_node = newnode
        self.size +=1
        return newnode
    
    def preorder(self,node):
        if node is not None:
            print(node.data)
            self.preorder(node.left_node)
            self.preorder(node.right_node)

    def inorder(self,node):
        if node is not None:
            self.inorder(node.left_node)
            print(node.data)
            self.inorder(node.right_node)

    def postorder(self,node):
        if node is not None:
            self.postorder(node.left_node)
            self.postorder(node.right_node)
            print(node.data)

    def inorderExpressions(self, node):
        if node.left_node is not None:
            print("(",end='')
            self.inorderExpressions(node.left_node)

        print(node.data,end='')

        if node.right_node is not None:
            self.inorderExpressions(node.right_node)
            print(")",end='')

    def evalExpr(self, node):
        if node.left_node is None and node.right_node is None:
            return node.data
        else:
            x = self.evalExpr(node.left_node)
            y = self.evalExpr(node.right_node)
            return self.oper(x,y,node.data)
        
    def oper(self, x,y,data):
        if(data == "-"):
            return x-y
        if(data == "+"):
            return x+y
        if(data == "*"):
            return x*y
        if(data == "/"):
            return x/y
                

        
        
BT = BinaryTree()

n1 = BT.add_root("+")
n2 = BT.add_left(n1,"*")
n3 = BT.add_right(n1,"*")
n4 = BT.add_left(n2, 1)
n5 = BT.add_right(n2,"-")
n6 = BT.add_left(n3, 3)
n7 = BT.add_right(n3,2)
n8 = BT.add_left(n5, 5)
n9 = BT.add_right(n5, 1)

        
print(BT.evalExpr(n1))
            