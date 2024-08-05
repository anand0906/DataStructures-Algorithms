<h1>Binary Tree Traversal</h1>
<p>Tree traversal refers to the process of visiting each node in a tree data structure exactly once in a specific order</p>
<p>Traversal in binary trees can be broadly classified into two categories:</p>
<ol>
	<li>Depth First Search (DFS)</li>
	<li>Breadth Firts Search (BFS)</li>
</ol>
<p>Each uses a different strategy to visit the nodes within the tree.</p>

<h2>Depth First Search (DFS)</h2>

<p>Depth-First Search (DFS) is a method for exploring or traversing a tree or graph by starting at the root (or any node), and then exploring as far down one path as possible before backtracking to explore other paths.</p>
<p>In DFS, you start at the beginning, explore one direction completely until you can't go any further, then backtrack and explore other directions, repeating this process until all nodes are visited.</p>
<p><strong>How DFS Works</strong></p>
<ol>
	<li>Start at the root node</li>
	<li>Visit the current node</li>
	<li>Traverse each unvisited adjacent node from the current node by recursively applying the DFS algorithm.</li>
	<li>Backtrack to the previous node if there are no unvisited adjacent nodes.</li>
	<li>Repeat the process until all nodes are visited.</li>
</ol>
<p><strong>Real-Time Examples:</strong></p>
<ul>
	<li>Navigating a File System</li>
	<p>Imagine you are looking through folders on your computer. You start in the main folder, open a subfolder, then open another subfolder inside that one, and continue until you can't go any further. If you reach a folder with no more subfolders, you go back up to the previous folder and check the next subfolder.</p>
	<pre>
		Root
			├── Folder A
			│   ├── Folder B
			│   │   ├── File 1
			│   │   └── File 2
			│   └── Folder C
			│       ├── File 3
			│       └── Folder D
			│           └── File 4
			└── Folder E
			    ├── File 5
			    └── File 6
	</pre>
	<li>Solving a Maze</li>
	<p>When you try to solve a maze, you start at the entrance and follow one path as far as you can. If you reach a dead end, you go back to the last intersection and try a different path.</p>
	<pre>
		Entrance
		  |
		  |--A
		  |   |--B (Dead End)
		  |
		  |--C
		      |--D (Dead End)
		      |
		      |--E
		          |--Exit
	</pre>
</ul>

<h3>Types of DFS</h3>
<p>Depth-First Search (DFS) can be implemented in three primary ways, which are known as tree traversal methods.</p>
<p>hese methods determine the order in which nodes are visited. The three types are:</p>
<ol>
	<li>Inorder Traversal</li>
	<li>Preorder Traversal</li>
	<li>Postorder Traversal</li>
</ol>

<h4>Inorder Traversal</h4>
<p>Inorder Traversal is the type of Depth First Traversal where nodes are visited in the order</p>
<ol>
	<li>Left Subtree</li>
	<li>Root Node</li>
	<li>Right Subtree</li>
</ol>
<p>Imagine you are reading a book and want to read all the pages in a logical sequence. You first read the left half of the book, then the middle page, and finally the right half of the book.</p>
<p><strong>Procedure</strong></p>
<ul>
	<li><strong>Traverse the Left Subtree</strong>: Recursively apply the Inorder Traversal to the left subtree.</li>
	<li><strong>Visit the Current Node</strong>: Process the current node (e.g., print its value).</li>
	<li><strong>Traverse the Right Subtree</strong>:Recursively apply the Inorder Traversal to the right subtree.</li>
</ul>
<p>It's named "inorder" because it traverses the nodes in a sequence where the "Visit" step occurs between the left and right child nodes.</p>
<img src="https://static.takeuforward.org/content/Screenshot%202024-01-07%20at%208.32.00%20PM-FWEyDNjN">

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def InOrder(node,arr):
    if not node:
        return
    InOrder(node.left,arr)
    arr.append(node.data)
    InOrder(node.right,arr)
def main(root):
    #InOrder
    arr=[]
    InOrder(root,arr)
    print(arr)

