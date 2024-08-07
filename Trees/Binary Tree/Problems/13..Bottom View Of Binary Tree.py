class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque
def solve(node):
    ans=[]
    if not node:
        return ans
    queue=deque()
    queue.append((node,0))
    level=0
    store={}
    while queue:
        n=len(queue)
        for i in range(n):
            node,x=queue.popleft()
            if x not in store:
                store[x]=node.data
            else:
                store[x]=node.data
            if(node.left):
                queue.append((node.left,x-1))
            if(node.right):
                queue.append((node.right,x+1))
    temp=sorted(store.items(),key=lambda x:x[0])
    for x,data in temp:
        ans.append(data)
    return ans
        
        
    


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
print(solve(root))
