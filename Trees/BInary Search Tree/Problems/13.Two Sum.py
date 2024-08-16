class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class ReverseIterator:
    def __init__(self,root):
        self.root=root
        self.stack=[]
        self.pushAllRight(root)

    def pushAllRight(self,root):
        node=root
        while node:
            self.stack.append(node)
            node=node.right

    def hasNext(self):
        return len(self.stack)!=0

    def next(self):
        top=self.stack.pop()
        self.pushAllRight(top.left)
        return top.data

class Iterator:
    def __init__(self,root):
        self.root=root
        self.stack=[]
        self.pushAllLeft(root)

    def pushAllLeft(self,root):
        node=root
        while node:
            self.stack.append(node)
            node=node.left

    def hasNext(self):
        return len(self.stack)!=0

    def next(self):
        top=self.stack.pop()
        self.pushAllLeft(top.right)
        return top.data
    
def solve(root,target):
    if not root:
        return False
    left=Iterator(root)
    right=ReverseIterator(root)
    l,r=left.next(),right.next()
    while l<r:
        if(l+r==target):
            return True
        elif(l+r<target):
            l=left.next()
        else:
            r=right.next()
    return False

root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
target=17
print(solve(root,target))
