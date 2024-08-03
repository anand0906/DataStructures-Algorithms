class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def preorder_list(self,final=[]):
        final.append(self.data)
        if self.left:
            self.left.preorder_list(final)
        if self.right:
            self.right.preorder_list(final)
        return final

    def preorder_iterative(self):
        stack=[]
        stack.append(self)
        final=[]
        while stack:
            temp=stack.pop()
            final.append(temp.data)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        print(final)

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
root.preorder()
print(root.preorder_list([]))
root.preorder_iterative()
