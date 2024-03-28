
<h2>Shortest Path in Undirected Graph with unit distance</h2>
<p><strong>Given an Undirected Graph having unit weight, find the shortest path from the source to all other nodes in this graph. In this problem statement, we have assumed the source vertex to be ‘0’. If a vertex is unreachable from the source node, then return -1 for that vertex.</strong></p>
<img src="https://takeuforward.org/wp-content/uploads/2022/10/image-19.png">
<p><strong>Input:</strong></p>
<p>n = 9, m = 10</p>
<p>edges = [[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]</p>
<p>src=0</p>
<p><strong>Output:</strong> 0 1 2 1 2 3 3 4 4</p>
<p><strong>Explanation:</strong></p>
<p>The above output array shows the shortest path to all the nodes from the source vertex (0), Dist[0] = 0, 
Dist[1] = 1 , Dist[2] = 2 , …. Dist[8] = 4 Where Dist[node] is the shortest path between src and the node. For a node, if the value of Dist[node]= -1, then we conclude that the node is unreachable from the src node.</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/10/image-20.png">
<p><strong>Input:</strong></p>
<p>n = 8, m = 10</p>
<p>Edges =[[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]]</p>
<p>src=0</p>
<p><strong>Output:</strong> 0 1 2 1 2 3 3 2</p>
<p><strong>Explanation:</strong></p>
<p>The above output list shows the shortest path to all the nodes from the source vertex (0),  Dist[0] = 0, 
Dist[1] = 1, Dist[2] = 2,.....Dist[7] = 2</p>
<p><strong>Solution</strong></p>
<p>Here, we have to find the shortest distance from source to all other nodes in given graph</p>
<p>Since, each edge has unit weight. We can solve it using bfs</p>
<p>In BFS, we used to visit all nodes level wise from source node.</p>
<p>It guarantees that the first time a vertex is reached during traversal, it is reached by the shortest path. because, it visits nodes level by level in order.</p>
<p><strong>Steps To Solve : </strong></p>
<ul>
	<li>Create adjacency list for given graph</li>
	<li>Create a distance array which stores shortest distance of each node. Intialize with infinity by default</li>
	<li>create queue for bfs</li>
	<li>add source node (Node 0) to queue and update node 0's distance to 0 in distance array</li>
	<li>Proform bfs operation</li>
	<li>perform following step untill queue is empty</li>
	<ul>
		<li>pop node from queue</li>
		<li>loop through each of its adjacent nodes</li>
		<li>update its adjacent nodes distance in distance array by relaxing its distance</li>
		<li>if distance[currentNode]+1 < distance[adjacentNode] , then distance[adjacentNode]=distance[currentNode]+1</li>
	</ul>
	<li>Once all the nodes have been iterated, the dist[] array will store the shortest paths.</li>
</ul>

```python
nodes,edges=int(input()),int(input())
edges=[input().split() for i in range(edges)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    graph[j].add(i)
queue=[]
distance={i:float('inf') for i in range(nodes)}
source=0
distance[source]=0
queue.append(source)
while queue:
    current=queue.pop(0)
    for adj in graph[current]:
        if(distance[current]+1 < distance[adj]):
            distance[adj]=1+distance[current]
            queue.append(adj)
final_output={i:-1 for i in range(nodes)}
for i,j in distance.items():
	if(distance[i]!=float('inf')):
    	final_output[i]=j
print(final_output)
#print(final_output.values())
```
<p><strong>TC</strong> :O(nodes+edges)</p>
<p><strong>SC</strong> :O(nodes)</p>

<h2>Dijkstra’s Algorithm – Using Priority Queue</h2>
<p>Dijkstra's Algorithm is a widely used algorithm for finding the shortest path from a source vertex to all other vertices in a weighted graph, where the weight of each edge represents the distance between the vertices it connects.</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/11/Screenshot-2022-11-23-162337.png">
<p><strong>Input : </strong></p>
<p>V = 2</p>
<p>adj [] = {{{1, 9}}, {{0, 9}}}</p>
<p>S = 0</p>
<p><strong>Output:</strong></p>
<p>0 9</p>
<p><strong>Explanation: </strong></p>
<p>The source vertex is 0. Hence, the shortest distance of node 0 from the source is 0 and the shortest distance of node 1 from source will be 9.</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/11/Screenshot-2022-11-23-162453.png">
<p><strong>Input : </strong></p>
<p>V = 3, E = 3</p>
<p>adj = {{{1, 1}, {2, 6}}, {{2, 3}, {0, 1}}, {{1, 3}, {0, 6}}}</p>
<p>S = 2</p>
<p><strong>Output:</strong></p>
<p>4 3 0</p>
<p><strong>Explanation: </strong></p>
<p>For nodes 2 to 0, we can follow the path 2-1-0. This has a distance of 1+3 = 4, whereas the path 2-0 has a distance of 6. So, the Shortest path from 2 to 0 is 4.</p>
<p>The shortest distance from 0 to 1 is 1.</p>

<p><strong>Solution : </strong></p>
<p>Given an undirected weighted graph and source node</p>
<p>we need to find shortest distance from source node to all other nodes</p>
<p>Unlike previous problem, here we are having different weights on edges</p>
<p>Using bfs technique takes more time and not preferrable</p>
<p>but we can modify it to solve this problem more efficietly</p>
<p>Simply use priority queue instead of normal queue</p>
<p>By using min-heap, we always try to pop element which is having less node's distance</p>

<p><strong>Steps To Solve : </strong></p>
<ul>
	<li>Create adjacency list for given graph</li>
	<li>Create a distance array which stores shortest distance of each node. Intialize with infinity by default</li>
	<li>create proirity queue for bfs</li>
	<li>add (source node,distance (0)) to queue and update node 0's distance to 0 in distance array</li>
	<li>Proform bfs operation</li>
	<li>perform following step untill queue is empty</li>
	<ul>
		<li>pop node from proirity queue based on node's distance</li>
		<li>loop through each of its adjacent nodes</li>
		<li>update its adjacent nodes distance in distance array by relaxing its distance</li>
		<li>if distance[currentNode]+weight < distance[adjacentNode] , then distance[adjacentNode]=distance[currentNode]+weight</li>
	</ul>
	<li>Once all the nodes have been iterated, the dist[] array will store the shortest paths.</li>
</ul>

```python
import heapq
nodes,edges=int(input()),int(input())
edges=[input().split() for i in range(edges)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(nodes)}
for i,j,w in edges_converted:
    graph[i][j]=w
    graph[j][i]=w
source=int(input())
queue=[]
distance={i:float('inf') for i in range(nodes)}
heapq.heappush(queue,(0,source))
distance[source]=0
while queue:
    dist,current=heapq.heappop(queue)
    for adj,weight in graph[current].items():
        if(dist+weight < distance[adj]):
            distance[adj]=dist+weight
            heapq.heappush(queue,(dist+weight,adj))
print(distance)
#print(*distance.values())
```

<h2>Print Shortest Path From Source To Destination : Dijikstra Algorithm</h2>
<p>Given an undirected weighted graph and source and destination nodes</p>
<p>We have to print the shortest path from source to destination</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/12/Screenshot-2022-12-19-004616.png">
<p><strong>Input : </strong></p>
<p>n = 5, m= 6</p>
<p>edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]</p>
<p><strong>Output:</strong></p>
<p>1 4 3 5</p>
<p>The source vertex is 1. Hence, the shortest distance path of node 5 from the source will be 1->4->3->5 as this is the path with a minimum sum of edge weights from source to destination.</p>

