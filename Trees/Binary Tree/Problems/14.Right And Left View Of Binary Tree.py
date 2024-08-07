class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque
def solve(node):
    left,right=[],[]
    if not node:
        return left,right
    queue=deque()
    queue.append(node)
    level=[]
    while queue:
        n=len(queue)
        for i in range(n):
            node=queue.popleft()
            level.append(node.data)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        left.append(level[0])
        right.append(level[n-1])
        level=[]
    return left,right

def leftView(node,level,ans):
    if(not node):
        return
    if(level==len(ans)):
        ans.append(node.data)
    leftView(node.left,level+1,ans)
    leftView(node.right,level+1,ans)

def rightView(node,level,ans):
    if(not node):
        return
    if(level==len(ans)):
        ans.append(node.data)
    rightView(node.right,level+1,ans)
    rightView(node.left,level+1,ans)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
print(solve(root))
ans=[]
leftView(root,0,ans)
ans2=[]
rightView(root,0,ans2)
print(ans,ans2)


