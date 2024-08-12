class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def solve(root):
    ans=[]
    if not root:
        return ans
    current=root
    while current:
        if(current.left==None):
            ans.append(current.data)
            current=current.right
        else:
            rightMost=current.left
            while rightMost.right and rightMost.right!=current:
                rightMost=rightMost.right
            if(rightMost.right==None):
                rightMost.right=current
                ans.append(current.data)
                current=current.left
            else:
                rightMost.right=None
                current=current.right
    return ans

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print(solve(root))