```


<h4>Preorder Traversal</h4>
<p>Preorder Traversal is the type of Depth First Traversal where nodes are visited in the order</p>
<ol>
	<li>Root Node</li>
	<li>Left Subtree</li>
	<li>Right Subtree</li>
</ol>
<p>Think of it as inspecting a room before cleaning. You first note the room itself, then clean the left side, and finally the right side.</p>
<p><strong>Procedure</strong></p>
<ul>
	<li><strong>Visit the Current Node</strong>: Process the current node (e.g., print its value).</li>
	<li><strong>Traverse the Left Subtree</strong>: Recursively apply the Preorder Traversal to the left subtree.</li>
	<li><strong>Traverse the Right Subtree</strong>:Recursively apply the Preorder Traversal to the right subtree.</li>
</ul>
<p>It's named "preorder" because the "Visit" step occurs before traversing the left and right child nodes.</p>
<img src="https://static.takeuforward.org/content/Screenshot%202024-01-07%20at%208.44.51%20PM-786-gX9m">

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def PreOrder(node,arr):
    if not node:
        return
    arr.append(node.data)
    PreOrder(node.left,arr)
    PreOrder(node.right,arr)
def main(root):
    #PreOrder
    arr=[]
    PreOrder(root,arr)
    print(arr)
```

<h4>Postorder Traversal</h4>
<p>Postorder Traversal is the type of Depth First Traversal where nodes are visited in the order</p>
<ol>
	<li>Left Subtree</li>
	<li>Right Subtree</li>
	<li>Root Node</li>
</ol>
<p>Think of packing up a picnic. You pack up the items on the left side first, then the items on the right side, and finally the picnic basket itself.</p>
<p><strong>Procedure</strong></p>
<ul>
	<li><strong>Traverse the Left Subtree</strong>: Recursively apply the Postorder Traversal to the left subtree.</li>
	<li><strong>Traverse the Right Subtree</strong>:Recursively apply the Postorder Traversal to the right subtree.</li>
	<li><strong>Visit the Current Node</strong>: Process the current node (e.g., print its value).</li>
</ul>
<p>It's named "postorder" because the "Visit" step occurs after traversing the left and right child nodes.</p>
<img src="https://static.takeuforward.org/content/Screenshot%202024-01-07%20at%208.55.17%20PM-DgFI8ob3">

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def PostOrder(node,arr):
    if not node:
        return
    PostOrder(node.left,arr)
    PostOrder(node.right,arr)
    arr.append(node.data)
def main(root):
    #PostOrder
    arr=[]
    PostOrder(root,arr)
    print(arr)
