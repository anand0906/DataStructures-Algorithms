<h1>Topological Sorting</h1>
<p>Topological sorting is a method used to order the vertices of a directed graph in such a way that for every directed edge u→v, vertex u comes before vertex v in the ordering.</p>
<p>it arranges the nodes of a graph in a linear order, such that if there is a path from node A to node B, then node A appears before node B in the ordering.</p>
<p><strong>Applications</strong></p>
<ul>
	<li><strong>Task scheduling and dependency resolution</strong>: In project management and computer science, tasks often have dependencies on each other. Topological sorting can be used to determine the order in which tasks should be executed based on their dependencies.</li>
	<li><strong>Compiler design</strong>: In compilers, topological sorting is used to determine the order in which various modules or functions should be compiled based on their dependencies.</li>
	<li><strong>Course scheduling</strong>: In universities, courses often have prerequisites. Topological sorting can be used to schedule courses in such a way that all prerequisites are completed before a course is taken.</li>
	<li><strong>Data dependency analysis</strong>: In parallel computing and optimization, topological sorting can be used to analyze data dependencies between different tasks or instructions.</li>
	<li><strong>Network routing</strong>: In computer networks, topological sorting can be used to determine the order in which data should be routed through the network based on the topology of the network.</li>
</ul>
<p>It can be implmented in two ways</p>
<ul>	
	<li>Using DFS</li>
	<li>Khan's Algorithm</li>
</ul>
<h2>Topological Sort Algorithm | DFS</h2>
<p>Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.</p>
<p><strong>Example 1:</strong></p>
<p>Input: V = 6, E = 6</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/10/image-14.png">
<p>Output: 5, 4, 2, 3, 1, 0</p>
<p>Explanation: A graph may have multiple topological sortings. The result is one of them. The necessary conditions for the ordering are:</p>
<ul>	
	<li>According to edge 5 -> 0, node 5 must appear before node 0 in the ordering.</li>
	<li>According to edge 4 -> 0, node 4 must appear before node 0 in the ordering.</li>
	<li>According to edge 5 -> 2, node 5 must appear before node 2 in the ordering.</li>
	<li>According to edge 2 -> 3, node 2 must appear before node 3 in the ordering.</li>
	<li>According to edge 3 -> 1, node 3 must appear before node 1 in the ordering.</li>
	<li>According to edge 4 -> 1, node 4 must appear before node 1 in the ordering.</li>
</ul>
<p>The above result satisfies all the necessary conditions. [4, 5, 2, 3, 1, 0] is also one such topological sorting that satisfies all the conditions.</p>
<p><strong>Example 2:</strong></p>
<p>Input: V = 4, E = 3</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/10/image-15.png">
<p>Result: 3, 2, 1, 0</p>
<p>Explanation: The necessary conditions for the ordering are:</p>
<ul>	
	<li>For edge 1 -> 0 node 1 must appear before node 0.</li>
	<li>For edge 2 -> 0 node 1 must appear before node 0.</li>
	<li>For edge 3 -> 0 node 1 must appear before node 0.</li>
</ul>
<p>[2, 3, 1, 0] is also another topological sorting for the graph.</p>

