class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
prev=None
def revPostOrder(node):
    global prev
    if not node:
        return
    revPostOrder(node.right)
    revPostOrder(node.left)
    node.right=prev
    node.left=None
    prev=node


def bruteForce(root):
    global prev
    prev=None
    if not root:
        return None
    revPostOrder(root)
    return root

def better(root):
    if not root:
        return None
    stack=[]
    stack.append(root)
    while stack:
        current=stack.pop()
        if(current.right):
            stack.append(current.right)
        if(current.left):
            stack.append(current.left)
        current.right=stack[-1] if stack else None
        current.left=None
    return root

def optimized(root):
    if not root:
        return None
    current=root
    while current:
        if(current.left):
            rightMost=current.left
            while rightMost.right:
                rightMost=rightMost.right
            rightMost.right=current.right
            current.right=current.left
            current.left=None
        current=current.right
    return root
            


def display(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.right
    print()
    
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
head=bruteForce(root)
display(head)
head=better(root)
display(head)
head=optimized(root)
display(head)
