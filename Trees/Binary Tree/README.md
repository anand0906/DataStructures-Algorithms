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

<h1>Height / Maximum Depth Of Given Tree</h1>
<p>Given the root of a binary tree, return its maximum depth.</p>
<p>A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.</p>
<p><strong>Examples : </strong></p>
<img src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg">
<p><strong>Input :</strong>root = [3,9,20,null,null,15,7]</p>
<p><strong>Output :</strong>3</p>
<img src="https://static.takeuforward.org/content/depth-binary-image1-4ZMPxYhK">
<p><strong>Input :</strong>Binary Tree: 1 2 5 -1 -1 4 6 5</p>
<p><strong>Output :</strong>4</p>
<p>In the above example, the height of the binary tree is along the longest path from the root node 1 -> 5 -> 4 -> 5. </p>
<img src="https://static.takeuforward.org/content/depth-of-binary-tree-image3-AKue3nNZ">
<p><strong>Input :</strong>Binary Tree: 3 1 2</p>
<p><strong>Output :</strong>2</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in two approaches</p>

<p><strong>Recursive Approach</strong></p>
<p>Here, to find out height of a partcular node, it will ask its left node's height and right node's height recursively, then it will consider max height and by adding 1 to max height to include current node, we will get height of that partcular node</p>
<ol>
    <li><strong>Check if Node is Empty:</strong>
        <ul>
            <li>If the current node is <strong>None</strong>, the height is <strong>0</strong>.</li>
            <li>This is your stopping condition.</li>
        </ul>
    </li>
    <li><strong>Calculate Heights of Subtrees:</strong>
        <ul>
            <li>Find the height of the left subtree.</li>
            <li>Find the height of the right subtree.</li>
        </ul>
    </li>
    <li><strong>Combine and Add One:</strong>
        <ul>
            <li>Take the maximum height of the left and right subtrees.</li>
            <li>Add <strong>1</strong> to this maximum height (for the current node).</li>
        </ul>
    </li>
</ol>

<p><strong>Visualization:</strong></p>
<p>Think of it like climbing a tree:</p>
<ol>
    <li><strong>Base Camp (Empty Node):</strong>
        <ul>
            <li>If there’s no tree (node is <strong>None</strong>), you’re at base camp, so height is <strong>0</strong>.</li>
        </ul>
    </li>
    <li><strong>Explore Left and Right Paths:</strong>
        <ul>
            <li>Look at the left path (left subtree) and see how high you can go.</li>
            <li>Look at the right path (right subtree) and see how high you can go.</li>
        </ul>
    </li>
    <li><strong>Find the Highest Point:</strong>
        <ul>
            <li>The highest point you can reach from the current node is <strong>1 + the higher path (left or right)</strong>.</li>
        </ul>
    </li>
