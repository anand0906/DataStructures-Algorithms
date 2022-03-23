class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def traversal(self):
        stack=[]
        stack.append([self,1])
        preorder,postorder,inorder=[],[],[]
        while stack:
            top=stack[-1]
            if(top[1]==1):
                top[1]+=1
                preorder.append(top[0].data)
                if(top[0].left):
                    stack.append([top[0].left,1])
            elif(top[1]==2):
                top[1]+=1
                inorder.append(top[0].data)
                if top[0].right:
                    stack.append([top[0].right,1])
            else:
                postorder.append(top[0].data)
                stack.pop()
        print("preorder",*preorder,sep=" ")
        print("inorder",*inorder,sep=" ")
        print("postorder",*postorder,sep=" ")

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
root.traversal()
        
        
