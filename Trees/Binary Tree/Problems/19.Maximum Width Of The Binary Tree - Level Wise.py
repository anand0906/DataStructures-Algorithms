class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque
def solve(node):
    ans=0
    if not node:
        return ans
    queue=deque()
    queue.append((node,1))
    level=0
    store={}
    while queue:
        n=len(queue)
        for i in range(n):
            node,x=queue.popleft()
            if(i==0):
                first=x
            if(i==n-1):
                last=x
            if(node.left):
                queue.append((node.left,2*x+1))
            if(node.right):
                queue.append((node.right,2*x+2))
            ans=max(ans,(last-first+1))
    return ans


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
print(solve(root))