<p><strong>Steps To Solve :</strong></p>
<p>We know that, to find shortest distance from source to destination we can use dijikstra algorithm</p>
<p>While we are calculating shortest distance, simply we can track each node's parent</p>
<p>So, that we can print any node's path</p>

```python
import heapq
nodes,edge=int(input()),int(input())
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
source,destination=int(input("Source : ")),int(input("Destination : "))
graph={i:{} for i in range(1,nodes+1)}
for i,j,w in edges_converted:
    graph[i][j]=w
    graph[j][i]=w
queue=[]
heapq.heappush(queue,(0,source))
distance={i:float('inf') for i in range(1,nodes+1)}
parent={i:i for i in range(1,nodes+1)}
parent[source]=-1
distance[source]=0
while queue:
    dist,current=heapq.heappop(queue)
    for adj,weight in graph[current].items():
        if(distance[current]+weight < distance[adj]):
            distance[adj]=distance[current]+weight
            heapq.heappush(queue,(distance[current]+weight,adj))
            parent[adj]=current
temp=destination
final=[]
while temp!=source:
    final.append(temp)
    temp=parent[temp]
else:
    final.append(source)
print(final[::-1])
```

<h2>Shortest Distance in a Binary Maze</h2>
<p>Given an n * m matrix grid where each element can either be 0 or 1. You need to find the shortest distance between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1. </p>
<p>If the path is not possible between the source cell and the destination cell, then return -1.</p>
<p><strong>Input : </strong></p>
<pre>
grid[][] = {{1, 1, 1, 1},
        {1, 1, 0, 1},
        {1, 1, 1, 1},
        {1, 1, 0, 0},
        {1, 0, 0, 1}}
