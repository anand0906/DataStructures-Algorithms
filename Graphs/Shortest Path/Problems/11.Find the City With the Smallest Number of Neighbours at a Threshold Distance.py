nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i)-1,int(j)-1,int(w)) for i,j,w in edges]
threshold=int(input())
graph=[[float('inf')]*nodes for i in range(nodes)]
for i,j,w in edges_converted:
    graph[i][j]=w
    graph[j][i]
for i in range(nodes):
    graph[i][i]=0
for k in range(nodes):
    for i in range(nodes):
        for j in range(nodes):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
finalCity=0
maxCnt=float('inf')
for i in range(nodes):
    city=i
    cnt=0
    for j in range(nodes):
        if(graph[i][j]<=threshold):
            cnt+=1
        if(cnt<=maxCnt):
            maxCnt=cnt
            finalCity=city
print(finalCity)
