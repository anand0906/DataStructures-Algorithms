class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def buildTree(postOrder,postStart,postEnd,inOrder,inStart,inEnd,index):
    if(postStart>postEnd or inStart>inEnd):
        return None
    root=Node(postOrder[postEnd])
    inRoot=index[postOrder[postEnd]]
    numsLeft=inRoot-inStart
    root.left=buildTree(postOrder,postStart,postStart+numsLeft-1,inOrder,inStart,inRoot-1,index)
    root.right=buildTree(postOrder,postStart+numsLeft,postEnd-1,inOrder,inRoot+1,inEnd,index)
    return root


def solve(n,inorder,postorder):
    root=None
    if(n==0):
        return root
    index={}
    for i in range(n):
        index[inorder[i]]=i
    postStart,postEnd=0,n-1
    inStart,inEnd=0,n-1
    root=buildTree(postorder,postStart,postEnd,inorder,inStart,inEnd,index)
    return root

def InOrder(node):
    if not node:
        return
    InOrder(node.left)
    print(node.data,end="->")
    InOrder(node.right)

inorder =[40, 20, 50, 10, 60, 30]
postorder =[40, 50, 20, 60, 30, 10]
n=len(postorder)
root=solve(n,inorder,postorder)
InOrder(root)
    
