class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def InOrder(node,arr):
    if not node:
        return
    InOrder(node.left,arr)
    arr.append(node.data)
    InOrder(node.right,arr)

def PreOrder(node,arr):
    if not node:
        return
    arr.append(node.data)
    PreOrder(node.left,arr)
    PreOrder(node.right,arr)

def PostOrder(node,arr):
    if not node:
        return
    PostOrder(node.left,arr)
    PostOrder(node.right,arr)
    arr.append(node.data)

from collections import deque
def LevelOrder(node):
    ans=[]
    if(not node):
        return ans
    queue=deque()
    queue.append(node)
    while queue:
        current=queue.popleft()
        ans.append(current.data)
        if(current.left):
            queue.append(current.left)
        if(current.right):
            queue.append(current.right)
    return ans

def LevelOrder_Print_LevelWise(node):
    ans=[]
    if not node:
        return ans
    queue=deque()
    queue.append(node)
    while queue:
        n=len(queue)
        level=[]
        for i in range(n):
            current=queue.popleft()
            level.append(current.data)
            if(current.left):
                queue.append(current.left)
            if(current.right):
                queue.append(current.right)
        ans.append(level)
    return ans
    

def main(root):
    #InOrder
    arr=[]
    InOrder(root,arr)
    print(arr)
    #PreOrder
    arr=[]
    PreOrder(root,arr)
    print(arr)
    #PostOrder
    arr=[]
    PostOrder(root,arr)
    print(arr)
    #LevelOrder
    ans=LevelOrder(root)
    print(ans)
    print(LevelOrder_Print_LevelWise(root))

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.left.right=Node(9)
root.left.left.right.left=Node(1)
root.right.left=Node(7)
root.right.right=Node(6)
root.right.right.left=Node(8)
main(root)