</ol>

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def findHeight(node):
    if not node:
        return 0
    leftHeight=findHeight(node.left)
    rightHeight=findHeight(node.right)
    return 1+max(leftHeight,rightHeight)

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.left.right=Node(9)
root.left.left.right.left=Node(1)
root.right.left=Node(7)
root.right.right=Node(6)
root.right.right.left=Node(8)
print(findHeight(root))
```

<p><strong>Time Complexity :</strong>O(n), atmost we will visit each node at once</p>
<p><strong>Space Complexity :</strong>O(n), recursion call stack will store maximum of given nodes</p>

<p><strong>Example 1: Height 0</strong></p>
<p><strong>Diagram:</strong></p>
<pre>
  (None)
</pre>
<p><strong>Explanation:</strong></p>
<ul>
    <li>If the tree is empty (i.e., there is no root node), its height is 0.</li>
</ul>
<p><strong>Flow:</strong></p>
<ol>
    <li>The function <code>findHeight</code> is called with <code>node = None</code>.</li>
    <li>The function checks if <code>node</code> is <code>None</code>. Since it is, it returns 0.</li>
</ol>
<p><strong>Code:</strong></p>
<pre>
node = None
print(findHeight(node))  # Output: 0
</pre>

<p><strong>Example 2: Height 1</strong></p>
<p><strong>Diagram:</strong></p>
<pre>
    1
   / \
(None)(None)
</pre>
<p><strong>Explanation:</strong></p>
<ul>
    <li>The tree has only one node (the root), with no children.</li>
    <li>Height is 1 (from the root to itself).</li>
</ul>
<p><strong>Flow:</strong></p>
<ol>
    <li>The function <code>findHeight</code> is called with the root node <code>1</code>.</li>
    <li>The function checks if <code>node</code> is <code>None</code>. It's not, so it proceeds to calculate the heights of the left and right subtrees.</li>
    <li>It calls <code>findHeight</code> on <code>node.left</code> (which is <code>None</code>) and gets 0.</li>
    <li>It calls <code>findHeight</code> on <code>node.right</code> (which is <code>None</code>) and gets 0.</li>
    <li>It returns <code>1 + max(0, 0)</code>, which is 1.</li>
</ol>
<p><strong>Code:</strong></p>
<pre>
root = TreeNode(1)
print(findHeight(root))  # Output: 1
</pre>

<p><strong>Example 3: Height 2</strong></p>
<p><strong>Diagram:</strong></p>
<pre>
    1
   / \
  2   3
 / \
(None)(None)
</pre>
<p><strong>Explanation:</strong></p>
<ul>
    <li>The tree has a root and two levels. The root has two children, and each child has no children.</li>
    <li>The height is 2 (from the root to the farthest leaf).</li>
</ul>
<p><strong>Flow:</strong></p>
<ol>
    <li>The function <code>findHeight</code> is called with the root node <code>1</code>.</li>
    <li>The function checks if <code>node</code> is <code>None</code>. It's not, so it proceeds to calculate the heights of the left and right subtrees.</li>
    <li>It calls <code>findHeight</code> on <code>node.left</code> (node <code>2</code>).</li>
    <ul>
        <li>For node <code>2</code>:</li>
        <ol>
            <li>It calls <code>findHeight</code> on <code>node.left</code> (which is <code>None</code>) and gets 0.</li>
            <li>It calls <code>findHeight</code> on <code>node.right</code> (which is <code>None</code>) and gets 0.</li>
            <li>It returns <code>1 + max(0, 0)</code>, which is 1.</li>
        </ol>
    </ul>
    <li>It calls <code>findHeight</code> on <code>node.right</code> (node <code>3</code>).</li>
    <ul>
        <li>For node <code>3</code>:</li>
        <ol>
            <li>It calls <code>findHeight</code> on <code>node.left</code> (which is <code>None</code>) and gets 0.</li>
            <li>It calls <code>findHeight</code> on <code>node.right</code> (which is <code>None</code>) and gets 0.</li>
            <li>It returns <code>1 + max(0, 0)</code>, which is 1.</li>
        </ol>
    </ul>
    <li>It returns <code>1 + max(1, 1)</code>, which is 2.</li>
</ol>
<p><strong>Code:</strong></p>
<pre>
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(findHeight(root))  # Output: 2
</pre>

<p><strong>Iterative Approach</strong></p>
<p>Here, we can use level order traversal to find out height, since number of levels in given tree will be the height of our tree</p>
<ol>
    <li>
        <strong>Understanding Tree Height</strong>:
        <ul>
            <li>The height of a tree is the number of levels or layers it has.</li>
            <li>A single node tree has a height of 1, and an empty tree has a height of 0.</li>
        </ul>
    </li>
    <li>
        <strong>Using a Queue for Level-by-Level Processing</strong>:
        <ul>
            <li>To find the height, we use a queue to help us process each level of the tree one by one.</li>
            <li>A queue is like a line where you add items to the back and take them from the front.</li>
        </ul>
    </li>
    <li>
        <strong>Starting with the Root</strong>:
        <ul>
            <li>We start by putting the root node (the topmost node of the tree) into the queue.</li>
        </ul>
    </li>
    <li>
        <strong>Processing Each Level</strong>:
        <ul>
            <li>While the queue is not empty, we do the following:</li>
            <ul>
                <li>Count the number of nodes currently in the queue. This represents all the nodes at the current level.</li>
                <li>Remove each of these nodes from the queue, and for each node, add its children (left and right) to the queue.</li>
                <li>After processing all nodes at the current level, increase the level count by 1.</li>
            </ul>
        </ul>
    </li>
    <li>
        <strong>Continuing Until All Levels Are Processed</strong>:
        <ul>
            <li>We repeat the above steps until there are no more nodes left in the queue.</li>
            <li>Each time we finish processing a level, we move to the next level by working on the nodes that were added to the queue.</li>
        </ul>
    </li>
    <li>
        <strong>Result</strong>:
        <ul>
            <li>The number of times we increase the level count is equal to the height of the tree.</li>
        </ul>
    </li>
</ol>


```python
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findHeight2(node):
    if not node:
        return 0
    queue = deque()
    queue.append(node)
    level = 0
    while queue:
        n = len(queue)
        for i in range(n):
            temp = queue.popleft()
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        level += 1
    return level

