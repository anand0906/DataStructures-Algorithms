class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def findPath(node,target,ans):
    if(not node):
        return
    ans.append(node.data)
    if(node.data==target):
        return True
    a=findPath(node.left,target,ans)
    b=findPath(node.right,target,ans)
    if(a or b):
        return True
    ans.pop()
    return False
        
def bruteForce(root,target1,target2):
    ans=None
    if not root:
        return ans
    path1=[]
    findPath(root,target1,path1)
    path2=[]
    findPath(root,target2,path2)
    index=0
    n1,n2=len(path1),len(path2)
    while index<n1 and index<n2 and path1[index]==path2[index]:
        ans=path1[index]
        index+=1
    return ans

def lca(node,target1,target2):
    if not node:
        return None
    if(node.data==target1 or node.data==target2):
        return node
    left=lca(node.left,target1,target2)
    right=lca(node.right,target1,target2)
    if(left and right):
        return node
    if(left):
        return left
    else:
        return right



def optimized(root,target1,target2):
    ans=None
    if not root:
        return ans
    ans=lca(root,target1,target2)
    return ans.data


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
target1,target2=list(map(int,input().split()))
print(bruteForce(root,target1,target2))
print(optimized(root,target1,target2))
