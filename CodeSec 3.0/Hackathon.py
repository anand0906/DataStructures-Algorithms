class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []
        self.locked=False
        self.lockedDesc=[]
        self.UID=None

    def __repr__(self):
        return str(self.data)

class Solution:

    def __init__(self,root):
        self.root=root

    def informAncestors(self,node):
        temp=node.parent
        while temp:
            temp.lockedDesc+=[node]
            temp=temp.parent

    def checkAncestorLock(self,node):
        temp=node.parent
        while temp:
            if(temp.locked):
                return True
            temp=temp.parent
        return False

    def lock(self,node,uid):
        if(node.locked):
            return False
        if(node.lockedDesc):
            return False
        if(self.checkAncestorLock(node)):
            return False
        node.locked=True
        node.UID=uid
        self.informAncestors(node)
        return True

    def unlock(self,node,uid):
        if(not node.locked):
            return False
        if(node.UID!=uid):
            return False
        node.locked=False
        node.UID=None
        temp=node.parent
        while temp:
            temp.lockedDesc.remove(node)
            temp=temp.parent
        return True

    def upgrade(self,node,uid):
        if(node.locked):
            return False
        if(not node.lockedDesc):
            return False
        if(self.checkAncestorLock(node)):
            return False
        for i in node.lockedDesc:
            if(i.UID!=uid):
                return False
        while node.lockedDesc:
            temp=node.lockedDesc[0]
            temp,self.unlock(temp,uid)
        self.lock(node,uid)
        return True
        
        
    
def generateTree(n, m, nodes):
    root = nodes[0]
    for i in range(n):
        parent = nodes[i]
        for j in range(1, m + 1):
            index = i * m + j
            if index < n:
                child = nodes[index]
                child.parent = parent
                parent.children.append(child)
            else:
                break
    return root


def printTree(node, level=0):
    print(" " * (level * 4),node,"Locked Descendents :",node.lockedDesc,"Is Locked :",node.locked)
    for child in node.children:
        printTree(child, level + 1)

def solve(n,m,q,nodes,queries):
    nodes_map={i:Node(i) for i in nodes}
    root=generateTree(n,m,list(nodes_map.values()))
    #printTree(root)
    obj=Solution(root)
    for i in range(q):
        id,node,uid=queries[i].split()
        #print(id,node,uid)
        if(id=='1'):
            print(obj.lock(nodes_map[node],uid))
        if(id=='2'):
            print(obj.unlock(nodes_map[node],uid))
        if(id=='3'):
            print(obj.upgrade(nodes_map[node],uid))
        #printTree(root)
    

n=int(input())
m=int(input())
q=int(input())
nodes=[input() for i in range(n)]
queries=[input() for i in range(q)]
solve(n,m,q,nodes,queries)
