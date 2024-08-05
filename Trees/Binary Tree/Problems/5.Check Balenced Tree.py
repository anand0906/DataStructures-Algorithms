class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def findHeight(node):
    if not node:
        return 0
    leftHeight=findHeight(node.left)
    rightHeight=findHeight(node.right)
    return 1+max(leftHeight,rightHeight)

def bruteForce(node):
    if not node:
        return True
    leftHeight=findHeight(node.left)
    rightHeight=findHeight(node.right)

    diff=abs(leftHeight-rightHeight)

    if((diff<=1) and bruteForce(node.left) and bruteForce(node.right)):
        return True
    return False

def Height(node):
    if(not node):
        return 0
    leftHeight=Height(node.left)
    if(leftHeight==-1):
        return -1
    rightHeight=Height(node.right)
    if(rightHeight==-1):
        return -1
    diff=abs(leftHeight-rightHeight)
    if(diff>1):
        return -1
    return 1+max(leftHeight,rightHeight)

def optimized(node):
    return Height(node)
    

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
print(optimized(root)!=-1)

