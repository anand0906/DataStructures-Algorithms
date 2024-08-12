class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


from collections import deque
def serialize(root):
    ans=[]
    if not root:
        return ""
    queue=deque()
    queue.append(root)
    ans.append(str(root.data))
    while queue:
        n=len(queue)
        for i in range(n):
            node=queue.popleft()
            if(node.left):
                queue.append(node.left)
                ans.append(str(node.left.data))
            else:
                ans.append("#")
            if(node.right):
                queue.append(node.right)
                ans.append(str(node.right.data))
            else:
                ans.append("#")
    s=",".join(ans)
    return s


def deserialize(s):
    if not s:
        return None
    arr=s.split(',')
    queue=deque()
    index=0
    root=Node(arr[index])
    queue.append(root)
    index+=1
    while queue:
        node=queue.popleft()
        if(arr[index]=="#"):
            node.left=None
        else:
            new=Node(arr[index])
            node.left=new
            queue.append(new)
        index+=1
        if(arr[index]=="#"):
            node.right=None
        else:
            new=Node(arr[index])
            node.right=new
            queue.append(new)
        index+=1
    return root
        
        
    


root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.right=Node(5)
a=serialize(root)
print(a)
b=deserialize(a)
print(serialize(b)==a)