<p><strong>Solution :</strong></p>
<p>First, let's understand DFS. It's a way to traverse or visit all the nodes of a graph, starting from a particular node. It explores as far as possible along each branch before backtracking.</p>
<p>When using DFS for topological sorting, we perform DFS on each unvisited node in the graph. While doing DFS, we mark the current node as visited and recursively visit all its adjacent nodes.</p>
<p>Once you've visited all neighbors of the current node, backtrack. Before you backtrack, store the current node in a list or stack. This is important because we want to remember the order in which we finish exploring each node.</p>
<p>Once all nodes are visited, the list or stack you stored the nodes in will give you the topological ordering.</p>
<p>The stack helps us keep track of the order in which the nodes are visited. The node that is added to the stack last will come first in the topological ordering because it has no outgoing edges remaining to explore.</p>
<p>Once DFS has been performed on all nodes, the stack will contain the nodes in the reverse order of the topological sorting. So, we pop nodes from the stack one by one. The order in which we pop the nodes from the stack gives us the topological sorting of the graph.</p>
<p><strong>Steps To Solve : </strong></p>
<ol>
	<li>Create adjacency list for given nodes and edges</li>
	<li>Create a visited array for given nodes, mark it as unvisited by default</li>
	<li>create stack to store ordered nodes</li>
	<li>Loop through each node in visited array, for each unvisted node, start doing dfs</li>
	<li>Dfs of node will follow steps as below</li>
	<ol>
		<li>Mark current node as visited</li>
		<li>loop through adjcent nodes of current node</li>
		<li>perform bfs for each adjcent node which is unvisited</li>
		<li>add current node to stack</li>
	</ol>
	<li>Once, dfs completed for all nodes</li>
	<li>print nodes in stack in reverse , will give the sorted nodes of given graph</li>
</ol>

```python
def dfs(node,graph,visited,stack):
    visited[node]=True
    for adj in graph[node]:
        if(not visited[adj]):
            dfs(adj,graph,visited,stack)
    stack.append(node)
nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(nodes)}
visited={i:False for i in range(nodes)}
stack=[]
for i,j in edges_converted:
    graph[i].add(j)
for i in range(nodes):
    if(not visited[i]):
        dfs(i,graph,visited,stack)
print(*stack[::-1])
```
<p>Time Complexity: O(V+E)+O(V), where V = no. of nodes and E = no. of edges. There can be at most V components. So, another O(V) time complexity.</p>
<p>Space Complexity: O(2N) + O(N) ~ O(2N): O(2N) for the visited array and the stack carried during DFS calls and O(N) for recursive stack space, where N = no. of nodes.</p>

<h2> Kahn's Algorithm Topological Sort Algorithm BFS </h2>
<p>Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.</p>
<p><strong>Solution : </strong></p>
<p>Previously, we solved this question using the DFS traversal technique. But in this article,  we will apply the BFS(Breadth First Search) traversal technique.</p>
<p>BFS is another graph traversal algorithm. Instead of going as deep as possible, like DFS, it explores neighbors of nodes before moving on to the next level of neighbors.</p>
<p>When using BFS for topological sorting, we start by finding nodes with no incoming edges (nodes with zero in-degree) and enqueueing them. Then, we repeatedly dequeue nodes, adding them to the topological ordering, and removing their outgoing edges. This process continues until all nodes have been visited.</p>
<p>In BFS, we use a queue data structure to keep track of nodes to visit. We enqueue nodes with no incoming edges first and then dequeue nodes to explore their neighbors.</p>
<p>As we dequeue nodes, we add them to the topological ordering. The order in which nodes are added to the ordering is the topological order of the graph.</p>

<p><strong>Steps to solve : </strong></p>
<li>
	<ol>Create adjacency list for given nodes and edges</ol>
	<ol>Create a visited array for given nodes, mark it as unvisited by default</ol>
	<ol>Create an indegree array to store the indegree of each node</ol>
	<ol>Create a queue for doing bfs</ol>
	<ol>Create a topoSort array to store ordered nodes</ol>
	<ol>Add nodes with indegree as 0 to the queue</ol>
	<ol>while queue is no empty perform following steps</ol>
	<li>
		<ol>pop element from queue</ol>
		<ol>add popped element to topoSort array</ol>
		<ol>loop through its adjcent nodes</ol>
		<ol>decrease the indegree of adj node by 1</ol>
		<ol>if indegree of adj node is zero, add it to queue</ol>	
	</li>
</li>

```python
nodes,edge=list(map(int,input().split()))
edges=[list(map(int,input().split())) for i in range(edge)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(nodes)}
indegree={i:0 for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    indegree[j]+=1
queue=[]
for i in range(nodes):
    if(indegree[i]==0):
        queue.append(i)
topoSort=[]
while queue:
    currentNode=queue.pop(0)
    topoSort.append(currentNode)
    for adj in graph[currentNode]:
        indegree[adj]-=1
        if(indegree[adj]==0):
            queue.append(adj)
print(topoSort)
```

