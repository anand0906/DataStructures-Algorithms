class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def inorder_list(self,final=[]):
        if self.left:
            self.left.inorder_list(final)
        final.append(self.data)
        if self.right:
            self.right.inorder_list(final)
        return final

    def inorder_iterative(self):
        stack=[]
        final=[]
        current=self
        while True:
            if current:
                stack.append(current)
                current=current.left
            else:
                if not stack:
                    break
                else:
                    current=stack.pop()
                    final.append(current.data)
                    current=current.right
        print(final)

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
root.inorder()
print(root.inorder_list([]))
root.inorder_iterative()
