class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def checkTree(node):
    if not node:
        return True
    left=checkTree(node.left)
    right=checkTree(node.right)
    if (left==False or right==False):
        return False
        
    childSum=0
    if(node.left):
        childSum+=node.left.data
    if(node.right):
        childSum+=node.right.data
    if(node.left or node.right):
        if(childSum==node.data):
            return True
        else:
            return False
    return True
    



root=Node(4)
root.left=Node(1)
root.right=Node(3)
root.left.right=Node(1)
print(checkTree(root))