<p>Time Complexity: O(V+E), where V = no. of nodes and E = no. of edges. This is a simple BFS algorithm.</p>
<p>Space Complexity: O(N) + O(N) ~ O(2N), O(N) for the indegree array, and O(N) for the queue data structure used in BFS(where N = no.of nodes).</p>

<h2>Cycle Detection In Directed Graph Using Topological Sorting</h2>
<p>Given directed graph, we have to check whether it contains cycle or not</p>
<p><strong>Solution : </strong></p>
<p>We know that,  a directed acyclic graph (DAG), every node should have at least one incoming edge, as nodes are ordered based on their dependencies.</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/10/image-11.png">
<p>If we try to get topological sorting of this cyclic graph, for edge 1->2, node 1 must appear before 2, for edge 2->3, node 2 must appear before 3, and for edge 3->1, node 3 must appear before 1 in the linear ordering. But such ordering is not possible as there exists a cyclic dependency in the graph. Thereby, topological sorting is only possible for a directed acyclic graph.</p>
<p>So, apply topological sorting on given directed graph</p>
<p>if final toposort contains all nodes, means topoSort is success, graph doesn't contains any cycles</p>
<p>Otherwise, given graph contains cycle</p>
<p><strong>Steps to Solve</strong></p>
<ol>
	<li>Apply Topological Sort For Given Directed Graph</li>
	<li>if length of final topoSort is equal to number of nodes, then return false, means no cycle</li>
	<li>otherwise, return true, graph contains cycle</li>
</ol>

```python
nodes,edge=list(map(int,input().split()))
edges=[list(map(int,input().split())) for i in range(edge)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(nodes)}
indegree={i:0 for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    indegree[j]+=1
queue=[]
for i in range(nodes):
    if(indegree[i]==0):
        queue.append(i)
topoSort=[]
while queue:
    currentNode=queue.pop(0)
    topoSort.append(currentNode)
    for adj in graph[currentNode]:
        indegree[adj]-=1
        if(indegree[adj]==0):
            queue.append(adj)
if(len(topoSort)==nodes):
    print("No Cycle Found")
else:
    print("Cycle Found")
```

<p>Time Complexity: O(V+E), where V = no. of nodes and E = no. of edges. This is a simple BFS algorithm.</p>
<p>Space Complexity: O(N) + O(N) ~ O(2N), O(N) for the indegree array, and O(N) for the queue data structure used in BFS(where N = no.of nodes).</p>

<h2>Course Schedule - 1</h2>
<p>There are a total of n tasks you have to pick, labeled from 0 to n-1. Some tasks may have prerequisites tasks, for example, to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]</p>
<p>Given the total number of n tasks and a list of prerequisite pairs of size m. Find the order of tasks you should pick to finish all tasks.</p>
<p>Note: There may be multiple correct orders, you need to return one of them. If it is impossible to finish all tasks, return an empty array.</p>

<p><strong>Example 1:</strong></p>
<p>Input: N = 4, P = 3,  array[] = {{1,0},{2,1},{3,2}}</p>
<p>Output: 3 2 1 0</p>
<p>Explanation: It is possible to finish all the tasks in the order : 3 2 1 0.
First, we will finish task 3. Then we will finish task 2, task 1, and task 0</p>

<p><strong>Example 2</strong></p>
<p>Input: N = 4, P = 4,  array[] = {{1,2},{4,3},{2,4},{4,1}}</p>
<p>Output: </p>
<p>It is impossible to finish all the tasks. Let’s analyze the pairs:
For pair {1, 2} -> we need to finish task 1 first and then task 2. (order : 1 2).
For pair{4, 3} -> we need to finish task 4 first and then task 3. (order: 4 3).
For pair {2, 4} -> we need to finish task 2 first and then task 4. (order: 1 2 4 3).
But for pair {4, 1} -> we need to finish task 4 first and then task 1 but this pair contradicts the previous pair. So, it is not possible to finish all the tasks.</p>


