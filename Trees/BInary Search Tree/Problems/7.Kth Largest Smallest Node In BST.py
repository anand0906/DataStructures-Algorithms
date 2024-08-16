class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(node,arr):
    if not node:
        return
    inorder(node.left,arr)
    arr.append(node.data)
    inorder(node.right,arr)
    

def smallestBruteForce(root,k):
    ans=None
    if not root:
        return ans
    arr=[]
    inorder(root,arr)
    n=len(arr)
    if(k>n):
        return ans
    ans=arr[k-1]
    return ans

def inOrder(node,k,count,ans):
    if not node:
        return
    inOrder(node.left,k,count,ans)
    count[0]+=1
    if(count[0]==k):
        ans[0]=node.data
    inOrder(node.right,k,count,ans)

def smallestOptimized(root,k):
    ans=None
    if not root:
        return ans
    ans=[None]
    count=[0]
    inOrder(root,k,count,ans)
    return ans[0]


def reverseInorder(node,arr):
    if not node:
        return
    reverseInorder(node.right,arr)
    arr.append(node.data)
    reverseInorder(node.left,arr)

    

def largestBruteForce(root,k):
    ans=None
    if not root:
        return ans
    arr=[]
    reverseInorder(root,arr)
    n=len(arr)
    if(k>n):
        return ans
    ans=arr[k-1]
    return ans

def reverseInOrder(node,k,count,ans):
    if not node:
        return
    reverseInOrder(node.right,k,count,ans)
    count[0]+=1
    if(count[0]==k):
        ans[0]=node.data
    reverseInOrder(node.left,k,count,ans)

def largestOptimized(root,k):
    ans=None
    if not root:
        return ans
    ans=[None]
    count=[0]
    reverseInOrder(root,k,count,ans)
    return ans[0]





root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
k=2
print(smallestBruteForce(root,k))
print(smallestOptimized(root,k))
print(largestBruteForce(root,k))
print(largestOptimized(root,k))

