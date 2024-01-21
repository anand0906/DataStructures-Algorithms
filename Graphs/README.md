<center><h1><strong>Graphs</strong><h1></center>
<h4>Definations<h4>
<ul>
<li>Graph is a non-linear data structure which consists of nodes/vertices/points and edges/lines/arcs(used to connect the pair of nodes).</li>
<li>Graph is a finite set of nodes and edges which is used to connect the pair of nodes.</li>
<li>Graph is pictorial representation of set of objects,where some pair of objects connected together by links.The interconnected objects are termed as nodes and links present between pair of objects termed as edges.</li>
<li>Graph is simply cyclic tree.</li>
</ul>

<h4>Example</h4>
Consider a graph of vertices V(A,B,C,D,E) and edges E((A,B), (B,C), (C,E), (E,D), (D,B), (D,A)) is represented as follows
<img src="https://static.javatpoint.com/ds/images/graph-definition.png">

<h4>Applications</h4>
<ul>
<li>Graphs are used for developing recommandation system for social media applications and ecommerce applications</li>
<li>graphs are used to represent the flow of computation in computer science.</li>
<li>Google maps uses graphs for building transportation systems, where intersection of two(or more) roads are considered to be a vertex and the road connecting two vertices is considered to be an edge, thus their navigation system is based on the algorithm to calculate the shortest path between two vertices.</li>
<li>In world wide web,One page will connect to another through link. which is develeped based on graph data structure.</li>
</ul>

<h4>Types of Graphs</h4>
<ol>
	<li>Null</li>
	<li>Finite & Infinte</li>
	<li>Cyclic & Acyclic</li>
	<li>Simple & Multi</li>
	<li>Complete & Pseudo</li>
	<li>Connected & Disconnected</li>
	<li>Directed & Undirected</li>
	<li>Weighted & Unweighted</li>	
	<li>Dense & Sparse Graphs</li>
	<li>Bipartite Graph</li>
</ol>

