class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def min(root):
    node=root
    while node.left:
        node=node.left
    return node.data

def max(root):
    node=root
    while node.right:
        node=node.right
    return node.data


root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
print(min(root))
print(max(root))
