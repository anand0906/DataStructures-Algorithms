
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

<h2>Path With Minimum Effort : Minimum Absolute Difference From Source To Destination</h2>
<p>You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of the cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.</p>
<p>A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.</p>

<p><strong>Example 1:</strong></p>
<p><strong>Input:</strong></p>
<p>heights = [[1,2,2],[3,8,2],[5,3,5]]</p>
<p><strong>Output:</strong></p>
<p>2</p>
<p>The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.</p>

<p><strong>Example 2:</strong></p>
<p><strong>Input:</strong></p>
<p>heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]</p>
<p><strong>Output:</strong></p>
<p>0</p>
<p>The route of [1,1,1,1,1,1,1,1,1,1,1,1,1,1] has a maximum absolute difference of 0 in consecutive cells.This is better than the route of [1,1,1,1,1,1,2,1], where the maximum absolute difference is 1.</p>

<p><strong>Steps To Solve : </strong></p>
<p>Here we have given an matrix of integers</p>
<p>we have given source and destination positions</p>
<p>we can move in all four direction from current positions</p>
<p>For each step , we can have absolute difference between current position element and target moving position</p>
<p>To Move from source to destination , there might have different ways</p>
<p>We have to find most optimal way which have minimum of maximum absolute difference in steps involved in that path</p>
<ul>
    <li>Declare matrix, source and destination</li>
    <li>let's take an difference matrix with same size as given matrix and fill it with infinity</li>
    <li>Above difference matrix can be used to store maximum absolute difference at each position while coming from source</li>
    <li>Since source is starting point, put maximum absolute difference as 0 in difference matrix </li>
    <li>Since we need to find all possible ways , we can apply dijiktra algorithm Here</li>
    <ul>
        <li>Create a priority queue and add source position as (currentDifference,(row,col))</li>
        <li>Since we need maximum difference add element to queue like specified format</li>
        <li>Untill queue is empty , repeat the following steps</li>
        <ul>
            <li>pop element from queue -> (currentDifference,(row,col))</li>
            <li>loop through its four directions</li>
            <li>Check their new absolute Difference and take maximum of currentDifference and new Difference </li>
            <li>Store minimum value into new position and add that it into queue if maximum difference is less than current position difference</li>
        </ul>
        <li>Final Distance array will give all possible minimum of maximum difference from source to all other positions</li>
        <li>We can return our required destination position</li>
    </ul>
</ul>

```python
import heapq
n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
sourceRow,sourceCol=list(map(int,input().split()))
destRow,destCol=list(map(int,input().split()))
difference=[[float('inf')]*m for i in range(n)]
difference[sourceRow][sourceCol]=0
queue=[]
heapq.heappush(queue,(0,(sourceRow,sourceCol)))
while queue:
    currentDiff,(row,col)=heapq.heappop(queue)
    for i,j in zip([0,0,-1,1],[1,-1,0,0]):
        r=row+i
        c=col+j
        if(r>=0 and c>=0 and r<n and c<m):
            newDiff=max(abs(matrix[r][c]-matrix[row][col]),currentDiff)
            if(newDiff < difference[r][c]):
                heapq.heappush(queue,(newDiff,(r,c)))
                difference[r][c]=newDiff
print(difference[destRow][destCol])
```

<p>Time Complexity: O( 4*N*M * log( N*M) ) { N*M are the total cells, for each of which we also check 4 adjacent nodes for the minimum effort and additional log(N*M) for insertion-deletion operations in a priority queue } </p>
<p>Where, N = No. of rows of the binary maze and M = No. of columns of the binary maze.</p>
<p>Space Complexity: O( N*M ) { Distance matrix containing N*M cells + priority queue in the worst case containing all the nodes ( N*M) }.</p>
<p>Where, N = No. of rows of the binary maze and M = No. of columns of the binary maze</p>

<h2>Cheapest Flights Within K Stops</h2>
<p>There are n cities and m edges connected by some number of flights. You are given an array of flights where flights[i] = [ fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost price. You have also given three integers src, dst, and k, and return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.</p>

<p><strong>Example 1:</strong></p>
<img src="https://static.takeuforward.org/wp/uploads/2023/01/Screenshot-2023-01-08-143709.png">
<p><strong>Input:</strong></p>
<p>flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]</p>
<p>src = 0</p>
<p>dst = 3</p>
<p>k = 1</p>
<p><strong>Output:</strong></p>
<p>700</p>
<p>The optimal path with at most 1 stops from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.</p>