<h4>1.Null Graph</h4>
A Graph which is defined as Null Graph if and only if it consists vertices/nodes and doesn't contains any edge between nodes/vertices.
<br>
A Graph consists of n nodes and zero vertices is called as Null Graph.
<br>
<h4>Example</h4>
<img src="https://static.javatpoint.com/tutorial/dms/images/types-of-graphs.jpg">
<h4>2.Finite Graph</h4>
A Graph which consists of finite number of vertices and edges is called as Finite Graph.
<br>
<h4>Example</h4>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/simplegraph.png">
<br>
<h4>3.Infinte Graph</h4>
A Graph which Consists of infinite number of vertices and infinte number of edges called as Infinite Graph.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/graph2-4.png">
<h4>4.Cyclic Graph</h4>
A Graph Which consists of atleast one cycle is called as Cyclic Graph.
<img src="https://study.com/cimages/multimages/16/cyclic_graphs.png">
<h4>5.Acyclic Graph</h4>
A Graph which consists of No cycles is known as Acyclic Graph.
<img src="https://generalducky.github.io/images/Pic4.PNG">
<h4>6.Simple Graph</h4>
A Graph which consists of only one edge between any pair of vertices is known as simple graph.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/simple1.png">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/simple2-1.png">
<h4>7.Multi Graph</h4>
A Graph which consits multiple edges between any pair of vertices and does not contain any self-loops is known as multi graph.
<img src="https://static.javatpoint.com/tutorial/dms/images/types-of-graphs2.jpg">
<h4>8.Complete Graph.</h4>
A graph which should consists of edge between every pair of vertices called Complete graph.Every complete graph is simple graph.
<br>
Degree of each node is number of vertices-1 
<img src="https://cdn.educba.com/academy/wp-content/uploads/2019/12/Graph-Types6.jpg.webp">
<h4>8.Pseudo Graph</h4>
A Graph which consists of atleast one self loop is known as Pseudo graph.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/pseudo-2.png">
<h4>9.Regular Graph</h4>
A graph which said to be regular if all vertices consists of equal degree.
<br>
A complete graph is regular but vice versa not possible.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/regular-1.png">
<h4>9.Connected Graph</h4>
A Graph is said to be connected if there exists atleast one path between every pair of vertices.
<img src="https://cdn.educba.com/academy/wp-content/uploads/2019/12/Graph-Types12-1.jpg.webp">
<h4>10.DisConnected Graph</h4>
A Graph is said to be disconnected if it does not contain a path between atleast one pair of vertices.
<img src="https://cdn.educba.com/academy/wp-content/uploads/2019/12/Graph-Types14.jpg.webp">
<h4>11.Directed Graph</h4>
A Graph is said to be Directed if and only if all edges contains direction and determines the traversal order.
<br>
A graph G = (V, E) with a mapping f such that every edge maps onto some ordered pair of vertices (Vi, Vj) is called Digraph. It is also called Directed Graph. Ordered pair (Vi, Vj) means an edge between Vi and Vj with an arrow directed from Vi to Vj
<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/digraph.png">
<h4>12.Undirected Graph</h4>
A Graph is said to be undirected if and only if there is  no orientation/direction on the edges of graph.
Where a set of objects are connected, and all the edges are bidirectional. The below image showcases the undirected graph, 
It’s like the associativity of two Facebook users after connecting as a friend. Both users can refer and share photos, comment among each other
<img src="https://www.upgrad.com/blog/wp-content/uploads/2020/10/2.png">
<h4>13.Weighted Graph</h4>
Graphs whose edges or paths have values. All the values seen associated with the edges are called weights. Edges value can represent weight/cost/length.
<img src="https://miro.medium.com/max/469/1*tDJlwZ1x9TLibRvTlDQcEg.png">
<h4>14.Unweighted Graph</h4>
Where there is no value or weight associated with the edge. By default, all the graphs are unweighted unless there is a value associated.
<img src="https://miro.medium.com/max/471/1*EJLaKGGx2dd0NkwjHEPFEg.png">
<h4>15.Dense & Sparse Graphs</h4>
a dense graph is a graph in which the number of edges is close to the maximal number of edges. The opposite, a graph with only a few edges, is a sparse graph.
<img src="https://images.slideplayer.com/14/4318595/slides/slide_4.jpg">
<h4>16.Bipartite Graph</h4> 
If the vertex-set of a graph G can be split into two disjoint sets, V1 and V2 , in such a way that each edge in the graph joins a vertex in V1 to a vertex in V2 , and there are no edges in G that connect two vertices in V1 or two vertices in V2 , then the graph G is called a bipartite graph.
<img src="https://www.tutorialspoint.com/discrete_mathematics/images/complete_bipartite.jpg">
<h4>17.Complete Bipartite Graph</h4>
A complete bipartite graph is a bipartite graph in which each vertex in the first set is joined to every single vertex in the second set. The complete bipartite graph is denoted by Kx,y where the graph G contains x vertices in the first set and y vertices in the second set.
<img src="https://www.tutorialspoint.com/discrete_mathematics/images/complete_bipartite.jpg">

