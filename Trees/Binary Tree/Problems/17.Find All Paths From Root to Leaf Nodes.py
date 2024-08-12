class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def findPath(node,ans,total):
    if(not node):
        return
    ans.append(node.data)
    findPath(node.left,ans,total)
    findPath(node.right,ans,total)
    if(node.left==None and node.right==None):
        total.append(ans.copy())
    ans.pop()

def solve(root):
    ans=[]
    total=[]
    if not root:
        return []
    findPath(root,ans,total)
    return total
        
        
    


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
print(solve(root))
