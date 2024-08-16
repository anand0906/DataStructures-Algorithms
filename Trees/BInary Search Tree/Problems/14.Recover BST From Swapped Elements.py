class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(node,prev,swapped):
    if not node:
        return None
    inorder(node.left,prev,swapped)
    if(prev[0] and node.data < prev[0].data):
        if(swapped[0]==None):
            swapped[0]=prev[0]
            swapped[1]=node
        else:
            swapped[2]=node
    prev[0]=node
    inorder(node.right,prev,swapped)
	

def solve(root):
    if not root:
        return None
    swapped=[None,None,None]
    prev=[None]
    inorder(root,prev,swapped)
    if(swapped[0] and swapped[2]):
        swapped[0].data,swapped[2].data=swapped[2].data,swapped[0].data
    else:
        swapped[0].data,swapped[1].data=swapped[1].data,swapped[0].data
    return root

def inOrder(node,ans):
    if not node:
        return None
    inOrder(node.left,ans)
    ans.append(node.data)
    inOrder(node.right,ans)


root = Node(3)
root.left = Node(5)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
ans=[]
inOrder(root,ans)
print(ans)
solve(root)
ans=[]
inOrder(root,ans)
print(ans)
