class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isLeaf(node):
    return node.left==None and node.right==None

def addLeftBoundary(node,ans):
    current=node.left
    while current:
        if(not isLeaf(current)):
            ans.append(current.data)
        if(current.left):
            current=current.left
        else:
            current=current.right

def addRightBoundary(node,ans):
    current=node.right
    stack=[]
    while current:
        if(not isLeaf(current)):
            stack.append(current.data)
        if(current.right):
            current=current.right
        else:
            current=current.left
    while stack:
        ans.append(stack.pop())

def preOrder(node,ans):
    if(not node):
        return
    if(isLeaf(node)):
        ans.append(node.data)
    preOrder(node.left,ans)
    preOrder(node.right,ans)

def solve(node):
    ans=[]
    if(not node):
        return ans
    if(not isLeaf(node)):
        ans.append(node.data)
    addLeftBoundary(node,ans)
    preOrder(node,ans)
    addRightBoundary(node,ans)
    return ans
            

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.left.right=Node(9)
root.left.left.right.left=Node(1)
root.right.left=Node(7)
root.right.right=Node(6)
root.right.right.left=Node(8)
print(solve(root))
