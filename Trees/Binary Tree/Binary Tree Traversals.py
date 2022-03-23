#Two Type of Traversals
#1.Depth First Traversal
#  1.Inorder
#  2.Preorder
#  3.Postorder
#2.Breadth First Traversal
#  1.Level Order


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder()

    def inorder_iterative(self):
        stack=[]
        final=[]
        node=self
        while True:
            if node:
                stack.append(node)
                node=node.left
            else:
                if not stack:
                    break
                node=stack.pop()
                final.append(node.data)
                node=node.right
        print(final)
                


    def preorder(self):
        print(self.data,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def preorder_iterative(self):
        #Tc-O(n)
        #Sc-O(n)
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
            
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data,end=" ")

    def postorder_iterative(self):
        stack=[]
        stack2=[]
        final=[]
        stack.append(self)
        while stack:
            temp=stack.pop()
            stack2.append(temp)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        while stack2:
            final.append(stack2.pop().data)
        print(final)

    def postorder_iterative2(self):
        stack=[]
        pass
            
                
            

    def levelorder(self):
        #Tc-O(n)
        #Sc-O(n)
        temp=[]
        temp.append(self)
        while temp:
            k=temp.pop(0)
            print(k.data,end=" ")
            if k.left:
                temp.append(k.left)
            if k.right:
                temp.append(k.right)
            

    def __str__(self):
        return str(self.data)
root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
root.inorder()
root.inorder_iterative()
root.postorder()
root.postorder_iterative()
root.preorder()
root.preorder_iterative()
root.levelorder()