<p><strong>Example 2:</strong></p>
<img src="https://static.takeuforward.org/wp/uploads/2023/01/Screenshot-2023-01-08-143831.png">
<p><strong>Input:</strong></p>
<p>flights = [[0,1,100],[1,2,100],[0,2,500]]</p>
<p>src = 0</p>
<p>dst = 2</p>
<p>k = 1</p>
<p><strong>Output:</strong></p>
<p>200</p>
<p>The graph is shown above.
The optimal path with at most 1 stops from city 0 to 2 is marked in red and has cost 100 + 100 = 200.</p>

<p><strong>Steps To Solve : </strong></p>
<p>We have given an graph and source, destionation</p>
<p>We have to find path from source to destionation</p>
<p>But it should have maximum of k stops, means at max k nodes should be involved in path excluing source and dest</p>
<p>We have to find minimum path with at most k stops</p>
<p>It is completely similar to dijikstra</p>
<p>Since we need to take at most k stops, managing queue in terms of stops and distance will give answer</p>

<ul>
    <li>Create graph</li>
    <li>Create distance array and fill with infinity</li>
    <li>create queue and add source destionation as {steps,(src,dist)}</li>
    <li>fill source node distance as 0, since it is starting node</li>
    <li>repeat following steps untill queue is empty</li>
    <ul>
        <li>pop element from queue</li>
        <li>loop throw its adjacent nodes</li>
        <li>if current steps less than k and new distance is less than adjacent distance</li>
        <li>add adjacent node to queue and update adjacent distance</li>
    </ul>
    <p>final distance array gives all poosible minium distance for each node</p>
    <p>if destination node distance is infinity it is unreachble and return -1, otherwise return minium distance</p>

</ul>

```python
import heapq
nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
source=int(input())
destination=int(input())
k=int(input())
graph={i:dict() for i in range(nodes)}
for i,j,w in edges_converted:
    graph[i][j]=w
distance={i:float('inf') for i in range(nodes)}
distance[source]=0
queue=[]
heapq.heappush(queue,(0,source,0))
while queue:
    steps,node,currentDistance=heapq.heappop(queue)
    for adj,weight in graph[node].items():
        if(steps+1<=k+1 and currentDistance+weight<distance[adj]):
            distance[adj]=currentDistance+weight
            heapq.heappush(queue,(steps+1,adj,distance[adj]))
print(-1 if(distance[destination]==float('inf')) else distance[destination])
```

<p>Time Complexity: O( N ) { Additional log(N) of time eliminated here because we’re using a simple queue rather than a priority queue which is usually used in Dijkstra’s Algorithm }.</p>
<p>Where N = Number of flights / Number of edges.</p>
<p>Space Complexity:  O( |E| + |V| ) { for the adjacency list, priority queue, and the dist array }.</p>
<p>Where E = Number of edges (flights.size()) and V = Number of Airports.</p>


<h2>Number of Ways to Arrive at Destination</h2>
<p>You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.</p>
<p>You are given an integer n and a 2D integer array ‘roads’ where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.</p>
<p>Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.</p>

<img src="https://static.takeuforward.org/wp/uploads/2023/01/Screenshot-2023-01-08-151107.png">
<p><strong>Input : </strong></p>
<p>n=7, m=10</p>
<p>edges= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]</p>
<p><strong>Output:</strong></p>
<p>4</p>
<p>The four ways to get there in 7 minutes (which is the shortest calculated time) are:</p>
<p>- 0  6</p>
<p>- 0  4  6</p>
<p>- 0  1  2  5  6</p>
<p>- 0  1  3  5  6</p>

<img src="https://static.takeuforward.org/wp/uploads/2023/01/Screenshot-2023-01-08-151223.png">
<p><strong>Input : </strong></p>
<p>n=6, m=8</p>
<p>edges= [[0,5,8],[0,2,2],[0,1,1],[1,3,3],[1,2,3],[2,5,6],[3,4,2],[4,5,2]]</p>
<p><strong>Output:</strong></p>
<p>3</p>
<p>The three ways to get there in 8 minutes (which is the shortest calculated time) are:</p>
<p>- 0  5</p>
<p>- 0  2  5</p>
<p>- 0  1  3  4  5</p>

