class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def validate(node,minVal,maxVal):
    if not node:
        return True
    if(not (minVal<node.data<maxVal)):
        return False
    left=validate(node.left,minVal,node.data)
    right=validate(node.right,node.data,maxVal)
    return left and right


def solve(root):
    if not root:
        return True
    ans=validate(root,float('-inf'),float('inf'))
    return ans




root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
print(solve(root))