# Example usage
if __name__ == "__main__":
    # Constructing a simple binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Height of the tree is:", findHeight2(root))

```


<p><strong>Time Complexity :</strong>O(n)</p>
<p>The function processes each node exactly once. It enqueues and dequeues each node one time, leading to a time complexity that is directly proportional to the number of nodes in the tree.</p>
<p><strong>Space Complexity :</strong>O(n)</p>
<p> In the worst case, the queue can hold up to half of the nodes (if the tree is a complete binary tree). This happens because the widest part of the tree (the level with the most nodes) determines the maximum space needed for the queue.</p>

<br>
<br>

<h1>Balenced Binary Tree</h1>
<p> Given a Binary Tree, return true if it is a Balanced Binary Tree else return false. A Binary Tree is balanced if, for all nodes in the tree, the difference between left and right subtree height is not more than 1.</p>
<p><strong>Examples</strong></p>
<img src="https://static.takeuforward.org/content/balanced-tree-image1-EWX-8Niv">
<p><strong>Input :</strong>Binary Tree: 3 9 20 -1 -1 15 7</p>
<p><strong>Output :</strong>True, This is a Balanced Binary Tree</p>
<img src="https://static.takeuforward.org/content/balanced-tree-image2-46UA3Wf3">
<p><strong>Explanation :</strong>The difference in the height of left and right subtree is 1 hence the tree is balanced.</p>

<img src="https://static.takeuforward.org/content/balanced-tree-image3-Fjdfx1vW">
<p><strong>Input :</strong>Binary Tree: 1 3 2 5 4 -1 -1 7 6 </p>
<p><strong>Output :</strong>False, this is not a Balanced Binary Tree.</p>
<img src="https://static.takeuforward.org/content/balanced-tree-image4-srgyTlGy">
<p><strong>Explanation :</strong>The difference in the height of left and right subtree is 2 hence the tree is not balanced.</p>


<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>BruteForce Approach : </strong></p>
<p>The brute force approach for checking if a binary tree is balanced involves the following steps:</p>
<ul>
    <li><strong>Understanding Tree Height:</strong>
        <ul>
            <li>The height of a tree is the number of edges on the longest path from the root to a leaf.</li>
            <li>To find the height of a node, you need to know the height of its left and right subtrees.</li>
        </ul>
    </li>
    <li><strong>Balanced Tree Definition:</strong>
        <ul>
            <li>A tree is balanced if, for every node, the difference in height between its left and right subtrees is at most 1.</li>
        </ul>
    </li>
    <li><strong>Brute Force Approach:</strong>
        <ol>
            <li><strong>Calculate the Height of the Left Subtree:</strong>
                <ul>
                    <li>Recursively find the height of the left child node.</li>
                </ul>
            </li>
            <li><strong>Calculate the Height of the Right Subtree:</strong>
                <ul>
                    <li>Recursively find the height of the right child node.</li>
                </ul>
            </li>
            <li><strong>Check the Balance Condition:</strong>
                <ul>
                    <li>Compute the difference in heights between the left and right subtrees.</li>
                    <li>If the difference is more than 1, the tree is not balanced.</li>
                </ul>
            </li>
            <li><strong>Check Subtree Balance:</strong>
                <ul>
                    <li>Recursively ensure that both the left and right subtrees are also balanced.</li>
                </ul>
            </li>
        </ol>
    </li>
</ul>
<img src="https://static.takeuforward.org/content/balanced-tree-image6-0sxtQE1r">


```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findHeight(node):
    if not node:
        return 0
    leftHeight = findHeight(node.left)
    rightHeight = findHeight(node.right)
    return 1 + max(leftHeight, rightHeight)

def isBalanced(node):
    if not node:
        return True
    leftHeight = findHeight(node.left)
    rightHeight = findHeight(node.right)
    diff = abs(leftHeight - rightHeight)
    if diff <= 1 and isBalanced(node.left) and isBalanced(node.right):
        return True
    return False

# Example usage:
# Construct a sample tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Check if the tree is balanced
print(isBalanced(root))  # Output: True