```

<h2>Breadth First Search</h2>
<p>BFS explores a binary tree level by level, visiting all nodes at a given level before proceeding to the next level. BFS uses a queue data structure to maintain nodes at each level, ensuring that nodes at higher levels are visited before moving to lower levels.</p>
<p><strong>Real-Life Examples of BFS</strong></p>
<ul>
	<li>Level Order Processing:</li>
	<p>Classroom Attendance: Imagine calling out names for attendance class by class in a school, starting with the first grade, then the second grade, and so on.</p>
	<li>Social Network Friend Suggestions:</li>
	<p>Friend Recommendation: Social networks like Facebook use BFS to suggest friends by exploring immediate friends first, then friends of friends, and so on.</p>
</ul>

<h3>Level Order Traversal</h3>
<p>Level Order Traversal is the type of Breadth First Traversal where nodes are visited level by level, exploring each level completely before moving to the next level.</p>
<img src="https://static.takeuforward.org/content/Screenshot%202024-01-08%20at%2010.24.34%20AM-wmqzwxiP">
<p><strong>Procedure</strong></p>
<ul>
	<li><strong>Visit Nodes at Each Level</strong>: Starting from the root node, visit all nodes at level 0.</li>
	<li><strong>Move to Next Level</strong>: After visiting all nodes at level 0, move to level 1 and visit all nodes at this level from left to right..</li>
	<li><strong>Continue Level-wise</strong>:Repeat this process for subsequent levels, visiting nodes at each level from left to right until all levels are visited.</li>
</ul>


<p><strong>LevelOrder(node)</strong></p>
<ol>
  <li><strong>Start at the Root:</strong>
    <p>Begin with the root of the tree, as it's the starting point of the traversal.</p>
  </li>
  <li><strong>Use a Queue:</strong>
    <p>A queue is used to help process nodes level by level. The first node (root) is added to the queue.</p>
  </li>
  <li><strong>Process Nodes in Order:</strong>
    <p>While the queue is not empty, repeat the following steps:</p>
    <ul>
      <li>Remove (dequeue) the front node from the queue.</li>
      <li>Record the value of this node (add it to the result list).</li>
      <li>Add the left child of this node to the queue (if it exists).</li>
      <li>Add the right child of this node to the queue (if it exists).</li>
    </ul>
  </li>
  <li><strong>Move to the Next Level:</strong>
    <p>By adding the children of each node to the queue, the queue gradually contains all the nodes of the next level before moving on to the following level.</p>
  </li>
  <li><strong>Continue Until All Levels are Processed:</strong>
    <p>This process continues until all nodes in the tree are processed and the queue is empty.</p>
  </li>
</ol>

<p>The key idea is that the queue ensures nodes are processed in the correct order: first the current level, then the next level, and so on. This way, you get a list of nodes in their level order.</p>

<p><strong>LevelOrder_Print_LevelWise(node)</strong></p>
<ol>
  <li><strong>Start with the Root:</strong>
    <p>Begin at the root of the tree, which is the first level.</p>
  </li>
  <li><strong>Use a Queue:</strong>
    <p>Use a queue to help process nodes level by level. The first node (root) is added to the queue.</p>
  </li>
  <li><strong>Process Each Level:</strong>
    <p>While the queue is not empty:</p>
    <ul>
      <li>Determine the number of nodes at the current level by checking the size of the queue.</li>
      <li>Create an empty list to store the nodes of the current level.</li>
    </ul>
  </li>
  <li><strong>Process Each Node in the Current Level:</strong>
    <ul>
      <li>For each node at the current level:</li>
      <ul>
        <li>Remove the node from the queue.</li>
        <li>Add its value to the list for the current level.</li>
        <li>If the node has a left child, add it to the queue.</li>
        <li>If the node has a right child, add it to the queue.</li>
      </ul>
    </ul>
  </li>
  <li><strong>Move to the Next Level:</strong>
    <p>After processing all nodes at the current level, add the list of current level nodes to the result list.</p>
  </li>
  <li><strong>Repeat Until All Levels are Processed:</strong>
    <p>Continue this process until all nodes are processed and the queue is empty.</p>
  </li>
</ol>


```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque
def LevelOrder(node):
    ans=[]
    if(not node):
        return ans
    queue=deque()
    queue.append(node)
    while queue:
        current=queue.popleft()
        ans.append(current.data)
        if(current.left):
            queue.append(current.left)
        if(current.right):
            queue.append(current.right)
    return ans

def LevelOrder_Print_LevelWise(node):
    ans=[]
    if not node:
        return ans
    queue=deque()
    queue.append(node)
    while queue:
        n=len(queue)
        level=[]
        for i in range(n):
            current=queue.popleft()
            level.append(current.data)
            if(current.left):
                queue.append(current.left)
            if(current.right):
                queue.append(current.right)
        ans.append(level)
    return ans
def main(root):
    #LevelOrder
    ans=LevelOrder(root)
    print(ans)
    print(LevelOrder_Print_LevelWise(root))
```



<h1>Inorder Traversal (Iterative Approach)</h1>
<ol>
  <li><strong>In-Order Traversal:</strong>
    <p>In-order traversal means visiting the left subtree, then the root node, and finally the right subtree.</p>
  </li>
  <li><strong>Use a Stack:</strong>
    <p>A stack is used to keep track of nodes. This helps us to return to a node after finishing its left subtree.</p>
  </li>
  <li><strong>Start at the Root:</strong>
    <p>Begin with the root node and try to go as left as possible.</p>
  </li>
  <li><strong>Go Left:</strong>
    <p>Keep moving to the left child and push each node onto the stack until you reach a node with no left child.</p>
  </li>
  <li><strong>Process Node:</strong>
    <p>When you can't go left anymore, pop a node from the stack.</p>
    <p>Add the popped node's value to the result list (because it's now visited in in-order).</p>
  </li>
  <li><strong>Go Right:</strong>
    <p>Move to the right child of the popped node and repeat the process.</p>
  </li>
  <li><strong>Repeat Until Done:</strong>
    <p>Continue this process until there are no more nodes to visit (both stack and current node are empty).</p>
  </li>
</ol>

<img src="https://static.takeuforward.org/content/iterative-inorder-image5-LQQCJdeA">


```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def InOrder(node):
    ans=[]
    if not node:
        return ans
    stack=[]
    current=node
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        else:
            if not stack:
                break
            current=stack.pop()
            ans.append(current.data)
            current=current.right
    return ans

def main(root):
    print(InOrder(root))
