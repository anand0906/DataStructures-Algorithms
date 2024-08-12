class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isSymmetric(leftNode,rightNode):
    if(leftNode==None or rightNode==None):
        return leftNode==rightNode
    if(leftNode.data!=rightNode.data):
        return False
    a=isSymmetric(leftNode.left,rightNode.right)
    b=isSymmetric(leftNode.right,rightNode.left)
    return a and b


def solve(root):
    if(root==None):
        return True
    return isSymmetric(root.left,root.right)

    
root=Node(1)
root.left=Node(2)
root.right=Node(2)
print(solve(root))
