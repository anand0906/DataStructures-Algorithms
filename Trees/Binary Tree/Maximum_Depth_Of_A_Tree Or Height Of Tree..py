class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def height(node):
    if node is None:
        return -1
    else:
        left_height=height(node.left)
        right_height=height(node.right)
        return 1+max(left_height,right_height)

def height(node,c=0):
    if node is None:
        return c-1
    else:
        left_height=height(node.left,c+1)
        right_height=height(node.right,c+1)
        return max(left_height,right_height)
    
root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
print(height(root))