<h3>Graph Terminology</h3>
<h4>Vertex</h4>
Individual data element of a graph is known as Vertex.
<br>
Vertex is also known as node.
<h4>Edge</h4>
An Edge is path/line/connecting link betweet two vertices(Endpoints) in the graph.
<h4>Adjcent vertices</h4>
if two vertices are said to be adjacent if and only if they are endpoints of an edge.i.e those two vertices must and should form an edge.
<h4>Incident Edge</h4>
An Edge said to be an incident edge on a vertex,if the vertex is an endpoint of an edge.
<h4>Outgoing Edges</h4>
An Edge is said to be an outgoing edge of a vertx.If and only if edge is directed outwards from the vertex.
<h4>Incoming Edges</h4>
An Edge is said to be an Incoming edge of a vertx.if and only id edge is directd inwards to the vertex.
<h4>Degree</h4>
A degree of vertex is defined as number of edges which are incident/incoming on the vertex.
<h4>In-degree</h4>
Incoming degree of a vertex is defined as number of edges which are incoming to the vertex.
<h4>Out-degree</h4>
Outgoing degree of a vertex is defined as number of outgoing edges from thr vertex.
<h4>Parllel edges</h4>
if there are more than one edge between same pair of vertices.then they are called as parallel edges.
<h4>self-loop/cycle</h4>
self loop is an edge whose end vertices are equal.i.e if an edge exsited within same vertex.
<h4>Forest</h4>
A Graph with no cycles is known as Forest.
<h4>Simple Graph</h4>
a graph which does not contain any self loops and parellel edges.
<h4>Path</h4>
A Path is the sequence of successive edges between two nodes.
<h4>Length Of Path</h4>
Length Of Path id defined is number of successive edges between two nodes.
<h4>Simple Path</h4>
A Simple Path is the path which is formed by distinct vertices.
<h4>Source Vertex</h4>
A vertex whose in-degree is zero is called as source vertex.
<h4>Sink Vertex</h4>
A vertex whose out-degree is zero is called as sink vertex.
<h4>Strongly Connected Graph</h4>
A graph which contains a directed path from u to v and should contain a directed path from v to u for all pairs of vertices.
<h4>Weakly connected graph</h4>
A directed graph is said to be weakly connected if all directed edges are replaced by its undirected edges,it will form a connected graph.
<h4>Bridge</h4>
A bridge is an edge whose removal will result the disconnected graph.



<center><h1>Graph Represntation</h1></center>
<h4>Representation</h4>
We know graph is a finite set of vertices and edges.
<br>
Graph is the concept of how we are storing the graph in the computer memory.
<br>
A graph can be represented in three ways based on opertion that we are performing on the graph as follows.
<ul>
	<li>Adjacency Matrix</li>
	<li>Adjacency List</li>
	<li>Incidence Matrix</li>
	<li>Incidence  List</li>
</ul>
<h3>Adjacency Matrix</h3>
In this representation, the graph is represented using a matrix of size total number of vertices by a total number of vertices.
<br>
That means a graph with 4 vertices is represented using a matrix of size 4X4. In this matrix, both rows and columns represent vertices. This matrix is filled with either 1 or 0. 
<br>
Here, 1 represents that there is an edge from row vertex to column vertex and 0 represents that there is no edge from row vertex to column vertex.
<br>
<h4>Directed Graph</h4>
if A is adjacency matrix,aij=1 then there is a directed edge from vertex i to vertex j,
<img src="http://www.btechsmartclass.com/data_structures/ds_images/Graph%20Adjacency%20Matrix%202.jpg">
<h4>Undirected Graph</h4>
if A id adjacency matrix,aij=1 then there is a undiected edge from vertex i to vertex j and also there is another undirected edge from vertex i to vertex j
<img src="http://www.btechsmartclass.com/data_structures/ds_images/Graph%20Adjacency%20Matrix%201.jpg"> 
<h4>Weighted Graph</h4>
For weighted graph each cell is filled with that particular weight of edge instead of 1 as follows.
<br>
if any cell filled with 0,that means there is no edge between that vertices.
<br>
<img src="https://static.javatpoint.com/tutorial/graph-theory/images/graph-representations3.png">
<h4>Advantages</h4>
<ul>
	<li>Easy to understand and implements</li>
	<li>Checking whether an edge existed between two vertices/nodes takes O(1) time</li>
	<li>Removing an edge between two vertices/nodes takes O(1) time</li>
	<li>Adding an edge between two vertices/nodes takes O(1) time</li>
</ul>
<h4>Disadvantages</h4>
<ul>
	<li>Adding/removing a vertex to the existed graph will take more time O(v**2)(v=number of vertices)</li>
	<li>Consumes more space O(V**V) for even graph consists of less edges(sparse graph)</li>
