class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def buildTree(preOrder,preStart,preEnd,inOrder,inStart,inEnd,index):
    if(preStart>preEnd or inStart>inEnd):
        return None
    root=Node(preOrder[preStart])
    inRoot=index[preOrder[preStart]]
    numsLeft=inRoot-inStart
    root.left=buildTree(preOrder,preStart+1,preStart+numsLeft,inOrder,inStart,inRoot-1,index)
    root.right=buildTree(preOrder,preStart+numsLeft+1,preEnd,inOrder,inRoot+1,inEnd,index)
    return root


def solve(n,inorder,preorder):
    root=None
    if(n==0):
        return root
    index={}
    for i in range(n):
        index[inorder[i]]=i
    preStart,preEnd=0,n-1
    inStart,inEnd=0,n-1
    root=buildTree(preorder,preStart,preEnd,inorder,inStart,inEnd,index)
    return root

def InOrder(node):
    if not node:
        return
    InOrder(node.left)
    print(node.data,end="->")
    InOrder(node.right)

inorder =[40, 20, 50, 10, 60, 30]
preorder =[10, 20, 40, 50, 30, 60]
n=len(preorder)
root=solve(n,inorder,preorder)
InOrder(root)
    
