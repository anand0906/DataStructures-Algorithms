class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def InOrder(node):
    ans=[]
    if not node:
        return ans
    stack=[]
    current=node
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        else:
            if not stack:
                break
            current=stack.pop()
            ans.append(current.data)
            current=current.right
    return ans

def PreOrder(node):
    ans=[]
    if not node:
        return ans
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        ans.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return ans

def PostOrder(node):
    ans=[]
    if not node:
        return ans
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        ans.append(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    ans.reverse()
    return ans

def PostOrder_Using_One_Stack(node):
    ans=[]
    if not node:
        return ans
    current=node
    stack=[]
    while stack or current:
        if(current):
            stack.append(current)
            current=current.left
        else:
            temp=stack[-1].right
            if not temp:
                temp=stack.pop()
                ans.append(temp.data)
                while stack and temp==stack[-1].right:
                    temp=stack.pop()
                    ans.append(temp.data)
            else:
                current=temp
    return ans
        
            
def main(root):
    print(InOrder(root))
    print(PreOrder(root))
    print(PostOrder(root))
    print(PostOrder_Using_One_Stack(root))

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
