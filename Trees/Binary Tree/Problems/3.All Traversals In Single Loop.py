class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def solve(node):
    preOrder,inOrder,postOrder=[],[],[]
    if(not node):
        return preOrder,inOrder,postOrder
    stack=[]
    stack.append([node,1])
    while stack:
        current,cnt=stack.pop()
        if(cnt==1):
            preOrder.append(current.data)
            cnt+=1
            stack.append([current,cnt])
            if(current.left):
                stack.append([current.left,1])
        elif(cnt==2):
            inOrder.append(current.data)
            cnt+=1
            stack.append([current,cnt])
            if(current.right):
                stack.append([current.right,1])
        else:
            postOrder.append(current.data)
    return preOrder,inOrder,postOrder

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
