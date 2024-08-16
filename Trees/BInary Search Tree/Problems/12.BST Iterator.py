class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
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
    


root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)

iterable=Iterator(root)
print(iterable.next())
print(iterable.next())
print(iterable.next())
print(iterable.next())
print(iterable.hasNext())
print(iterable.next())
print(iterable.next())
print(iterable.next())
print(iterable.hasNext())
