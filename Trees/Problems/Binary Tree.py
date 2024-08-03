class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self,node):
        self.root=node


tree=BinaryTree(Node('A'))
root=tree.root
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