```

<p><strong>Time Complexity :</strong>O(n^2), because the height function is called multiple times for each node.</p>
<p><strong>Space Complexity :</strong>O(n) ,in the worst case due to the recursion stack, which can grow to the height of the tree.</p>

<br>

<p><strong>Optimized Approach</strong></p>
<h1>Intuition Behind the Optimized Approach</h1>

<p><strong>Understanding Balance:</strong></p>
<ul>
    <li>A binary tree is balanced if, for every node, the height difference between its left and right subtrees is at most 1.</li>
</ul>

<p><strong>Combining Tasks:</strong></p>
<ul>
    <li>Instead of separately calculating the height of the tree and then checking if it’s balanced, you can do both in one go. This avoids recalculating heights multiple times.</li>
</ul>

<p><strong>Single Pass Calculation:</strong></p>
<ul>
    <li>The idea is to use a single function that:
        <ol>
            <li><strong>Calculates the Height</strong> of each subtree.</li>
            <li><strong>Checks if the Tree is Balanced</strong> at the same time.</li>
        </ol>
    </li>
</ul>

<p><strong>Early Exit for Unbalanced Trees:</strong></p>
<ul>
    <li>If at any point, the function detects that a subtree is unbalanced (by returning -1), it immediately stops further calculations. This is efficient because you don’t waste time checking other parts of the tree if you already know it’s not balanced.</li>
</ul>

<p><strong>How It Works:</strong></p>
<ul>
    <li><strong>Starting from the Root:</strong>
      <ul>
          <li>Begin at the root of the tree.</li>
      </ul>
    </li>
    <li><strong>Recursive Calculation:</strong>
    <ul>
        <li>For each node:
            <ol>
                <li><strong>Calculate Heights of Subtrees:</strong> Recursively find the height of the left and right subtrees.</li>
                    <li><strong>Check Balance:</strong> Compare the heights of the left and right subtrees. If the difference is more than 1, return -1 to indicate the tree is unbalanced.</li>
                </ol>
            </li>
        </ul>
    </li>
    <li><strong>Return Height if Balanced:</strong>
        <ul>
            <li>If the node and its subtrees are balanced, return the height of the node’s subtree.</li>
        </ul>
    </li>
</ul>

<p><strong>Example:</strong></p>
<p>Consider a tree:</p>
<pre>
   1
  / \
 2   3
/ \
4   5
</pre>

<ul>
    <li><strong>At Node 1:</strong>
        <ul>
            <li>Calculate height of left subtree (rooted at 2).</li>
            <li>Calculate height of right subtree (rooted at 3).</li>
            <li>Check the balance condition.</li>
            <li>Combine results and return the height.</li>
        </ul>
    </li>
    <li><strong>At Node 2:</strong>
        <ul>
            <li>Calculate height of left subtree (rooted at 4).</li>
            <li>Calculate height of right subtree (rooted at 5).</li>
            <li>Check balance.</li>
        </ul>
    </li>
    <li><strong>At Nodes 4 and 5:</strong>
        <ul>
            <li>They are leaf nodes, so their heights are straightforward.</li>
        </ul>
    </li>
</ul>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Height(node):
    # Base case: empty tree
    if not node:
        return 0
    
    # Get height of left subtree
    leftHeight = Height(node.left)
    if leftHeight == -1:
        return -1  # Left subtree is not balanced
    
    # Get height of right subtree
    rightHeight = Height(node.right)
    if rightHeight == -1:
        return -1  # Right subtree is not balanced
    
    # Check if current node is balanced
    if abs(leftHeight - rightHeight) > 1:
        return -1  # Current tree is not balanced
    
    # Return height of current tree
    return 1 + max(leftHeight, rightHeight)

def optimized(node):
    return Height(node) != -1

# Example usage:
# Construct a sample tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Check if the tree is balanced
print(optimized(root))  # Output: True

```

<p><strong>Time Complexity :</strong>O(n), atmost we will visit each node at once</p>
<p><strong>Space Complexity :</strong>O(n), recursion call stack will store maximum of given nodes</p>

<br>
<br>

