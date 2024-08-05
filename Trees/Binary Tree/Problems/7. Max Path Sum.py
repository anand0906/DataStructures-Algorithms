class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def maxSum(node,maxi):
    if not node:
        return 0
    leftSum=max(0,maxSum(node.left,maxi))
    rightSum=max(0,maxSum(node.right,maxi))
    maxi[0]=max(maxi[0],leftSum+rightSum+node.data)
    return node.data+max(leftSum,rightSum)

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.left.right=Node(9)
root.left.left.right.left=Node(1)
root.right.left=Node(7)
root.right.right=Node(6)
root.right.right.left=Node(8)
maxi=[float('-inf')]
maxSum(root,maxi)
print(maxi[0])
