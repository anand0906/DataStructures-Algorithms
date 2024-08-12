class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def InOrder(node,count):
    if(not node):
        return
    count[0]+=1
    InOrder(node.left,count)
    InOrder(node.right,count)

def bruteForce(root):
    if not root:
        return 0
    count=[0]
    InOrder(root,count)
    return count[0]

def findLeftHeight(node):
    h=0
    while node:
        h+=1
        node=node.left
    return h

def findRightHeight(node):
    h=0
    while node:
        h+=1
        node=node.right
    return h

def count(node):
    if not node:
        return 0
    lh=findLeftHeight(node)
    rh=findRightHeight(node)
    if(lh==rh):
        return (2**(lh)-1)
    return 1+count(node.left)+count(node.right)


def optimized(root):
    if not root:
        return 0
    return count(root)
    


root=Node(4)
root.left=Node(1)
root.right=Node(3)
root.left.right=Node(1)
root.left.left=Node(5)
print(bruteForce(root))
print(optimized(root))

