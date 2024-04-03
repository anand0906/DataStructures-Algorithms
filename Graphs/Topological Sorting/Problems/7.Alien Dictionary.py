n,k=list(map(int,input().split()))
words=input().split()
edges=[]
for i in range(1,len(words)):
    a,b=words[i],words[i-1]
    l=min(len(a),len(b))
    for i in range(l):
        if(a[i]!=b[i]):
            edges.append((b[i],a[i]))
            break
edges_converted=[(ord(i)-ord('a'),ord(j)-ord('a')) for i,j in edges]
nodes=k
graph={i:set() for i in range(nodes)}
indegree={i:0 for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    indegree[j]+=1
queue=[]
for i in range(nodes):
    if(indegree[i]==0):
        queue.append(i)
order=[]
while queue:
    currentNode=queue.pop(0)
    order.append(currentNode)
    for adj in graph[currentNode]:
        indegree[adj]-=1
        if(indegree[adj]==0):
            queue.append(adj)
print(*[chr(i+ord('a')) for i in order])
