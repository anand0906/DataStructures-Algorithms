
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
from collections import deque
def InOrder(node,target):
    if not node:
        return None
    if(node.data==target):
        return node
    left=InOrder(node.left,target)
    right=InOrder(node.right,target)
    if(left):
        return left
    if(right):
        return right
    return None

def findNode(root,target):
    if(not root):
        return None
    node=InOrder(root,target)
    return node
def assignParent(root):
    queue=deque()
    queue.append(root)
    root.parent=None
    while queue:
        n=len(queue)    
        for i in range(n):
            node=queue.popleft()
            if(node.left):
                node.left.parent=node
                queue.append(node.left)
            if(node.right):
                node.right.parent=node
                queue.append(node.right)
    



def solve(root,target):
    ans=[]
    if(not root):
        return ans
    node=findNode(root,target)
    assignParent(root)
    queue=deque()
    queue.append(node)
    level=0
    visited={}
    visited[node]=True
    while queue:
        n=len(queue)
        for i in range(n):
            node=queue.popleft()
            visited[node]=True
            if(node.left and not visited.get(node.left)):
                queue.append(node.left)
            if(node.right and not visited.get(node.right)):
                queue.append(node.right)
            if(node.parent and not visited.get(node.parent)):
                queue.append(node.parent)
        level+=1
    ans=level-1
    return ans
        
    
    
root=Node(4)
root.left=Node(1)
root.right=Node(3)
root.left.right=Node(1)
target=int(input())
print(solve(root,target))