<p><strong>Solution</strong></p>
<p>Given a n number of courses and dependency among each others</p>
<p>we need find order in which courses should be finshed</p>
<p>we can represent the problem in terms of directed graph</p>
<p>nodes -> tasks</p>
<p>edges -> dependencies</p>
<p>we can apply topological sorting to get the order of tasks</p>
<p>given prerequsite order is, [a,b] a depend on b, so edge should be [b,a]</p>

```python
tasks,dependencies=list(map(int,input().split()))
nodes=tasks
edges=[list(map(int,input().split())) for i in range(dependencies)]
edges_converted=[(int(j),int(i)) for i,j in edges] # order should be correct
graph={i:set() for i in range(nodes)}
indegree={i:0 for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    indegree[j]+=1
queue=[]
for i in range(nodes):
    if(indegree[i]==0):
        queue.append(i)
topoSort=[]
while queue:
    currentNode=queue.pop(0)
    topoSort.append(currentNode)
    for adj in graph[currentNode]:
        indegree[adj]-=1
        if(indegree[adj]==0):
            queue.append(adj)
print(topoSort)
```

<p>Time Complexity: O(V+E), where V = no. of nodes and E = no. of edges. This is a simple BFS algorithm.</p>
<p>Space Complexity: O(N) + O(N) ~ O(2N), O(N) for the indegree array, and O(N) for the queue data structure used in BFS(where N = no.of nodes).</p>

<h2>Course Schedule - 2</h2>
<p>There are a total of n tasks you have to pick, labeled from 0 to n-1. Some tasks may have prerequisites tasks, for example, to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]</p>
<p>Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.</p>

<p><strong>Example 1:</strong></p>
<p>Input: N = 4, P = 3,  array[] = {{1,0},{2,1},{3,2}}</p>
<p>Output: Yes</p>
<p>Explanation: It is possible to finish all the tasks in the order : 3 2 1 0.
First, we will finish task 3. Then we will finish task 2, task 1, and task 0</p>

<p><strong>Example 2</strong></p>
<p>Input: N = 4, P = 4,  array[] = {{1,2},{4,3},{2,4},{4,1}}</p>
<p>Output: No</p>
<p>It is impossible to finish all the tasks. Let’s analyze the pairs:
For pair {1, 2} -> we need to finish task 1 first and then task 2. (order : 1 2).
For pair{4, 3} -> we need to finish task 4 first and then task 3. (order: 4 3).
For pair {2, 4} -> we need to finish task 2 first and then task 4. (order: 1 2 4 3).
But for pair {4, 1} -> we need to finish task 4 first and then task 1 but this pair contradicts the previous pair. So, it is not possible to finish all the tasks.</p>


<p><strong>Solution</strong></p>
<p>Given a n number of courses and dependency among each others</p>
<p>we need find whether it is possible to finish courses</p>
<p>we can represent the problem in terms of directed graph</p>
<p>nodes -> tasks</p>
<p>edges -> dependencies</p>
<p>we can apply topological sorting to get the order of tasks</p>
<p>if length of topoSort is equal to number of tasks them it is possible to finish, otherwise not possible</p>
<p>given prerequsite order is, [a,b] a depend on b, so edge should be [b,a]</p>

```python
tasks,dependencies=list(map(int,input().split()))
nodes=tasks
edges=[list(map(int,input().split())) for i in range(dependencies)]
edges_converted=[(int(j),int(i)) for i,j in edges] # order should be correct
graph={i:set() for i in range(nodes)}
indegree={i:0 for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    indegree[j]+=1
queue=[]
for i in range(nodes):
    if(indegree[i]==0):
        queue.append(i)
topoSort=[]
while queue:
    currentNode=queue.pop(0)
    topoSort.append(currentNode)
    for adj in graph[currentNode]:
        indegree[adj]-=1
        if(indegree[adj]==0):
            queue.append(adj)
if(len(topoSort)==nodes):
    print("Yes")
else:
    print("No")
```