</ul>
<h3>Adjacency List</h3>
Adjacency list is a linked representation.
<br>
In this representation, for each vertex in the graph, we maintain the list of its neighbors. It means, every vertex of the graph contains list of its adjacent vertices.
<br>
We have an array of vertices which is indexed by the vertex number and for each vertex v, the corresponding array element points to a singly linked list of neighbors of v.
<br>
Let's see the following directed graph representation implemented using linked list
<img src="https://static.javatpoint.com/tutorial/graph-theory/images/graph-representations5.png">
We can also implement this representation using array as follows:
<img src="https://static.javatpoint.com/tutorial/graph-theory/images/graph-representations6.png">
<h4>Advantages</h4>
<ul>
	<li>Adjacency list saves lot of space.</li>
	<li>Adding/deleting edge/vertex takes O(1) time</li>
	<li>Such kind of representation is easy to follow and clearly shows the adjacent nodes of node.</li>
</ul>
<h4>Disadavtages</h4>
<ul>
	<li>The adjacency list allows testing whether two vertices are adjacent to each other but it is slower to support this operation.</li>
</ul>
<h4>Incindence Matrix</h4>
In this representation, the graph is represented using a matrix of size total number of vertices by a total number of edges. That means graph with 4 vertices and 6 edges is represented using a matrix of size 4X6. In this matrix, rows represent vertices and columns represents edges. This matrix is filled with 0 or 1 or -1. Here, 0 represents that the row edge is not connected to column vertex, 1 represents that the row edge is connected as the outgoing edge to column vertex and -1 represents that the row edge is connected as the incoming edge to column vertex.
<br>
For example, consider the following directed graph representation...
<br>
<img src="http://www.btechsmartclass.com/data_structures/ds_images/Graph%20Incidence%20Matrix.jpg">
<br>
<h3>Problems</h3>
<h4>Creating Graph</h4>
<p>A graph can be represented in either adjacency matrix and adjacency list</p>
<p>Adjacency List</p>

<p>Undirected Graph</p>

```python
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_conv=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(1,n+1)}
for i,j in edges_conv:
    graph[i].add(j)
    graph[j].add(i)
print(graph)
```

<p>Directed Graph</p>

```python
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_conv=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(1,n+1)}
for i,j in edges_conv:
    graph[i].add(j)
print(graph)
```

<p>Undirected Weighted Graph</p>

```python
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_conv=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(1,n+1)}
for i,j,w in edges_conv:
    graph[i][j]=w
    graph[j][i]=w
print(graph)
```

<p>Directed Weighted Graph</p>

```python
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_conv=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(1,n+1)}
for i,j,w in edges_conv:
    graph[i][j]=w
print(graph)
```

<p>Adjacency Matrix</p>

<p>Undirected graph</p>

```python
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_conv=[(int(i)-1,int(j)-1) for i,j in edges]
graph=[[0]*n for i in range(n)]
for i,j in edges_conv:
    graph[i][j]=1
    graph[j][i]=1
print(*graph,sep="\n")
```

<p>Directed graph</p>

```python
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_conv=[(int(i)-1,int(j)-1) for i,j in edges]
graph=[[0]*n for i in range(n)]
for i,j in edges_conv:
    graph[i][j]=1
print(*graph,sep="\n")
```

<p>Weighted Undirected graph</p>

```python
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_conv=[(int(i)-1,int(j)-1,int(w)) for i,j,w in edges]
graph=[[0]*n for i in range(n)]
for i,j,w in edges_conv:
    graph[i][j]=w
    graph[j][i]=w
print(*graph,sep="\n")
```

<p>Weighted directed graph</p>

```python
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_conv=[(int(i)-1,int(j)-1,int(w)) for i,j,w in edges]
graph=[[0]*n for i in range(n)]
for i,j,w in edges_conv:
    graph[i][j]=w
print(*graph,sep="\n")
```

<h5>Breadth First Search</h5>

```python
queue=[]
visited={i:False for i in range(1,n+1)}
queue.append(1)
visited[1]=True
while queue:
    temp=queue.pop(0)
    print(temp,end="->")
    for i in graph[temp]:
        if not visited[i]:
            visited[i]=True
            queue.append(i)
```