<h1>Diameter / Width Of A Tree</h1>
<p>Given the root of the Binary Tree, return the length of its diameter. The Diameter of a Binary Tree is the longest distance between any two nodes of that tree. This path may or may not pass through the root.</p>
<p><strong>Examples</strong></p>
<img src="https://static.takeuforward.org/content/diameter-tree-image1-rfCH6MsT">
<p><strong>Input :</strong></p>
<p><strong>Output :</strong>4</p>
<img src="https://static.takeuforward.org/content/diameter-tree-image2-eZz0n4yE">
<p><strong>Explanation :</strong>The distance between the leftmost node 4 and the rightmost node 3 is 4, since this is the longest horizontal distance of the binary tree, hence its diameter.</p>

<p><strong>Input : </strong></p>
<img src="https://static.takeuforward.org/content/diameter-tree-image3-UlLQBXcW">
<p><strong>Output : </strong>7</p>
<p><strong>Explanation : </strong>The distance between the leftmost node 4 and the rightmost node 3 is 4, since this is the longest horizontal distance of the binary tree, hence its diameter.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>Bruteforce Approach : </strong></p>

<p><strong>Understanding Diameter:</strong></p>
<ul>
    <li>The diameter of a binary tree is the longest path between any two nodes.</li>
    <li>This path can pass through the root, be entirely in the left subtree, or be entirely in the right subtree.</li>
</ul>

<p><strong>Breaking Down the Problem:</strong></p>
<ul>
    <li>For each node, the diameter can be calculated as the sum of the heights of its left and right subtrees.</li>
    <li>We need to compare this diameter with the diameters of the left and right subtrees.</li>
</ul>

<p><strong>Recursive Calculation:</strong></p>
<ul>
    <li>For each node:
        <ol>
            <li>Calculate the height of the left subtree.</li>
            <li>Calculate the height of the right subtree.</li>
            <li>The potential diameter at this node is the sum of these two heights.</li>
            <li>Recursively find the diameters of the left and right subtrees.</li>
            <li>The diameter of the tree rooted at this node is the maximum of these three values.</li>
        </ol>
    </li>
</ul>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findHeight(node):
    # Base case: if the node is null, the height is 0
    if not node:
        return 0
    # Recursively find the height of the left subtree
    leftHeight = findHeight(node.left)
    # Recursively find the height of the right subtree
    rightHeight = findHeight(node.right)
    # The height of the current node is 1 + the maximum of the heights of the left and right subtrees
    return 1 + max(leftHeight, rightHeight)

def bruteForce(node):
    # Base case: if the node is null, the diameter is 0
    if not node:
        return 0
    # Calculate the height of the left subtree
    leftHeight = findHeight(node.left)
    # Calculate the height of the right subtree
    rightHeight = findHeight(node.right)
    # The potential diameter at the current node is the sum of the heights of the left and right subtrees
    currentDiameter = leftHeight + rightHeight
    # Recursively find the diameter of the left subtree
    leftDiameter = bruteForce(node.left)
    # Recursively find the diameter of the right subtree
    rightDiameter = bruteForce(node.right)
    # The diameter of the tree rooted at the current node is the maximum of the current diameter, left diameter, and right diameter
    return max(currentDiameter, leftDiameter, rightDiameter)

# Example usage:
# Construct a sample tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Find the diameter of the tree
print(bruteForce(root))  # Output: 3

```


<p><strong>Time Complexity :</strong>O(n^2), because the height function is called multiple times for each node.</p>
<p><strong>Space Complexity :</strong>O(n) ,in the worst case due to the recursion stack, which can grow to the height of the tree.</p>

<br>

<p><strong>Optimized Approach</strong></p>
<p><strong>Understanding Diameter:</strong></p>
<ul>
    <li>The diameter of a binary tree is the longest path between any two nodes.</li>
    <li>This path can pass through the root, be entirely in the left subtree, or be entirely in the right subtree.</li>
</ul>

<p><strong>Combining Tasks:</strong></p>
<ul>
    <li>Instead of calculating the height of the tree and then separately checking for the diameter, the optimized approach combines these tasks.</li>
    <li>This avoids recalculating heights multiple times, making the solution more efficient.</li>
</ul>

<p><strong>Single Pass Calculation:</strong></p>
<ul>
    <li>The idea is to use a single function that:
        <ol>
            <li>Calculates the height of each subtree.</li>
            <li>Updates the diameter at each node based on the heights of the left and right subtrees.</li>
        </ol>
    </li>
</ul>

<p><strong>How It Works:</strong></p>
<ul>
    <li><strong>Starting from the Root:</strong>
        <ul>
            <li>Begin at the root of the tree.</li>
        </ul>
    </li>
    <li><strong>Recursive Calculation:</strong>
        <ul>
            <li>For each node:
                <ol>
                    <li>Calculate the height of the left subtree.</li>
                    <li>Calculate the height of the right subtree.</li>
                    <li>Update the diameter using the sum of the heights of the left and right subtrees.</li>
                    <li>Return the height of the node's subtree.</li>
                </ol>
            </li>
        </ul>
    </li>
</ul>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Height(node, diameter):
    # Base case: if the node is null, the height is 0
    if not node:
        return 0
    # Recursively find the height of the left subtree
    leftHeight = Height(node.left, diameter)
    # Recursively find the height of the right subtree
    rightHeight = Height(node.right, diameter)
    # Update the diameter with the sum of the heights of the left and right subtrees
    diameter[0] = max(diameter[0], leftHeight + rightHeight)
    # The height of the current node is 1 + the maximum of the heights of the left and right subtrees
    return 1 + max(leftHeight, rightHeight)

def optimized(node):
    # Initialize diameter as a list to store the maximum diameter
    diameter = [0]
    # Call the helper function to calculate the height and update the diameter
    Height(node, diameter)
    # Return the diameter
    return diameter[0]

# Example usage:
# Construct a sample tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Find the diameter of the tree
print(optimized(root))  # Output: 3

```

