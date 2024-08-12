class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def changeTree(node):
    if not node:
        return
    childSum=0
    if(node.left):
        childSum+=node.left.data
    if(node.right):
        childSum+=node.right.data
    if(childSum>=node.data):
        node.data=childSum
    else:
        if(node.left):
            node.left.data=node.data
        if(node.right):
            node.right.data=node.data
    changeTree(node.left)
    changeTree(node.right)
    childSum=0
    if(node.left):
        childSum+=node.left.data
    if(node.right):
        childSum+=node.right.data
    if(node.left or node.right):
        node.data=childSum

def Inorder(node):
    if not node:
        return
    Inorder(node.left)
    print(node.data,end=" ")
    Inorder(node.right)
    



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
changeTree(root)
Inorder(root)

