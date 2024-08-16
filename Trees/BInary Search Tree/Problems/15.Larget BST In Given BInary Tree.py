class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class NodeValue:
    def __init__(self,max,min,size):
        self.max=max
        self.min=min
        self.size=size

def postOrder(node):
    if(not node):
        return NodeValue(float('inf'),float('-inf'),0)
    left=postOrder(node.left)
    right=postOrder(node.right)
    if(left.max<node.data<right.min):
        return NodeValue(min(node.data,left.min),max(node.data,right.max),left.size+right.size+1)
    return NodeValue(float('-inf'),float('inf'),max(left.size,right.size))
	

def solve(root):
    if not root:
        return None
    return postOrder(root).size


root = Node(1)
root.left = Node(4)
root.right = Node(4)
root.left.left = Node(6)
root.left.right = Node(8)
print(solve(root))
