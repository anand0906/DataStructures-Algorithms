class Node:
    def __init__(self,data,start):
        self.data=data
        self.children=[]
        self.parent=None
        self.total=0
        self.start=start

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret




n=int(input())
arr=[input().split() for i in range(n)]
root=Node(arr[0][1],int(arr[0]))
stack=[root]
current=root
for i in range(1,n):
    time,data,status=arr[i]
    time=int(time)
    if(data==stack[-1].data and status=="exit"):
        stack.pop()
    else:
        current=stack[-1]
        if(current.children and current.children[-1].data==data):
            continue
        node=Node(data)
        stack.append(node)
        node.parent=current
        current.children.append(node)
        current=node
print(root)
    
          
