class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)


def height(node):
    global diameter
    if node is None:
        return 0
    else:
        left_hieght=height(node.left)
        right_hiegth=height(node.right)
        if left_hieght==-1 or right_hiegth==-1:
            return -1
        if abs(left_hieght-right_hiegth)>1:
            return -1
        return 1+max(left_hieght,right_hiegth)

root=Node('A')
root.left=Node('B')
root.right=Node('c')
root.left.left=Node('E')
root.left.left.left=Node('D')
diameter=-float('inf')
print(height(root))
