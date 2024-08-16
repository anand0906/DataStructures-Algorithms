class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def solve(root,target):
    node=root
    while node and node.data!=target:
        if(target>node.data):
            node=node.right
        else:
            node=node.left
    if(node):
        return True
    else:
        return False



root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
target=int(input())
print(solve(root,target))