<p>Time Complexity: O(V+E), where V = no. of nodes and E = no. of edges. This is a simple BFS algorithm.</p>
<p>Space Complexity: O(N) + O(N) ~ O(2N), O(N) for the indegree array, and O(N) for the queue data structure used in BFS(where N = no.of nodes).</p>

<h2>Find Eventual Safe States - BFS - Topological Sort</h2>
<p>A directed graph of V vertices and E edges is given in the form of an adjacency list adj. Each node of the graph is labeled with a distinct integer in the range 0 to V - 1. A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node. You have to return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.</p>
<p><strong>Example 1:</strong></p>
<p>Input Format: N = 7, E = 7</p>
<img src="Input Format: N = 7, E = 7">
<p>Result: {2 4 5 6}</p>
<p>Explanation: Here terminal nodes are 5 and 6 as they have no outgoing edges.</p>
<p>From node 0: two paths are there 0->2->5 and 0->1->3->0. The second path does not end at a terminal node. </p>
<p>So it is not a safe node.</p>
<p>From node 1: two paths exist: 1->3->0->1 and 1->2->5. But the first one does not end at a terminal node. So it is not a safe node.</p>
<p>From node 2: only one path: 2->5 and 5 is a terminal node. So it is a safe node.</p>
<p>From node 3: two paths: 3->0->1->3 and 3->0->2->5 but the first path does not end at a terminal node.So it is not a safe node.From node 4: Only one path: 4->5 and 5 is a terminal node. 
So it is also a safe node. </p>
<p>From node 5: It is a terminal node. So it is a safe node as well.</p>
<p>From node 6: It is a terminal node. So it is a safe node as well.</p>
<p><strong>Example 2 :</strong></p>
<p>Input Format: N = 4, E = 4</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/image.png">
<p>Result: {3}</p>
<p>Explanation: Node 3 itself is a terminal node and it is a safe node as well. But all the paths from other nodes do not lead to a terminal node. So they are excluded from the answer.</p>

<p><strong>Solution : </strong></p>
<p>A terminal node is a node without any outgoing edges(i.e outdegree = 0). Now a node is considered to be a safe node if all possible paths starting from it lead to a terminal node.</p>
<p>Here we need to find out all safe nodes and return them sorted in ascending order. </p>
<p>If we closely observe, all possible paths starting from a node are going to end at some terminal node unless there exists a cycle and the paths return back to themselves</p>
<p>So, we need to find nodes with outdegree is zero and its associated nodes without cycle</p>
<p>we can apply topological sort for this</p>
<p>The node with outdegree 0 is considered to be a terminal node but the topological sort algorithm deals with the indegrees of the nodes.</p>
<p>	So, to use the topological sort algorithm, we will reverse every edge of the graph. Now, the nodes with indegree 0 become the terminal nodes. After this step, we will just follow the topological sort algorithm as it is.</p>
<p><strong>Steps To Solve</strong></p>
<ol>	
	<li>reverse the edges of given graph</li>
	<li>Apply topological sort</li>
	<li>print the resulted topo sort in sorted order</li>
</ol>

```python
nodes,edge=list(map(int,input().split()))
edges=[list(map(int,input().split())) for i in range(edge)]
edges_converted=[(int(j),int(i)) for i,j in edges]
graph={i:set() for i in range(nodes)}
indegree={i:0 for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    indegree[j]+=1
queue=[]
for i in range(nodes):
    if(indegree[i]==0):
        queue.append(i)
safeNodes=[]
while queue:
    currentNode=queue.pop(0)
    safeNodes.append(currentNode)
    for adj in graph[currentNode]:
        indegree[adj]-=1
        if(indegree[adj]==0):
            queue.append(adj)
print(sorted(safeNodes))
```

<p>Time Complexity: O(V+E), where V = no. of nodes and E = no. of edges. This is a simple BFS algorithm.</p>
<p>Space Complexity: O(N) + O(N) ~ O(2N), O(N) for the indegree array, and O(N) for the queue data structure used in BFS(where N = no.of nodes).</p>

