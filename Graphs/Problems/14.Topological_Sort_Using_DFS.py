
def dfs(node,visited):
    global stack
    visited[node]=True
    for i in graph[node]:
        if(not visited[i]):
            dfs(i,visited)
    stack.append(node)

def bfs():
    inDegree={i:0 for i in range(1,n+1)}
    for i,j in edges:
        inDegree[j]+=1
    queue=[]
    for i,j in inDegree.items():
        if(j==0):
            queue.append(i)
    final=[]
    while queue:
        temp=queue.pop(0)
        final.append(temp)
        for i in graph[temp]:
            inDegree[i]-=1
            if(inDegree[i]<=0):
                queue.append(i)
    print(final)
n=int(input())
e=int(input())
edges=[tuple(map(int,input().split())) for i in range(e)]
graph={i:[] for i in range(1,n+1)}
for i,j in edges:
    if j not in graph[i]:
        graph[i].append(j)
visited={i:False for i in range(1,n+1)}
stack=[]
for i in range(1,n+1):
    if(not visited[i]):
        dfs(i,visited)
print(stack[::-1])
bfs()
