class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def findHeight(node):
    if(not node):
        return 0
    leftHeight=findHeight(node.left)
    rightHeight=findHeight(node.right)
    return 1+max(leftHeight,rightHeight)

def bruteForce(node):
    if not node:
        return 0
    leftHeight=findHeight(node.left)
    rightHeight=findHeight(node.right)
    return max(leftHeight+rightHeight,bruteForce(node.left),bruteForce(node.right))

def Height(node,diameter):
    if(not node):
        return 0
    leftHeight=Height(node.left,diameter)
    rightHeight=Height(node.right,diameter)
    diameter[0]=max(diameter[0],leftHeight+rightHeight)
    return 1+max(leftHeight,rightHeight)

def optimized(node):
    diameter=[0]
    Height(node,diameter)
    return diameter[0]

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.left.right=Node(9)
root.left.left.right.left=Node(1)
root.right.left=Node(7)
root.right.right=Node(6)
root.right.right.left=Node(8)
print(bruteForce(root))
print(optimized(root))