```

<h1>PreOrder Traversal (Iterative Approach)</h1>
<ol>
  <li><strong>Pre-Order Traversal:</strong>
    <p>Pre-order traversal means visiting the root node first, then the left subtree, and finally the right subtree.</p>
  </li>
  <li><strong>Use a Stack:</strong>
    <p>A stack is used to help process nodes in the order required for pre-order traversal.</p>
  </li>
  <li><strong>Start at the Root:</strong>
    <p>Begin with the root node and push it onto the stack.</p>
  </li>
  <li><strong>Process Nodes:</strong>
    <ul>
      <li>While the stack is not empty:</li>
      <ul>
        <li>Pop a node from the stack.</li>
        <li>Add the popped node's value to the result list (because it's visited in pre-order).</li>
        <li>If the popped node has a right child, push it onto the stack.</li>
        <li>If the popped node has a left child, push it onto the stack.</li>
      </ul>
    </ul>
  </li>
  <li><strong>Repeat Until Done:</strong>
    <p>Continue this process until there are no more nodes to visit (the stack is empty).</p>
  </li>
</ol>

<p>The key idea is that by using a stack, you can visit nodes in the correct order for pre-order traversal: root, left, right. Here's a visual breakdown using a simple binary tree:</p>

<img src="https://static.takeuforward.org/content/preorder-binarytree-image7-LoL_nauS">

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def PreOrder(node):
    ans=[]
    if not node:
        return ans
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        ans.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return ans

def main(root):
    print(PreOrder(root))
```

<h1>PostOrder Traversal (Iterative Approach - 1)</h1>
<ol>
  <li><strong>Post-Order Traversal:</strong>
    <p>In post-order traversal, you visit the left subtree, then the right subtree, and finally the root node.</p>
  </li>
  <li><strong>Use a Stack:</strong>
    <p>A stack helps manage nodes and their traversal order. Initially, push the root node onto the stack.</p>
  </li>
  <li><strong>Processing Nodes:</strong>
    <ul>
      <li>While the stack is not empty:</li>
      <ul>
        <li>Pop a node from the stack.</li>
        <li>Add the node’s value to the result list.</li>
        <li>Push the left child of the node to the stack (if it exists).</li>
        <li>Push the right child of the node to the stack (if it exists).</li>
      </ul>
    </ul>
  </li>
  <li><strong>Reverse the Result:</strong>
    <p>Since nodes are added to the result list in a root-right-left order, reverse the list at the end to get the correct post-order traversal.</p>
  </li>
  <li><strong>Return the Result:</strong>
    <p>After reversing, the list contains the nodes in the post-order sequence.</p>
  </li>
</ol>
<p>Here’s a visual breakdown using a simple binary tree:</p>

<pre>
     1
   /   \
  2     3
 / \   / \
4   5 6   7
</pre>

<p>Step-by-step:</p>

<ol>
  <li>Start with the root node (1). Push it onto the stack.</li>
  <li>Pop (1) from the stack, add (1) to the result. Push its left child (2) and right child (3) to the stack.</li>
  <li>Pop (3) from the stack, add (3) to the result. Push its left child (6) and right child (7) to the stack.</li>
  <li>Pop (7) from the stack, add (7) to the result. (7) has no children.</li>
  <li>Pop (6) from the stack, add (6) to the result. (6) has no children.</li>
  <li>Pop (2) from the stack, add (2) to the result. Push its left child (4) and right child (5) to the stack.</li>
  <li>Pop (5) from the stack, add (5) to the result. (5) has no children.</li>
  <li>Pop (4) from the stack, add (4) to the result. (4) has no children.</li>
  <li>Stack is empty. Reverse the result list to get the final post-order sequence.</li>
</ol>

<p>Final result list (before reversing): [1, 3, 7, 6, 2, 5, 4]</p>
<p>Final result list (after reversing): [4, 5, 2, 6, 7, 3, 1]</p>


```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def PostOrder(node):
    ans=[]
    if not node:
        return ans
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        ans.append(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    ans.reverse()
    return ans

def main(root):
    print(PreOrder(root))
```