<h5>Depth First Search</h5>

```python
stack=[]
visited={i:False for i in range(1,n+1)}
visited[1]=True
stack.append(1)
while stack:
    temp=stack.pop()
    print(temp,end="->")
    for i in graph[temp]:
        if not visited[i]:
            visited[i]=True
            stack.append(i)

```

<p>Using Recursion</p>

```python
def dfs(node):
    global visited
    visited[node]=True
    print(node,end="->")
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
visited={i:False for i in range(1,n+1)}
for i in range(1,n+1):
	dfs(i)
```

<h5>1.Number of Provinces</h5>
<p>Given an undirected graph with V vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.</p>
<img src="https://lh4.googleusercontent.com/Vwi5EtntYRGiFEYNhOgiQvlBxmD7RklrbgeseG7kjf1sYVDmcdTtr3HtklVbhdvvmNeQomW7wcbnOgVnYtcWcYoMeld67HC_-HCg5weQktMUY3gFN5koWPhoXONLtSerDkJBK6F7BegkK-CN1iwGSNM"/>

```python
def bfs(graph,i):
    global visited
    queue=[i]
    visited[i]=False
    while queue:
        temp=queue.pop(0)
        for j in graph[temp]:
            if(not visited[j]):
                visited[j]=True
                queue.append(j)

n,e=int(input("Enter number of nodes : ")),int(input("Enter number of edges : "))
edges=[input().split() for i in range(e)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(1,n+1)}
for i,j in edges_converted:
    graph[i].add(j)
    graph[j].add(i)
visited={i:False for i in range(1,n+1)}
count=0
for i in range(1,n+1):
    if(not visited[i]):
        count+=1
        bfs(graph,i)
        
print(count)
```

<h5>2.Number of Islands</h5>
<p>Given a grid of size NxM (N is the number of rows and M is the number of columns in the grid) consisting of ‘0’s (Water) and ‘1’s(Land). Find the number of islands.</p>
<p>An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/08/image-2.png"/>
<p>Output: 3</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/08/image-4.png"/>
<p>Output: 1</p>

```python
def bfs(matrix,i,j):
    global visited
    queue=[(i,j)]
    visited[i][j]=1
    while queue:
        temp=queue.pop(0)
        r,c=temp
        for row in range(-1,2):
            for col in range(-1,2):
                ro=r+row
                co=c+col
                if(ro>=0 and ro<n and co>=0 and co<m and matrix[ro][co] and (not visited[ro][co])):
                    visited[ro][co]=1
                    queue.append((ro,co))
    
n,m=int(input("Enter row size : ")),int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
visited=[[0 for j in range(m)] for i in range(n)]
count=0
for i in range(n):
    for j in range(m):
        if(matrix[i][j] and (not visited[i][j])):
            count+=1
            bfs(matrix,i,j)
print(count)
```

<h5>3.Rotten Oranges : Min time to rot all oranges : BFS</h5>
<p>You will be given an m x n grid, where each cell has the following values : </p>
<p>2  –  represents a rotten orange</p>
<p>1  –  represents a Fresh orange</p>
<p>0  –  represents an Empty Cell</p>
<p>Every minute, if a Fresh Orange is adjacent to a Rotten Orange in 4-direction ( upward, downwards, right, and left ) it becomes Rotten. 
Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it’s not possible, return -1.</p>
<img src="https://lh3.googleusercontent.com/L1EzxJ4FUwvQb7G8pJ9rO1Crx5SykbcRrsSn_lW9ZlT6E6KtqfCfg3twYfTGZw3q9fD0RCzo84oktZTuwsbiJYN-osewe9BaJHAKstiqiT_kiZh4ZPBnKoVSGm89e5QRXYA-5i13"/>
<img src="https://lh3.googleusercontent.com/XKWocUensy0Kubpp05af0peLXbkLylI6BoSd66v7siGsp-dYljICrSJF5ggo6ueqtDTZ9MVZHNVTJEi2cR3c4ByQwHel9xLzVsPlkxVPnwyL6wefOmBUzGArazUivXI0efsUbsvF"/>

