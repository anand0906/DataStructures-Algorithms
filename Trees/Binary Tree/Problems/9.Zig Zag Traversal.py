class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
from collections import deque
def solve(node):
    ans=[]
    if not node:
        return []
    queue=deque()
    queue.append(node)
    reverse=False
    while queue:
        n=len(queue)
        level=[0]*n
        for i in range(n):
            temp=queue.popleft()
            pos=(n-i-1)if reverse else i
            level[pos]=temp.data
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)
        ans.append(level)
        reverse=(not reverse)
    return ans
            

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.left.right=Node(9)
root.left.left.right.left=Node(1)
root.right.left=Node(7)
root.right.right=Node(6)
root.right.right.left=Node(8)
print(solve(root))
