class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def ceil(root,target):
    node=root
    ans=-1
    while node:
        if(node.data==target):
            ans=node.data
            break
        elif(target>node.data):
            node=node.right
        else:
            ans=node.data
            node=node.left
    return ans

def floor(root,target):
    node=root
    ans=-1
    while node:
        if(node.data==target):
            ans=node.data
            break
        elif(target>node.data):
            ans=node.data
            node=node.right
        else:
            node=node.left
    return ans


root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
target=int(input())
print(ceil(root,target))
print(floor(root,target))
