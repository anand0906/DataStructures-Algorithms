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

def bruteForce(preorder):
    if not preorder:
        return None
    inorder=sorted(preorder)
    n=len(preorder)
    root=solve(n,inorder,preorder)
    return root

def build(preorder,index,maxVal):
    if(index[0]>= len(preorder) or preorder[index[0]]>maxVal):
        return None
    node=Node(preorder[index[0]])
    index[0]+=1
    node.left=build(preorder,index,node.data)
    node.right=build(preorder,index,maxVal)
    return node
    

def optimized(preorder):
    if not preorder:
        return None
    index=[0]
    root=build(preorder,index,float('inf'))
    return root


    




preorder=[8,5,1,7,10,12]
root=bruteForce(preorder)
root=optimized(preorder)

