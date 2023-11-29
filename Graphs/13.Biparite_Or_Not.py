def bfs(graph,i,col):
    global color
    queue=[(i,col)]
    color[i]=col
    while queue:
        temp=queue.pop(0)
        j,c=temp
        for k in graph[j]:
            if(color[k]==-1):
                color[k]=(int(not c))
                queue.append((k,int(not c)))
            elif(color[k]==c):
                return False
    return True

def dfs(i,col):
    global color
    color[i]=col
    for j in graph[i]:
        if(color[j]==-1):
            temp=dfs(j,int(not col))
            if(temp==False):
                return False
        elif(color[j]==col):
            return False
    return True


n=int(input("Enter number of nodes : "))
e=int(input("Enter number of edges : "))
edges=[list(map(int,input().split())) for i in range(e)]
graph={i:set() for i in range(1,n+1)}
for i,j in edges:
    graph[i].add(j)
    graph[j].add(i)
color={i:-1 for i in range(1,n+1)}
for i in range(1,n+1):
    if(color[i]==-1):
        temp=bfs(graph,i,0)
        if(not temp):
            print("It is not biparite graph")
            break
else:
    print("It is biparite graph")

color={i:-1 for i in range(1,n+1)}
for i in range(1,n+1):
    if(color[i]==-1):
        temp=dfs(i,0)
        if(not temp):
            print("It is not biparite graph")
            break
else:
    print("It is biparite graph")
    
