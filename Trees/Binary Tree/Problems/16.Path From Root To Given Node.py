class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def findPath(node,target,ans):
    if(not node):
        return False
    ans.append(node.data)
    if(node.data==target):
        return True
    a=findPath(node.left,target,ans)
    b=findPath(node.right,target,ans)
    if(a or b):
        return True
    ans.pop()
    return False

def solve(root,target):
    ans=[]
    if not root:
        return ans
    findPath(root,target,ans)
    return ans
        
        
    


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
print(solve(root,2))