<p><strong>Steps To Solve : </strong></p>
<p>We have given an undirectional graph and source, destination</p>
<p>We need to find number to find path from source to destination with minimum distance</p>
<p>we know how to find minimum distance path using dijikstra algorithm</p>
<p>While finding path, track the number ways to reach each node from source</p>

<p>While storing minimum distance in distance array, if same distance again come while looping we will increase ways for that particular node</p>

```python
import heapq
nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
source=int(input())
destination=int(input())
graph={i:dict() for i in range(nodes)}
ways={i:0 for i in range(nodes)}
for i,j,w in edges_converted:
    graph[i][j]=w
    graph[j][i]=w
distance={i:float('inf') for i in range(nodes)}
distance[source]=0
ways[source]=1
queue=[]
heapq.heappush(queue,(source,0))
while queue:
    node,currentDistance=heapq.heappop(queue)
    for adj,weight in graph[node].items():
        if(currentDistance+weight<distance[adj]):
            distance[adj]=currentDistance+weight
            heapq.heappush(queue,(adj,distance[adj]))
            ways[adj]=ways[node]
        elif(currentDistance+weight==distance[adj]):
            ways[adj]=(ways[node]+ways[adj])%(int(1e9+9))
print(-1 if(distance[destination]==float('inf')) else ways[destination])
```
<p>Time Complexity: O( E* log(V)) { As we are using simple Dijkstra's algorithm here, the time complexity will be or the order E*log(V)}</p>
<p>Where E = Number of edges and V = No. of vertices.</p>
<p>Space Complexity :  O(N) { for dist array + ways array + approximate complexity for priority queue }</p>
<p>Where, N = Number of nodes.</p>

<h2>Minimum Multiplications to Reach End</h2>
<p>Given start, end, and an array arr of n numbers. At each step, the start is multiplied by any number in the array and then a mod operation with 100000 is done to get the new start.</p>
<p>Your task is to find the minimum steps in which the end can be achieved starting from the start. If it is not possible to reach the end, then return -1.</p>

<p><strong>Example : 1</strong></p>
<p>Input : </p>
<p>arr[] = {2, 5, 7}</p>
<p>start = 3</p>
<p>end = 30</p>
<p>Output : </p>
<p>2</p>
<p>Step 1: 3*2 = 6 % 100000 = 6</p>
<p>Step 2: 6*5 = 30 % 100000 = 30</p>
<p>Therefore, in minimum 2 multiplications we reach the end number which is treated as a destination 
node of a graph here.</p>

<p><strong>Example : 2</strong></p>
<p>Input : </p>
<p>arr[] = {3, 4, 65}</p>
<p>start = 7</p>
<p>end = 66175</p>
<p>Output : </p>
<p>4</p>
<p>Step 1: 7*3 = 21 % 100000 = 21</p>
<p>Step 2: 21*3 = 6 % 100000 = 63</p>
<p>Step 3: 63*65 = 4095 % 100000 = 4095 </p>
<p>Step 4: 4095*65 = 266175 % 100000 = 66175</p>
<p>Therefore, in minimum 4 multiplications we reach the end number which is treated as a destination node of a graph here.</p>

<p><strong>Steps To Solve : </strong></p>
<p>Given a start and end numbers</p>
<p>We can pick start number and multiply with any number in given array and resultant can be multiplied in any one number in array so on.</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/01/Screenshot-2023-01-08-145731.png">
<p>as shown in image,we have started from start number and it multiplied with given array like a graph structure</p>
<p>Here numbers we are getting by multiplication area considered as nodes of graph, since we have to modulo by 100000</p>
<p>Nodes will be maximum from 0 to 99999</p>
<p>edge will be from current number to resultant number from multiplication of array number</p>
<p>We have given end number that will be our destionation node</p>
<p>We need to minimum number of steps to reach from start (source) to end (destination).</p>
<ul>
    <li>Create queue and add start number , with steps as 0</li>
    <li>Define distance array of size 100000 and fill with infinity, since maximum nodes will be from 0 to 100000 only</li>
    <li>put distance[start] to zero, since it is source and starting point</li>
    <li>Then, untill queue is empty repeat following steps</li>
    <ul>
        <li>pop number from queue</li>
        <li>multiply with each array number</li>
        <li>if resultant steps less than existed, update distance array</li>
        <li>if resultant equal to end return steps</li>
    </ul>
    <li>if end not found, return -1</li>
</ul>

```python
def solve():
    array=list(map(int,input().split()))
    start=int(input())
    end=int(input())
    distance=[float('inf') for i in range(100000)]
    distance[start]=0
    queue=[(start,0)]
    mod=100000
    while queue:
        current,steps=queue.pop(0)
        for i in array:
            new=(current*i)%mod
            if(steps+1 < distance[new]):
                distance[new]=steps+1
                if(new==end):
                    return distance[new]
                queue.append((new,distance[new]))
    return -1
print(solve())
```

<p>Time Complexity : O(100000 * N) </p>
<p>Where ‘100000’ are the total possible numbers generated by multiplication (hypothetical) and N = size of the array with numbers of which each node could be multiplied</p>
<p>Space Complexity :  O(100000 * N) </p>
<p>Where ‘100000’ are the total possible numbers generated by multiplication (hypothetical) and N = size of the array with numbers of which each node could be multiplied. 100000 * N is the max possible queue size. The space complexity of the dist array is constant.</p>

<h2>Bellman Ford Algorithm</h2>
<p>Given a weighted, directed and connected graph of V vertices and E edges, Find the shortest distance of all the vertices from the source vertex S.</p>
<p>If the Graph contains a negative cycle then return an array consisting of only -1</p>

<p><strong>Example 1:</strong></p>
<p>Input : </p>
<p>V = 6</p>
<p>E = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]]</p>
<p>S = 0</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/Screenshot-2022-11-23-165611.png">
<p>Result: 0 5 3 3 1 2</p>
<p>Explanation: Shortest distance of all nodes from the source node is returned.</p>

