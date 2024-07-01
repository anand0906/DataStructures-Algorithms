from collections import defaultdict
class Log:

    def __init__(self,log):
        self.isStart=(log[-1]=="entry")
        self.time=int(log[0])
        self.func=log[1]
        self.children=[]
        self.total=0
        self.parent=None
        self.final=0

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.func)+"-"+repr(self.total)+"-"+repr(self.final)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return self.func


def find(node):
    if not node.children:
        node.final=node.total
        return node.final
    sum=0
    for child in node.children:
        sum+=find(child)
    node.final=(sum+node.total)
    return node.final

def findHotPath(node):
    print(node.func,time[node.func],sep=":",end="->")
    if(node.children):
        temp=max(node.children,key=lambda x:x.final)
        findHotPath(temp)

n=int(input())
logs=[input().split() for i in range(n)]
prev=0
final=[]
stack=[]
current=None
time={}
for log in logs:
    temp=Log(log)
    if temp.func not in time:
        time[temp.func]=0
    if(temp.isStart):
        if(not stack):
            root=temp
            final.append(root)
            stack.append(root)
            current=root
            prev=root.time
        else:
            peek=stack[-1]
            peek.total+=(temp.time-prev)
            time[peek.func]+=(temp.time-prev)
            prev=temp.time
            stack.append(temp)
            temp.parent=peek
            peek.children.append(temp)
            current=temp
            
    else:
        peek=stack[-1]
        tem=stack.pop()
        tem.total+=(temp.time-prev)
        time[peek.func]+=(temp.time-prev)
        prev=temp.time
for i in final:
    print(i)
find(final[-1])
findHotPath(final[-1])
