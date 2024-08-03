class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def height(node):
    if node is None:
        return 0
    else:
        left=height(node.left)
        right=height(node.right)
        return 1+max(left,right)
#o(n**2)
def diameter(node):
    global maxi
    if node is None:
        return
    left_height=height(node.left)
    right_height=height(node.right)
    maxi=max(maxi,left_height+right_height)
    diameter(node.left)
    diameter(node.right)



def height(node):
    global maxi
    if node is None:
        return 0
    else:
        left=height(node.left)
        right=height(node.right)
        maxi=max(maxi,left+right)
        return 1+max(left,right)

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.left.left=Node('E')
maxi=0
height(root)
print(maxi)