```python
n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
queue=[]
count=0
ct=0
final=-float('inf')
for i in range(n):
    for j in range(m):
        if(matrix[i][j]==2):
            queue.append((i,j,0))
        if(matrix[i][j]==1):
            count+=1
a,b=[0,0,1,-1],[1,-1,0,0]
while queue:
    temp=queue.pop(0)
    r,c,v=temp
    for i in range(4):
        r1=r+a[i]
        c1=c+b[i]
        if(r1>=0 and r1<n and c1<m and c1>=0 and matrix[r1][c1]==1):
            matrix[r1][c1]+=1
            ct+=1
            queue.append((r1,c1,v+1))
            final=max(final,v+1)
print(*matrix,sep="\n")
if(ct==count):
    print(final)
else:
    print(-1)
```

<h5>4.Flood Fill Algorithm</h5>
<p>An image is represented by a 2-D array of integers, each integer representing the pixel value of the image. Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, “flood fill” the image.</p>
<p>To perform a “flood fill”, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same colour as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same colour as the starting pixel), and so on. Replace the colour of all of the aforementioned pixels with the newColor.</p>
<p>Input :</p>
<p>sr = 1, sc = 1, newColor = 2</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/08/Screenshot-2022-08-12-at-9.57.33-PM.png"/>
<p>Output : </p>
<img src="https://takeuforward.org/wp-content/uploads/2022/08/Screenshot-2022-08-12-at-9.58.15-PM.png"/>

```python
n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
sr=int(input("Enter starting row : "))
sc=int(input("Enter starting column : "))
newColor=int(input("Enter new color : "))
queue=[(sr,sc)]
target=matrix[sr][sc]
a,b=[0,0,1,-1],[-1,1,0,0]
matrix[sr][sc]=newColor
while queue:
    temp=queue.pop(0)
    r,c=temp
    for i in range(4):
        r1,c1=r+a[i],c+b[i]
        if(r1>=0 and r1<n and c1>=0 and c1<m and matrix[r1][c1]==target):
            matrix[r1][c1]=newColor
            queue.append((r1,c1))
print(*matrix,sep="\n")
```

<h5>5.Distance of nearest cell having 1</h5>
<p>The distance is calculated as |i1  – i2| + |j1 – j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1.</p>
<p>Input :</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/09/image.png"/>
<p>Output :</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/09/image-1.png"/>
<p>Input :</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/09/image-2.png"/>
<p>Output :</p>
<img src="https://takeuforward.org/wp-content/uploads/2022/09/image-3.png"/>

```python
n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
distance=[[0]*m for i in range(n)]
visited=[[False]*m for i in range(n)]
queue=[]
for i in range(n):
    for j in range(m):
        if(matrix[i][j]==1):
            queue.append((i,j,0))
            visited[i][j]=True
while queue:
    temp=queue.pop(0)
    i,j,v=temp
    distance[i][j]=v
    for r,c in zip([0,0,1,-1],[1,-1,0,0]):
        row=i+r
        col=j+c
        if(row>=0 and row<n and col>=0 and col<m and (not visited[row][col])):
            queue.append((row,col,v+1))
            visited[row][col]=True
print(*distance,sep="\n")
```

<h5>6.Surrounded Regions | Replace O’s with X’s</h5>
<p>Given a matrix mat of size N x M where every element is either ‘O’ or ‘X’. Replace all ‘O’ with ‘X’ that is surrounded by ‘X’. An ‘O’ (or a set of ‘O’) is considered to be surrounded by ‘X’ if there are ‘X’ at locations just below, just above just left, and just right of it.</p>
<p>Input : </p>
<img src="https://takeuforward.org/wp-content/uploads/2022/09/image-4.png" />
<p>Output : </p>
<img src="https://takeuforward.org/wp-content/uploads/2022/09/image-5.png" />

