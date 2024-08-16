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
    
def findUpperBound(n,arr,k):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def bruteforce(root,k):
    ans=None
    if not root:
        return ans
    arr=[]
    inorder(root,arr)
    n=len(arr)
    index=findUpperBound(n,arr,k)
    if index==n:
        return -1
    ans=arr[index]
    return ans


def optimized(root,k):
    ans=None
    if not root:
        return ans
    node=root
    while node:
        if(k>=node.data):
            node=node.right
        else:
            ans=node.data
            node=node.left
    if not ans:
        return -1
    return ans
    


root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
k=8
print(bruteforce(root,k))
print(optimized(root,k))