source = {0, 1}
destination = {2, 2}
</pre>
<p><strong>Output : </strong></p>
<p>3</p>
<p><strong>Explanation : </strong></p>
<pre>
1 1 1 1
1 1 0 1
1 1 1 1
1 1 0 0
1 0 0 1
</pre>
<p>The highlighted part in the above matrix denotes the shortest path from source to destination cell.</p>

<p><strong>Input : </strong></p>
<pre>
grid[][] = {{1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1},
            {1, 1, 1, 1, 0},
            {1, 0, 1, 0, 1}}
source = {0, 0}
destination = {3, 4}
</pre>
<p><strong>Output : </strong></p>
<p>-1</p>
<p><strong>Explanation : </strong></p>
<p>Since, there is no path possible between the source cell and the destination cell, hence we return -1.</p>

<p><strong>Steps To Solve : </strong></p>
<p>Here we have to find minimum distance from source to destination in matrix</p>
<p>It can also be solved by using dijikstra algorithm</p>
<p>But, here we don't have adjacent nodes and we can move either top,bottom,left,right</p>
<ul>
	<li>Create distance array with size of given matrix and fill infinity</li>
	<li>fill zero for source position</li>
	<li>add source to priotity queue with 0 distance</li>
	<li>repeat following steps untill queue is empty</li>
	<ul>	
		<li>pop the element from queue</li>
		<li>loop throw its adjancent positions</li>
		<li>update it distances and add to queue</li>
	</ul>
</ul>

```python
import heapq
n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
source_row,source_col=list(map(int,input().split()))
dest_row,dest_col=list(map(int,input().split()))
distance=[[float('inf')]*m for i in range(n)]
distance[source_row][source_col]=0
queue=[]
heapq.heappush(queue,(0,(source_row,source_col)))
while queue:
    current_row,current_col=heapq.heappop(queue)[1]
    for i,j in zip([0,0,-1,1],[1,-1,0,0]):
        row=current_row+i
        col=current_col+j
        if(row>=0 and col>=0 and row<n and col<m and matrix[row][col]==1 and 1+distance[current_row][current_col]<distance[row][col]):
            distance[row][col]=1+distance[current_row][current_col]
            heapq.heappush(queue,(1+distance[current_row][current_col],(row,col)))
print(distance[dest_row][dest_col])
```