<p><strong>Example 2:</strong></p>
<p>Input : </p>
<p>V = 2, E = [[0,1,9]],  S = 0</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/Screenshot-2022-11-23-165658.png">
<p>Result: 0 9</p>
<p>Explanation: Shortest distance of all nodes from the source node is returned.</p>

<p>The bellman-Ford algorithm helps to find the shortest distance from the source node to all other nodes</p>
<p>While learning Dijkstra's algorithm, we came across the following two situations, where Dijkstra's algorithm failed:</p>
<ul>
    <li>If the graph contains negative edges.</li>
    <li>If the graph has a negative cycle (In this case Dijkstra's algorithm fails to minimize the distance, keeps on running, and goes into an infinite loop. As a result it gives TLE error).</li>
</ul>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/Screenshot-2022-11-23-165806.png">
<p>Negative Cycle: A cycle is called a negative cycle if the sum of all its weights becomes negative. The following illustration is an example of a negative cycle:</p>
<p>Bellman-Ford's algorithm successfully solves these problems. It works fine with negative edges as well as it is able to detect if the graph contains a negative cycle.</p>

<p>Steps : </p>
<ul>
    <li>create graph with given edges and nodes</li>
    <li>define distance dictionary for given nodes and fill with infinity</li>
    <li>Make distance of source node to zero</li>
    <li>repeat following steps for (number of nodes-1) times</li>
    <ul>
        <li>loop through each edge of given graph and do following steps</li>
        <ul>
            <li>Relax the edge</li>
            <li>Means, check starting distanec[node] + weight < distance[end], if it satisfies update distance array with new minimum distance</li>
        </ul>
    </ul>
    <li>After performing above steps, distance array will update to minimum distance from source to all nodes</li>
    <li>To Check negative cycle</li>
    <li>repeat above step once again, if distance array updated, then negative cycle existed</li>
</ul>   


```python
n,e=list(map(int,input().split()))
edges=[list(map(int,input().split())) for i in range(e)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
source=int(input())
distance={i:float('inf') for i in range(n)}
distance[source]=0
for _ in range(n-1):
    for i,j,w in edges_converted:
        if(distance[i]+w<distance[j]):
            distance[j]=distance[i]+w
for i,j,w in edges_converted:
    if(distance[i]+w<distance[j]):
        print("Negative Cycle")
        break
else:
    print(distance)
```

<p>Time Complexity: O(V*E), where V = no. of vertices and E = no. of Edges.</p>
<p>Space Complexity: O(V) for the distance array which stores the minimized distances.</p>

<h2>Floyd Warshall Algorithm</h2>
<p>he problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. If Matrix[i][j]=-1, it means there is no edge from i to j.</p>
<p><strong>Example 1:</strong></p>
<p><strong>Input Format:</strong></p>
<p>matrix[][] = { {0, 2, -1, -1},{1, 0, 3, -1},{-1, -1, 0, -1},{3, 5, 4, 0} }</p>
<p><strong>Result:</strong></p>
<p>0 2 5 -1 </p>
<p>1 0 3 -1 </p>
<p>-1 -1 0 -1</p>
<p>3 5 4 0</p>
<p>In this example, the final matrix is storing the shortest distances. For example, matrix[i][j] is 
storing the shortest distance from node i to j.</p>
<p><strong>Example 2:</strong></p>
<p><strong>Input Format:</strong></p>
<p>matrix[][] = {{0,25},{-1,0}}</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/image-6.png">
<p><strong>Result</strong></p>
<p>0 25</p>
<p>-1 0﻿</p>
<p>In this example, the shortest distance is already given (if it exists).</p>

<p>Dijkstra's Shortest Path algorithm and Bellman-Ford algorithm are single-source shortest path algorithms where we are given a single source node and are asked to find out the shortest path to every other node from that given source. But in the Floyd Warshall algorithm, we need to figure out the shortest distance from each node to every other node.</p>
<p>Basically, the Floyd Warshall algorithm is a multi-source shortest path algorithm and it helps to detect negative cycles as well. The shortest path between node u and v necessarily means the path(from u to v) for which the sum of the edge weights is minimum.</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/Screenshot-2022-11-23-175537.png">
<p>From the above example we can derive the following formula:</p>
<p>matrix[i][j] =min(matrix[i][j], matrix[i ][k]+matrix[k][j]), where i = source node, j = destination node, and k = the node via which we are reaching from i to j.</p>
<p>Here we will calculate dist[i][j] for every possible node k (k = 0, 1….V, where V = no. of nodes), and will select the minimum value as our result.</p>

<p><strong>Steps to solve : </strong></p>
<p>Here, we just find all possible paths from one to another node and store it in array</p>
<p>Create a adjanceny matrix for given graph</p>
<p>To find minimum distance for every pair of vertices , we need two nested loops of vertices</p>
<p>For each pair , we need to find path considering each other node, so we need another nested loop</p>
<p>Find out the distance for every pair and take the minimum out of it</p>

```python
nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i)-1,int(j)-1,int(w)) for i,j,w in edges]
src,dest=list(map(int,input().split()))
graph=[[float('inf')]*nodes for i in range(nodes)]
for i,j,w in edges_converted:
    graph[i][j]=w
for i in range(nodes):
    graph[i][i]=0
for k in range(nodes):
    for i in range(nodes):
        for j in range(nodes):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
print(graph[src-1][dest-1])
```

<p>Time Complexity: O(V3), as we have three nested loops each running for V times, where V = no. of vertices.</p>
<p>Space Complexity: O(V2), where V = no. of vertices. This space complexity is due to storing the adjacency matrix of the given graph.</p>

<h2>Find the City With the Smallest Number of Neighbours at a Threshold Distance</h2>
<p>There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi,weighti]  represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distance Threshold. You need to find out a city with the smallest number of cities that are reachable through some path and whose distance is at most Threshold Distance, If there are multiple such cities, our answer will be the city with the greatest number.</p>
<p>Note: that the distance of a path, connecting cities i and j are equal to the sum of the edges' weights along that path.</p>

<p><strong>Example 1:</strong></p>
<p><strong>Input Format: </strong></p>
<p>N=4, M=4 </p>
<p>edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], </p>
<p>distanceThreshold = 4</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/Screenshot-2022-11-23-182442.png">
<p><strong>Output : </strong></p>
<p>3</p>

<p><strong>Example 2:</strong></p>
<p><strong>Input Format: </strong></p>
<p>N=3, M=2 </p>
<p>edges = [[0,1,3],[1,2,1]] </p>
<p>distanceThreshold = 2</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/Screenshot-2022-11-23-182533.png">

<p><strong>Steps to solve : </strong></p>
<p>Here we will need to find a path whose distance less than threshold distance.</p>
<p>So, we will apply floyd warshall to given graph and check all path and print the required one</p>
<p>we need to find a node, which is having minimum number of node having less than threshold distance</p>

```python
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
```

<p>Time Complexity: O(V3), as we have three nested loops each running for V times, where V = no. of vertices.</p>
<p>Space Complexity: O(V2), where V = no. of vertices. This space complexity is due to storing the adjacency matrix of the given graph.</p>