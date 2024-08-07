class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque,defaultdict
def default():
    return defaultdict(list)
def solve(node):
    ans=[]
    if not node:
        return ans
    queue=deque()
    queue.append((node,0))
    level=0
    store=defaultdict(default)
    while queue:
        n=len(queue)
        for i in range(n):
            node,x=queue.popleft()
            store[x][level].append(node.data)
            if(node.left):
                queue.append((node.left,x-1))
            if(node.right):
                queue.append((node.right,x+1))
        level+=1
    temp=sorted(store.items(),key=lambda x:x[0])
    for x,l_values in temp:
        vertical=[]
        l_values=sorted(l_values.items(),key=lambda x:x[0])
        for level,values in l_values:
            vertical.extend(sorted(values))
        ans.append(vertical)
    return ans
        
        
    


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)

print(solve(root))
