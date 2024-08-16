class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,target):
    node=root
    if(not node):
        root=Node(target)
        return root
    while True:
        if(target > node.data):
            if(node.right):
                node=node.right
            else:
                node.right=Node(target)
                break
        else:
            if(node.left):
                node=node.left
            else:
                node.left=Node(target)
                break
    return root


root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
target=int(input())
insert(root,target)