```python
n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[input().split() for i in range(n)]
visited=[[False]*m for i in range(n)]
queue=[]
for i in range(n):
    if(matrix[i][0]=='0'):
        queue.append((i,0))
        visited[i][0]=True
    if(matrix[i][m-1]=='0'):
        queue.append((i,m-1))
        visited[i][m-1]=True
        
for j in range(m):
    if(matrix[0][j]=='0'):
        queue.append((0,j))
        visited[0][j]=True
    if(matrix[n-1][j]=='0'):
        queue.append((n-1,j))
        visited[n-1][j]=True
while queue:
    temp=queue.pop(0)
    for i,j in zip([0,0,1,-1],[1,-1,0,0]):
        r=temp[0]+i
        c=temp[1]+j
        if(r<n and r>=0 and c<m and c>=0 and (not visited[r][c]) and matrix[r][c]=='0'):
            queue.append((r,c))
            visited[r][c]=True
for i in range(n):
    for j in range(m):
        if(visited[i][j]==False and matrix[i][j]=='0'):
            matrix[i][j]="x"
print(*matrix,sep="\n")
```

<h5>7.Number of Enclaves</h5>
<p>You are given an N x M binary matrix grid, where 0 represents a sea cell and 1 represents a land cell. A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid. Find the number of land cells in the grid for which we cannot walk off the boundary of the grid in any number of moves.</p>
<p>Input : </p>
<img src="https://takeuforward.org/wp-content/uploads/2022/09/image-8.png"/>
<p>Output : </p>
<img src="https://takeuforward.org/wp-content/uploads/2022/09/image-9.png"/>

```python
n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
queue=[]
visited=[[False]*m for i in range(n)]
for i in range(n):
    if(matrix[i][0]==1):
        queue.append((i,0))
    if(matrix[i][m-1]==1):
        queue.append((i,m-1))
for i in range(m):
    if(matrix[0][i]==1):
        queue.append((0,i))
    if(matrix[n-1][i]==1):
        queue.append((n-1,i))
while queue:
    temp=queue.pop(0)
    r,c=temp
    for i,j in zip([0,0,1,-1],[1,-1,0,0]):
        row,col=r+i,c+j
        if(row<n and col<m and row>=0 and col>=0 and (not visited[row][col]) and matrix[row][col]==1):
            queue.append((row,col))
            visited[row][col]=True
count=0
for i in range(n):
    for j in range(m):
        if((not visited[i][j]) and (matrix[i][j]==1)):
            count+=1
print(count)
```
<h5>8.Bipartite Graph | DFS Implementation</h5>
<p>Given an adjacency list of a graph adj of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.</p>
<p>If we are able to colour a graph with two colours such that no adjacent nodes have the same colour, it is called a bipartite graph.</p>	
<p>Input : </p>
<img src="https://lh6.googleusercontent.com/f1-CHQzuniIrn7WtinG5FaUW7Fh9qv-nh08tQIKzRR7eiH92ENP5zyEfhvVNVHcgd1eXYPXDaHuFBfcradut28yMnASlUzXs74hNSohogzR2ek3UmcKW__W4IVIklgGkz6uNUorESJaak5roRO5EKrb5gg377GenUZngD8O7Nq7UXQJ7RKWXbrG1dg"/>
<p>Output : 1</p>

<p>Input : </p>
<img src="https://lh4.googleusercontent.com/4uqS1cCTVVM7Y00AdKr344FE_xUnr0CcQTlV1gNrRey72wzHh-uyDQPbkT-KMSxQ9kiAIOQ-MCvSX211CivMoXf4rtQ1cKn4d8o7_OmtEtuFZ6I3h_8pNE6ReNXZvOg-5OVLUXZRYNTk1OGr6O8CBFtR5CiJqW8ub96i8hb3NJRUN28QjNXJzTxz_g"/>
<p>Output : 0</p>

```python
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
```

