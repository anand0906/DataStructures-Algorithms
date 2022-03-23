class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def postorder_list(self,final=[]):
        if self.left:
            self.left.postorder_list(final)
        if self.right:
            self.right.postorder_list(final)
        final.append(self.data)
        return final

    def postorder_iterative(self):
        stack=[]
        stack.append(self)
        stack2=[]
        while stack:
            temp=stack.pop()
            stack2.append(temp.data)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        while stack2:
            print(stack2.pop())

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
root.postorder()
print(root.postorder_list([]))
root.postorder_iterative()