<p><strong>Time Complexity :</strong>O(n), atmost we will visit each node at once</p>
<p><strong>Space Complexity :</strong>O(n), recursion call stack will store maximum of given nodes</p>

<br>
<br>

<h1>Max Path Sum</h1>
<p>Given a Binary Tree, determine the maximum sum achievable along any path within the tree. A path in a binary tree is defined as a sequence of nodes where each pair of adjacent nodes is connected by an edge. Nodes can only appear once in the sequence, and the path is not required to start from the root. Identify and compute the maximum sum possible along any path within the given binary tree.</p>
<p><strong>Examples</strong></p>
<p><strong>Input : </strong>Binary Tree: -10 9 20 -1 -1 15 7</p>
<img src="https://static.takeuforward.org/content/Maximum-path-sum-image1-28CrKnMo">
<p><strong>Output : </strong>42</p>
<img src="https://static.takeuforward.org/content/Maximum-path-sum-image2-YUVqI9Hq">
<p><strong>Explanation : </strong>Out of all the paths possible in the Binary Tree, 15 -> 20 -> 7 has the greatest sum ie. 42.
</p>

<p><strong>Input : </strong>Binary Tree: -2 2 1</p>
<img src="https://static.takeuforward.org/content/Maximum-path-sum-image3-BUE4Y-7t">
<p><strong>Output : </strong>2</p>
<img src="https://static.takeuforward.org/content/Maximum-path-sum-image4-d9m4rdz8">
<p><strong>Explanation : </strong>Out of all the paths possible in the Binary Tree, a path starting and ending at the node with value 2 has the greatest sum ie. 2.
</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>Optimized Approach</strong></p>
<p><strong>Understanding Maximum Path Sum:</strong></p>
<ul>
    <li>The path can start and end at any node in the tree.</li>
    <li>It can traverse both left and right subtrees, but it cannot return back to the parent node (i.e., it forms a "V" shape).</li>
</ul>

<p><strong>Breaking Down the Problem:</strong></p>
<ul>
    <li>For each node, calculate the maximum path sum that passes through the node.</li>
    <li>Compare it with the maximum path sums of its left and right subtrees to update the global maximum path sum.</li>
</ul>

<p><strong>Recursive Calculation:</strong></p>
<ul>
    <li>For each node:
        <ol>
            <li>Calculate the maximum path sum of the left subtree (ignore negative sums as they reduce the overall sum).</li>
            <li>Calculate the maximum path sum of the right subtree (ignore negative sums as they reduce the overall sum).</li>
            <li>Update the global maximum path sum using the current node's value and the maximum sums of its left and right subtrees.</li>
            <li>Return the maximum path sum where the current node is the end point, so it can be used in its parent node's path sum calculation.</li>
        </ol>
    </li>
