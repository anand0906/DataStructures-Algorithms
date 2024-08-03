class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def find_depth(node,c=0):
    if node==None:
        return c-1
    left=find_depth(node.left,c+1)
    right=find_depth(node.right,c+1)
    return max(left,right)

def find_depth(node):
    if node==None:
        return -1
    left=1+find_depth(node.left)
    right=1+find_depth(node.right)
    return max(left,right)

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
root.right.right.right=Node('E')
print(find_depth(root))
