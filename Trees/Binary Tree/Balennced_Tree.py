class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def height(node):
    if node is None:
        return -1
    else:
        left=height(node.left)
        right=height(node.right)
        return 1+max(left,right)
def check(node):
    if node is None:
        return True
    lh=height(node.left)
    rh=height(node.right)
    diff=abs(lh-rh)
    check_left=check(node.left)
    check_right=check(node.right)
    if diff<=1 and check_left and check_right:
        return True
    else:
        return False


def check(node):
    if node is None:
        return 0
    left=check(node.left)
    right=check(node.right)
    diff=abs(left-right)
    if left==-1 or right==-1 or diff>1:
        return -1
    return 1+max(left,right)

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.left.left=Node('E')
print(check(root.left.left))