</ul>

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxSum(node, maxi):
    # Base case: if the node is null, return 0
    if not node:
        return 0
    
    # Recursively find the maximum path sum of the left subtree
    # Only consider positive sums to maximize the path sum
    leftSum = max(0, maxSum(node.left, maxi))
    
    # Recursively find the maximum path sum of the right subtree
    # Only consider positive sums to maximize the path sum
    rightSum = max(0, maxSum(node.right, maxi))
    
    # Update the global maximum path sum
    maxi[0] = max(maxi[0], leftSum + rightSum + node.data)
    
    # Return the maximum path sum where the current node is the end point
    return node.data + max(leftSum, rightSum)

# Example usage:
# Construct a sample tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Find the maximum path sum
maxi = [float('-inf')]
print(maxSum(root, maxi))  # Output: 11
print(maxi[0])  # Output: 15
```
<p><strong>Time Complexity :</strong>O(n), atmost we will visit each node at once</p>
<p><strong>Space Complexity :</strong>O(n), recursion call stack will store maximum of given nodes</p>

<br>
<br>

<h1>Max Sum Path from Root to Leaf Node</h1>

<p><strong>Problem Statement:</strong></p>
<p>Find the maximum path sum from the root to any leaf node in a binary tree. A path is defined as a sequence of nodes starting from the root and ending at any leaf node, where each node is connected to its child nodes.</p>

<p><strong>Example Test Cases:</strong></p>
<ol>
    <li>
        <strong>Example 1:</strong>
        <p>Tree:</p>
        <pre>
<code>
    10
   /  \
  2    10
 / \      \
20  1     -25
           /  \
          3    4
</code>
            </pre>
            <p>Maximum Path Sum: 10 → 2 → 20 = 32</p>
        </li>
        <li>
            <strong>Example 2:</strong>
            <p>Tree:</p>
            <pre>
<code>
    -15
   /   \
  5    6
 / \    \
-8  1    3
         / \
        7   4
</code>
            </pre>
            <p>Maximum Path Sum: -15 → 6 → 3 → 7 = 1</p>
        </li>
    </ol>

<p><strong>Intuition in Simple Words:</strong></p>
<ul>
    <li><strong>Starting Point:</strong> Begin from the root node.</li>
    <li><strong>Path to Leaf:</strong> For each node, find the maximum sum path from that node to any leaf node.</li>
    <li><strong>Recursive Calculation:</strong> For each node:
        <ul>
            <li>Compute the maximum path sum for its left and right subtrees.</li>
            <li>Add the node's value to the maximum of the sums from its left or right subtree.</li>
        </ul>
    </li>
    <li><strong>Return the Best Sum:</strong> For the root node, this gives the maximum path sum from the root to any leaf.</li>
</ul>

<p><strong>Program:</strong></p>
<pre>

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxSumPath(root):
    # Base case: If the tree is empty
    if root is None:
        return 0

    # Recursive function to find the maximum path sum from root to leaf
    def maxPathSum(node):
        # Base case: If the node is a leaf node
        if node.left is None and node.right is None:
            return node.data

        # Initialize left and right maximum sums
        leftSum = float('-inf')
        rightSum = float('-inf')

        # Recursively calculate maximum sums from left and right subtrees
        if node.left is not None:
            leftSum = maxPathSum(node.left)
        if node.right is not None:
            rightSum = maxPathSum(node.right)

        # Return the maximum path sum from root to leaf
        return node.data + max(leftSum, rightSum)

    # Call the recursive function and return the result
    return maxPathSum(root)

# Example usage:
# Constructing the example tree:
#       10
#      /  \
#     2    10
#    / \      \
#   20  1     -25
#              /  \
#             3    4

root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

# Find the maximum path sum from root to any leaf
print(maxSumPath(root))  # Output: 32
```

    </pre>

<p><strong>Explanation:</strong></p>
<ul>
  <li><strong>Class Definition:</strong> Define a <code>Node</code> class for tree nodes.</li>
  <li><strong>Recursive Function:</strong> The <code>maxPathSum</code> function calculates the maximum path sum from the current node to any leaf node.
      <ul>
          <li><strong>Base Case:</strong> If the node is a leaf, return its value.</li>
          <li><strong>Recursive Case:</strong> Compute maximum sums for left and right subtrees, and add the node's value to the maximum of these sums.</li>
      </ul>
  </li>
  <li><strong>Example Tree:</strong> An example tree is constructed, and the <code>maxSumPath</code> function is called to find the maximum path sum.</li>
</ul>

<p><strong>Time Complexity :</strong>O(n), atmost we will visit each node at once</p>
<p><strong>Space Complexity :</strong>O(n), recursion call stack will store maximum of given nodes</p>