<h1>PostOrder Traversal (Iterative Approach - 2)</h1>
<ol>
  <li><strong>Post-Order Traversal:</strong>
    <p>In post-order traversal, you visit the left subtree, then the right subtree, and finally the root node.</p>
  </li>
  <li><strong>Use a Single Stack:</strong>
    <p>A single stack is used to manage nodes and their traversal order.</p>
  </li>
  <li><strong>Traversal with the Stack:</strong>
    <ul>
      <li>While either the stack is not empty or the current node is not <code>None</code>:</li>
      <ul>
        <li>If the current node is not <code>None</code>, push it onto the stack and move to its left child.</li>
        <li>If the current node is <code>None</code>, check the right child of the node at the top of the stack:</li>
        <ul>
          <li>If the right child exists and hasn’t been processed, move to the right child.</li>
          <li>If the right child is <code>None</code> or already processed, pop the node from the stack and add its value to the result list.</li>
          <li>Continue popping from the stack and adding values to the result list until the top of the stack is not the right child of the last processed node.</li>
        </ul>
      </ul>
    </ul>
  </li>
  <li><strong>Return the Result:</strong>
    <p>After processing all nodes, the result list contains the nodes in post-order.</p>
  </li>
</ol>

<img src="https://static.takeuforward.org/content/onestack-postorder-image3-6fRt5i1P">

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def PostOrder_Using_One_Stack(node):
    ans=[]
    if not node:
        return ans
    current=node
    stack=[]
    while stack or current:
        if(current):
            stack.append(current)
            current=current.left
        else:
            temp=stack[-1].right
            if not temp:
                temp=stack.pop()
                ans.append(temp.data)
                while stack and temp==stack[-1].right:
                    temp=stack.pop()
                    ans.append(temp.data)
            else:
                current=temp
    return ans

def main(root):
    print(PreOrder(root))
```

<h1>All Traversals In Single Loop</h1>

<ol>
  <li><strong>Initialize Lists and Stack:</strong>
    <p>Create empty lists for <code>preOrder</code>, <code>inOrder</code>, and <code>postOrder</code> to store the respective traversal results. Use a stack to help with the traversal. The stack stores tuples of the form [node, cnt], where <code>cnt</code> is a counter to keep track of the stage of processing for each node.</p>
  </li>
  <li><strong>Push Root Node:</strong>
    <p>Push the root node onto the stack with a counter value of <code>1</code> indicating the first visit.</p>
  </li>
  <li><strong>Process Nodes:</strong>
    <ul>
      <li>While the stack is not empty:</li>
      <ul>
        <li>Pop a node and its counter value from the stack.</li>
        <li>Depending on the counter value (<code>cnt</code>), determine which traversal operation to perform:</li>
        <ul>
          <li><strong><code>cnt == 1</code> (Pre-Order Visit):</strong>
            <p>Add the node’s value to the <code>preOrder</code> list. Increment the counter (<code>cnt = 2</code>) and push the node back onto the stack with the updated counter. Push the left child of the node onto the stack if it exists.</p>
          </li>
          <li><strong><code>cnt == 2</code> (In-Order Visit):</strong>
            <p>Add the node’s value to the <code>inOrder</code> list. Increment the counter (<code>cnt = 3</code>) and push the node back onto the stack with the updated counter. Push the right child of the node onto the stack if it exists.</p>
          </li>
          <li><strong><code>cnt == 3</code> (Post-Order Visit):</strong>
            <p>Add the node’s value to the <code>postOrder</code> list.</p>
          </li>
        </ul>
      </ul>
    </ul>
  </li>
  <li><strong>Return Results:</strong>
    <p>After processing all nodes, return the <code>preOrder</code>, <code>inOrder</code>, and <code>postOrder</code> lists.</p>
  </li>
</ol>

<img src="https://static.takeuforward.org/content/preorder-post-binarytree-image6-RyxeaYpQ">


```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def solve(node):
    preOrder,inOrder,postOrder=[],[],[]
    if(not node):
        return preOrder,inOrder,postOrder
    stack=[]
    stack.append([node,1])
    while stack:
        current,cnt=stack.pop()
        if(cnt==1):
            preOrder.append(current.data)
            cnt+=1
            stack.append([current,cnt])
            if(current.left):
                stack.append([current.left,1])
        elif(cnt==2):
            inOrder.append(current.data)
            cnt+=1
            stack.append([current,cnt])
            if(current.right):
                stack.append([current.right,1])
        else:
            postOrder.append(current.data)
    return preOrder,inOrder,postOrder

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.left.right=Node(9)
root.left.left.right.left=Node(1)
root.right.left=Node(7)
root.right.right=Node(6)
root.right.right.left=Node(8)
print(solve(root))
```