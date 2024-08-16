class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def helper(node):
    if(node.left==None):
        return node.right
    elif(node.right==None):
        return node.left
    else:
        rightMost=node.left
        while rightMost.right:
            rightMost=rightMost.right
        rightMost.right=node.right
        return node.left


def solve(root,target):
    if(not root):
        return None
    if(root.data==target):
        return helper(root)
    node=root
    while node:
        if(target > node.data):
            if(node.right and node.right.data==target):
                node.right=helper(node.right)
            else:
                node=node.right
        else:
            if(node.left and node.left.data==target):
                node.left=helper(node.left)
            else:
                node=node.left
    return root
            



root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
target=int(input())
solve(root,target)

