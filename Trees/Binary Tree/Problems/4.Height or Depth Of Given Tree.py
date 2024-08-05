class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def findHeight(node):
    if not node:
        return 0
    leftHeight=findHeight(node.left)
    rightHeight=findHeight(node.right)
    return 1+max(leftHeight,rightHeight)

from collections import deque
def findHeight2(node):
    if not node:
        return 0
    queue=deque()
    queue.append(node)
    level=0
    while queue:
        n=len(queue)

        for i in range(n):
            temp=queue.popleft()
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)
        level+=1
    return level

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.left.right=Node(9)
root.left.left.right.left=Node(1)
root.right.left=Node(7)
root.right.right=Node(6)
root.right.right.left=Node(8)
print(findHeight(root))
print(findHeight2(root))

