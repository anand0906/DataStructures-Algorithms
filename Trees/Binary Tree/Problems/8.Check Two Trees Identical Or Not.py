class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def InOrder(node,ans):
    if(node is None):
        return
    InOrder(node.left,ans)
    ans.append(node.data)
    InOrder(node.right,ans)

def bruteForce(root1,root2): # works for only nodes having different values
    ans1=[]
    InOrder(root1,ans1)
    ans2=[]
    InOrder(root2,ans2)
    return ans1==ans2

def optimized(node1,node2):
    if(node1==None and node2==None):
        return True
    if((node1==None and node2!=None) or (node1!=None and node2==None)):
        return False
    a=(node1.data==node2.data)
    b=optimized(node1.left,node2.left)
    c=optimized(node1.right,node2.right)
    return a and b and c

root1=Node(4)
root1.left=Node(2)
root1.right=Node(5)
root2=Node(4)
root2.left=Node(2)
root2.right=Node(5)
print(bruteForce(root1,root2))
print(optimized(root1,root2))
root2.right=Node(10)
print(bruteForce(root1,root2))
print(optimized(root1,root2))
