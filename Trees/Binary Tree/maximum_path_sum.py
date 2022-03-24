class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def height(node):
    global maxi
    if node is None:
        return -1
    else:
        leftsum=height(node.left)
        rightsum=height(node.right)
        maxi=max(maxi,leftsum+rightsum+node.data)
        return node.data+max(leftsum,rightsum)


root=Node(1)
root.left=Node(2)
root.right=Node(1)
root.left.left=Node(4)
root.left.left.left=Node(1)
maxi=-float('inf')
height(root)
print(maxi)

