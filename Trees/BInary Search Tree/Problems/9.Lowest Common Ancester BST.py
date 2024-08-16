class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def lca(node,node1,node2):
    if not node:
        return None
    current=node.data
    if(current > node1.data and current > node2.data):
        return lca(node.left,node1,node2)
    elif(current < node1.data and current < node2.data):
        return lca(node.right,node1,node2)
    else:
        return node


def solve(root,node1,node2):
    if not root:
        return None
    ans=lca(root,node1,node2)
    return ans.data


root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
print(solve(root,root.left.right,root.left.left))

