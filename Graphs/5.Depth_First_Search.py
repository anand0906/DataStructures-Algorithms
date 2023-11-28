def dfs(i,graph):
    global visited
    if(not visited[i]):
        print(i,end="->")
        visited[i]=True
        for j in graph[i]:
            if(not visited[j]):
                dfs(j,graph)

def iterative(graph):
    visited={i:False for i in range(1,n+1)}
    stack=[]
    for i in range(1,n+1):
        if(not visited[i]):
            visited[i]=True
            stack.append(i)
            while stack:
                temp=stack.pop()
                print(temp,end="->")
                for j in graph[temp]:
                    if(not visited[j]):
                        stack.append(j)
                        visited[j]=True
                
    
n=int(input("Enter Number Of Nodes : "))
e=int(input("Enter Number of Edges : "))
edges=[input().split() for i in range(e)]
edges_converted=[(ord(i)-ord('A')+1,ord(j)-ord('A')+1) for i,j in edges]
graph={i:set() for i in range(1,n+1)}
for i,j in edges_converted:
    graph[i].add(j)
    graph[j].add(i)
visited={i:False for i in range(1,n+1)}
for i in range(1,n+1):
    if (not visited[i]):
        dfs(i,graph)
print()
iterative(graph)