<h2>Alien Dictionary - Topological Sort</h2>
<p>Given a sorted dictionary of an alien language having N words and k starting alphabets of a standard dictionary. Find the order of characters in the alien language.</p>
<p>Many orders may be possible for a particular test case, thus you may return any valid order.</p>
<p><strong>Example 1:</strong></p>
<p>Input: N = 5, K = 4</p>
<p>dict = {"baa","abcd","abca","cab","cad"}</p>
<p>Output: b d a c</p>
<p>We will analyze every consecutive pair to find out the order of the characters.
The pair “baa” and “abcd” suggests ‘b’ appears before ‘a’ in the alien dictionary.
The pair “abcd” and “abca” suggests ‘d’ appears before ‘a’ in the alien dictionary.
The pair “abca” and “cab” suggests ‘a’ appears before ‘c’ in the alien dictionary.
The pair “cab” and “cad” suggests ‘b’ appears before ‘d’ in the alien dictionary.
So, [‘b’, ‘d’, ‘a’, ‘c’] is a valid ordering.</p>
<p>Example 2:</p>
<p>Input: N = 3, K = 3</p>
<p>dict = {"caa","aaa","aab"}</p>
<p>Output: c a b</p>
<p>Explanation: Similarly, if we analyze the consecutive pair for this example, we will figure out [‘c’, ‘a’, ‘b’] is a valid ordering.</p>

<p><strong>Solution : </strong></p>
<p>Given an sorted list of strings</p>
<p>We need to find the order of alphabets</p>
<p>Let’s consider the first example where N = 5, K = 4 and dict = {"baa", "abcd", "abca", "cab", "cad"}. So, here we need to find out the correct ordering of the first 4 letters of the alphabet(i.e. ‘a’, ‘b’, ‘c’, ‘d’).</p>
<p>If we consider the first 2 words and try to figure out why “baa” appears before “abcd”, we can clearly observe that they are differentiated by the first letter i.e. ‘b’ and ‘a’. </p>
<p>hat is why, we can conclude that in the alien dictionary, ‘b’ appears before ‘a’( i.e. ‘b’ is smaller than ‘a’). We can correspond this differentiating factor to a directed graph like the following:</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/Screenshot-2022-11-08-182031.png">
<p>Let’s understand why we need not check “baa” and “abca” (the 1st and the 3rd word) next:</p>
<p>Until now, we have figured out why “baa” appears before “abcd”. So, by convention, if “abcd” is appearing before “abca” and “baa” is appearing before “abcd”, “baa” will obviously appear before “abca”. That is why we will check the pair of “abcd” and “abca” next rather than checking “baa” with any other words and this flow will be continued for the rest of the words.</p>
<p>Points to remember that we need not check every pair of words rather we will just check the consecutive pair of words in the dictionary. Comparing each pair of consecutive words in the dictionary, we can construct a directed graph like the following:</p>
<img src="https://static.takeuforward.org/wp/uploads/2022/11/Screenshot-2022-11-08-182153.png">
<p>	Now, we have successfully reduced the problem to a known directed graph problem. If we look at the problem from the graph point of view, we just need to find out the linear ordering of the nodes of the directed graph. And we can do this easily using the topological sort algorithm which we have previously learned.</p>
<p><strong>Steps To Solve : </strong></p>
<p>Compare Consecutive Words in given list, find out charcters differed</p>
<p>create graph from that charcters</p>
<p>apply topological sorting for that graph</p>
<p>print topoSort order</p>

```python
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
```

<p>Time Complexity: O(N*len)+O(K+E), where N is the number of words in the dictionary, ‘len’ is the length up to the index where the first inequality occurs, K = no. of nodes, and E = no. of edges.</p>
<p>Space Complexity: O(K) + O(K)+O(K)+O(K) ~ O(4K), O(K) for the indegree array, and O(K) for the queue data structure used in BFS(where K = no.of nodes), O(K) for the answer array and O(K) for the adjacency list used in the algorithm.</p>