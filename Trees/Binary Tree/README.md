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


<h1>Check Two Tree Are Identical Or Not</h1>
<p>Given the roots of two binary trees, write a function to check if they are identical. Two binary trees are considered identical if they have the same structure and every corresponding node has the same value.</p>
<p><strong>Examples</strong></p>
<p><strong>Input : </strong>p = [1,2,3], q = [1,2,3]</p>
<img src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg">
<p><strong>Output :</strong>True</p>
<p><strong>Input : </strong>p = [1,2], q = [1,null,2]</p>
<img src="https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg">
<p><strong>Output :</strong>False</p>

<br>

<p><strong>Solution</strong></p>
<p>This solution checks if two binary trees are identical by comparing their structure and values in a recursive manner. The function returns True if both trees are identical and False otherwise.</p>
<p>We want to check if two binary trees are identical, meaning they have the same structure and values.</p>
<p><strong>Steps</strong></p>
<ol>
  <li><strong>Base Case: Both Nodes are None</strong>
    <ul>
      <li>If both nodes (<code>node1</code> and <code>node2</code>) are <code>None</code>, it means we've reached the end of both trees at the same time. Since both are empty at this point, they are identical. Return <code>True</code>.</li>
    </ul>
  </li>
  
  <li><strong>Base Case: One Node is None, the Other is Not</strong>
    <ul>
      <li>If one node is <code>None</code> and the other is not, it means the trees are not identical at this point because one tree has a node where the other does not. Return <code>False</code>.</li>
    </ul>
  </li>
  
  <li><strong>Compare Current Nodes' Values</strong>
    <ul>
      <li>If both nodes are not <code>None</code>, compare their values (<code>node1.data</code> and <code>node2.data</code>). If the values are different, return <code>False</code>.</li>
    </ul>
  </li>
  
  <li><strong>Recursive Comparison of Subtrees</strong>
    <ul>
      <li>Recursively compare the left children of both nodes (<code>node1.left</code> and <code>node2.left</code>).</li>
      <li>Recursively compare the right children of both nodes (<code>node1.right</code> and <code>node2.right</code>).</li>
    </ul>
  </li>
  
  <li><strong>Combine Results</strong>
    <ul>
      <li>The current nodes are identical if:
        <ul>
          <li>Their values are the same.</li>
          <li>Their left subtrees are identical.</li>
          <li>Their right subtrees are identical.</li>
        </ul>
      </li>
      <li>Return <code>True</code> if all three conditions are satisfied.</li>
    </ul>
  </li>
</ol>

<p><strong>Visual Breakdown</strong></p>

<p>Let's visualize the comparison process step-by-step for two identical trees:</p>

<pre>
Tree 1:        1
             /   \
            2     3

Tree 2:        1
             /   \
            2     3
</pre>

<ol>
  <li>Compare root nodes <code>1</code> and <code>1</code>: Values are the same.</li>
  <li>Recursively compare left children <code>2</code> and <code>2</code>:
    <ul>
      <li>Values are the same.</li>
      <li>Both left and right children of <code>2</code> are <code>None</code> in both trees.</li>
    </ul>
  </li>
  <li>Recursively compare right children <code>3</code> and <code>3</code>:
    <ul>
      <li>Values are the same.</li>
      <li>Both left and right children of <code>3</code> are <code>None</code> in both trees.</li>
    </ul>
  </li>
  <li>Since all comparisons returned <code>True</code>, the trees are identical.</li>
</ol>

```python
def optimized(node1,node2):
    if(node1==None and node2==None):
        return True
    if((node1==None and node2!=None) or (node1!=None and node2==None)):
        return False
    a=(node1.data==node2.data)
    b=optimized(node1.left,node2.left)
    c=optimized(node1.right,node2.right)
    return a and b and c

root1=Node(4)
root1.left=Node(2)
root1.right=Node(5)
root2=Node(4)
root2.left=Node(2)
root2.right=Node(5)
print(optimized(root1,root2))
root2.right=Node(10)
print(optimized(root1,root2))
```

<p><strong>Time Complexity : </strong>O(n), where n is the number of nodes in the trees, because each node is visited once.</p>
<p><strong>Space Complexity : </strong>𝑂(h) is the height of the trees, due to the recursion stack used in the depth-first traversal.</p>


<br>
<br>

<h1>Zig Zag Traversal</h1>
<p>Given a Binary Tree, print the zigzag traversal of the Binary Tree. Zigzag traversal of a binary tree is a way of visiting the nodes of the tree in a zigzag pattern, alternating between left-to-right and right-to-left at each level.</p>
<p><strong>Examples</strong></p>
<p><strong>Input : </strong>Binary Tree: 1 2 3 4 5 -1 6</p>
<img src="https://static.takeuforward.org/content/zig-zag-image1-fkiEDFoN">
<p><strong>Output : </strong>[[1],[3, 2],[4, 5, 6]]</p>
<p><strong>Explantaion</strong></p>
<img src="https://static.takeuforward.org/content/zig-zag-image2-ATavNI7k">
<ul>
  <li>Level 1 (Root): Visit the root node 1 from left to right. Zigzag Traversal: [1]</li>
  <li>Level 2: Visit nodes at this level in a right-to-left order. Zigzag Traversal:  [1], [3, 2]</li>
  <li>Level 3: Visit nodes at this level in a left-to-right order. Zigzag Traversal:  [1], [3, 2], [4, 5, 6]</li>
</ul>

<p><strong>Input : </strong>Binary Tree: 1 2 -1 4 5 -1 -1 7 8</p>
<img src="https://static.takeuforward.org/content/zig-zag-image3-hqVEj8-y">
<p><strong>Output : </strong>[[1], [2], [4, 5], [8, 7]]</p>
<p><strong>Explantaion</strong></p>
<img src="https://static.takeuforward.org/content/zig-zag-image4-B908-MAE">
<ul>
  <li>Level 1 (Root): Visit the root node 1 from left to right. Zigzag Traversal: [1]</li>
  <li>Level 2: Visit nodes at this level in a right-to-left order. Zigzag Traversal:  [1], [2]</li>
  <li>Level 3: Visit nodes at this level in a left-to-right order. Zigzag Traversal:  [1], [3, 2], [4, 5]</li>
  <li>Level 4: Visit nodes at this level in a right-to-left order. Zigzag Traversal:  [1], [3, 2], [4, 5], [8, 7]</li>
</ul>

<br>

<p><strong>Solution</strong></p>
<p>In this solution, basically we will find level order traversal, for each alternating level we are trying to store nodes in reverse order</p>
<p><strong>Steps</strong></p>
<ol>
  <li><strong>Initialization:</strong>
    <ul>
      <li>Create an empty list <code>ans</code> to store the final result.</li>
      <li>If the input <code>node</code> is <code>None</code>, return an empty list.</li>
      <li>Initialize a <code>deque</code> called <code>queue</code> and add the root node to it.</li>
      <li>Set a boolean variable <code>reverse</code> to <code>False</code>, indicating the order of node values on the current level.</li>
    </ul>
  </li>

  <li><strong>Level-order Traversal:</strong>
    <ul>
      <li>While there are nodes in the <code>queue</code>, perform the following steps:
        <ul>
          <li>Determine the number of nodes at the current level (<code>n</code>).</li>
          <li>Create a list <code>level</code> with <code>n</code> zeros to store node values for this level.</li>
          <li>For each node at this level:
            <ul>
              <li>Dequeue a node.</li>
              <li>Determine the position to place this node's value in the <code>level</code> list. If <code>reverse</code> is <code>True</code>, place it from the end; otherwise, place it from the start.</li>
              <li>Add the node’s left and right children to the <code>queue</code> if they exist.</li>
            </ul>
          </li>
          <li>Append the <code>level</code> list to the <code>ans</code> list.</li>
          <li>Toggle the <code>reverse</code> boolean to switch the order for the next level.</li>
        </ul>
      </li>
    </ul>
  </li>

  <li><strong>Return Result:</strong>
    <ul>
      <li>Return the <code>ans</code> list, which contains node values in zigzag level-order.</li>
    </ul>
  </li>
</ol>

<p><strong>Code</strong></p>

```python
from collections import deque

def solve(node):
    ans = []  # List to store the result
    if not node:  # If the tree is empty
        return []
    
    queue = deque()
    queue.append(node)
    reverse = False  # Flag to alternate between left-to-right and right-to-left
    
    while queue:
        n = len(queue)  # Number of nodes at the current level
        level = [0] * n  # Initialize a list to store node values for this level
        
        for i in range(n):
            temp = queue.popleft()
            pos = (n - i - 1) if reverse else i  # Determine position based on direction
            level[pos] = temp.data
            
            if temp.left:  # Add left child to queue
                queue.append(temp.left)
            if temp.right:  # Add right child to queue
                queue.append(temp.right)
        
        ans.append(level)  # Append the current level to the result
        reverse = not reverse  # Toggle the direction for the next level
    
    return ans

```

<p><strong>Time and Space Complexity</strong></p>

<ul>
  <li><strong>Time Complexity:</strong> <code>O(n)</code>, where <code>n</code> is the number of nodes in the tree. Each node is processed exactly once.</li>
  <li><strong>Space Complexity:</strong> <code>O(w)</code>, where <code>w</code> is the maximum width of the tree (i.e., the maximum number of nodes at any level). This space is used by the <code>deque</code> and the <code>level</code> list.</li>
</ul>


<h1>Boundary Traversal</h1>
<p> Given a Binary Tree, perform the boundary traversal of the tree. The boundary traversal is the process of visiting the boundary nodes of the binary tree in the anticlockwise direction, starting from the root.</p>
<p><strong>Examples</strong></p>
<p><strong>Input : </strong>Binary Tree: 1 2 7 3 -1 -1 8 -1 4 9 -1 5 6 10 11</p>
<img src="https://static.takeuforward.org/content/boundary-traversal-image1-XAwduImr">
<p><strong>Output : </strong>Boundary Traversal: [1, 2, 3, 4, 5, 6, 10, 11, 9, 8, 7]</p>
<p><strong>Explanation : </strong></p>
<img src="https://static.takeuforward.org/content/boundary-traversal-image2-1EFr7OIC">
<p>The boundary traversal of a binary tree involves visiting its boundary nodes in an anticlockwise direction:</p>
<ul>
  <li>Starting from the root, we traverse from: 1</li>
  <li>The left side traversal includes the nodes: 2, 3, 4</li>
  <li>The bottom traversal include the leaf nodes: 5, 6, 10, 11</li>
  <li>The right side traversal includes the nodes: 9, 8, 7</li>
  <li>We return to the  root and the boundary traversal is complete.</li>
</ul>
<br>
<p><strong>Input : </strong>Binary Tree: 10 5 20 3 8 18 25 -1 7 -1 -1</p>
<img src="Binary Tree: 10 5 20 3 8 18 25 -1 7 -1 -1">
<p><strong>Output : </strong>Boundary Traversal: [10, 5, 3, 7, 8, 18, 25, 20]</p>
<p><strong>Explanation : </strong></p>
<img src="https://static.takeuforward.org/content/boundary-traversal-image4-4QJ8Okw7">
<p>The boundary traversal of a binary tree involves visiting its boundary nodes in an anticlockwise direction:</p>
<ul>
  <li>Starting from the root, we traverse from: 10</li>
  <li>The left side traversal includes the nodes: 5</li>
  <li>The bottom traversal include the leaf nodes: 3, 7, 8, 18, 25</li>
  <li>The right side traversal includes the nodes: 20</li>
  <li>We return to the  root and the boundary traversal is complete.</li>
</ul>

<br>

<p><strong>Solution</strong></p>
<p><strong>Intuition Behind Boundary Traversal</strong></p>

<p>We want to collect the nodes that form the outer boundary of the binary tree. This includes:</p>
<ul>
  <li>The left boundary (excluding leaf nodes)</li>
  <li>All the leaf nodes</li>
  <li>The right boundary (excluding leaf nodes)</li>
</ul>

<p><strong>Steps to Collect Boundary Nodes:</strong></p>

<ol>
  <li><strong>Add Root Node:</strong>
    <ul>
      <li>Start with the root node. If it’s not a leaf, add its value to the list. This is the starting point of our boundary.</li>
    </ul>
  </li>

  <li><strong>Add Left Boundary:</strong>
    <ul>
      <li>Move down the left side of the tree, adding nodes to the boundary list.</li>
      <li>Skip leaf nodes because they are added separately.</li>
      <li>Continue this until you reach the end of the left boundary (either a leaf node or a node with no left child).</li>
    </ul>
  </li>

  <li><strong>Add Leaf Nodes:</strong>
    <ul>
      <li>Use pre-order traversal to visit all leaf nodes (nodes with no children).</li>
      <li>Add these leaf nodes to the boundary list.</li>
    </ul>
  </li>

  <li><strong>Add Right Boundary:</strong>
    <ul>
      <li>Move down the right side of the tree, similar to the left boundary, but this time collect nodes in reverse order (using a stack).</li>
      <li>Skip leaf nodes as they are already included in the previous step.</li>
      <li>After traversing the right boundary, reverse the collected nodes and add them to the boundary list.</li>
    </ul>
  </li>
</ol>

<p><strong>Summary:</strong></p>
<ul>
  <li><strong>Start:</strong> Add the root node if it’s not a leaf.</li>
  <li><strong>Left Boundary:</strong> Traverse and add non-leaf nodes on the left side.</li>
  <li><strong>Leaf Nodes:</strong> Collect all leaf nodes.</li>
  <li><strong>Right Boundary:</strong> Traverse and collect non-leaf nodes on the right side in reverse order.</li>
</ul>

<p>This approach ensures that all boundary nodes are collected in the correct order and avoids duplicates.</p>

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isLeaf(node):
    return node.left==None and node.right==None

def addLeftBoundary(node,ans):
    current=node.left
    while current:
        if(not isLeaf(current)):
            ans.append(current.data)
        if(current.left):
            current=current.left
        else:
            current=current.right

def addRightBoundary(node,ans):
    current=node.right
    stack=[]
    while current:
        if(not isLeaf(current)):
            stack.append(current.data)
        if(current.right):
            current=current.right
        else:
            current=current.left
    while stack:
        ans.append(stack.pop())

def preOrder(node,ans):
    if(not node):
        return
    if(isLeaf(node)):
        ans.append(node.data)
    preOrder(node.left,ans)
    preOrder(node.right,ans)

def solve(node):
    ans=[]
    if(not node):
        return ans
    if(not isLeaf(node)):
        ans.append(node.data)
    addLeftBoundary(node,ans)
    preOrder(node,ans)
    addRightBoundary(node,ans)
    return ans
            

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

<p><strong>1. <code>isLeaf(node)</code></strong></p>
<p><strong>Purpose:</strong> Determine if a node is a leaf node (a node with no children).</p>
<p><strong>Intuition:</strong></p>
<ul>
  <li>A leaf node is a node that does not have left or right children.</li>
  <li>If both <code>node.left</code> and <code>node.right</code> are <code>None</code>, the node is a leaf.</li>
  <li>This function helps in identifying which nodes are leaves and should be treated differently (e.g., not added to boundaries but included in the leaf nodes list).</li>
</ul>

<p><strong>2. <code>addLeftBoundary(node, ans)</code></strong></p>
<p><strong>Purpose:</strong> Add all non-leaf nodes along the left boundary of the tree to the <code>ans</code> list.</p>
<p><strong>Intuition:</strong></p>
<ul>
  <li>Start from the left child of the root and move down the left side of the tree.</li>
  <li>Add each node's value to the list if it is not a leaf. This ensures that only the boundary nodes are included.</li>
  <li>If a node has a left child, continue moving left. If not, move to the right child (if it exists) to cover nodes that might be at the boundary.</li>
  <li>This function helps in collecting the leftmost boundary nodes of the tree.</li>
</ul>

<p><strong>3. <code>addRightBoundary(node, ans)</code></strong></p>
<p><strong>Purpose:</strong> Add all non-leaf nodes along the right boundary of the tree to the <code>ans</code> list in reverse order.</p>
<p><strong>Intuition:</strong></p>
<ul>
  <li>Start from the right child of the root and move down the right side of the tree.</li>
  <li>Use a stack to reverse the order of nodes collected during traversal, since the right boundary nodes need to be added in reverse order to match the boundary traversal order.</li>
  <li>If a node has a right child, continue moving right. If not, move to the left child (if it exists).</li>
  <li>This function helps in collecting the rightmost boundary nodes and ensuring they are added in the correct order.</li>
</ul>

<p><strong>4. <code>preOrder(node, ans)</code></strong></p>
<p><strong>Purpose:</strong> Add all leaf nodes to the <code>ans</code> list using pre-order traversal.</p>
<p><strong>Intuition:</strong></p>
<ul>
  <li>Pre-order traversal visits nodes in the order: root, left, right. This traversal is useful for visiting all nodes in a subtree.</li>
  <li>If a node is a leaf (no children), its value is added to the list.</li>
  <li>Recursively visit the left and right children to ensure all leaves in the tree are included.</li>
  <li>This function helps in collecting all leaf nodes, which are a part of the boundary but not included in the left or right boundaries.</li>
</ul>

<p><strong>5. <code>solve(node)</code></strong></p>
<p><strong>Purpose:</strong> Combine all parts to collect boundary nodes of the binary tree.</p>
<p><strong>Intuition:</strong></p>
<ul>
  <li>Start by adding the root node (if it’s not a leaf) to the boundary list.</li>
  <li>Add the left boundary nodes by traversing the left side of the tree.</li>
  <li>Collect all leaf nodes using pre-order traversal.</li>
  <li>Add the right boundary nodes in reverse order using a stack.</li>
  <li>This function orchestrates the process of boundary collection by calling the helper functions and combining their results.</li>
</ul>

<p><strong>Time Complexity:</strong> O(N) – Each node in the binary tree is visited once during traversal.</p>
<p><strong>Space Complexity:</strong> O(H) – Space is required for the height of the tree due to recursive calls and stack storage.</p>


<br>
<br>


<h1>Vertical Order Traversal</h1>
<p>Given a Binary Tree, return the Vertical Order Traversal of it starting from the Leftmost level to the Rightmost level. If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree</p>
<p><strong>Examples</strong></p>
<p><strong>Input :Binary Tree: 1 2 3 4 10 9 11 -1 5 -1 -1 -1 -1 -1 -1 -1 6</strong></p>
<img src="https://static.takeuforward.org/content/vertical-traversal-image1-diChK2E3">
<p><strong>Output :Vertical Order Traversal: [[4],[2, 5], [1, 10, 9, 6],[3],[11]]</strong></p>
<p><strong>Explanation :</strong></p>
<img src="https://static.takeuforward.org/content/vertical-traversal-image2-L8jBykS-">
<p>Vertical Levels from left to right:</p>
<ul>
  <li>Level -2: [4]</li>
  <li>Level -1: [2]</li>
  <li>Level 0: [1, 10, 9, 6] (Overlapping nodes are added in their level order sequence)</li>
  <li>Level 1: [3]</li>
  <li>Level 2: [11]</li>
</ul>
<br>
<p><strong>Input : Binary Tree: 2 7 5 2 6 -1 9 -1 -1 5 11 4 -1</strong></p>
<img src="https://static.takeuforward.org/content/vertical-traversal-image3-t3_XyQdZ">
<p><strong>Output :</strong>[[2],[7, 5],[2, 6], [5, 11, 4],[9]]</p>
<p><strong>Explanation :</strong></p>
<img src="https://static.takeuforward.org/content/vertical-traversal-image4-aWuNOE3V">
<p>Vertical Levels from left to right:</p>
<ul>
  <li>Level -2: [2]</li>
  <li>Level -1: [7, 5]</li>
  <li>Level 0: [2, 6]</li>
  <li>Level 1: [5, 11, 4] (Overlapping nodes are added in their level order sequence)</li>
  <li>Level 2: [9]</li>
</ul>

<br>

<p><strong>Solution</strong></p>
<p><strong>Intuition of the Approach:</strong></p>

<p><strong>1. Concept of Vertical Order Traversal:</strong></p>
<ul>
  <li>We aim to print nodes of the binary tree in vertical order, grouping nodes that align vertically.</li>
  <li>Nodes at the same vertical level are listed from top to bottom.</li>
</ul>

<img src="https://static.takeuforward.org/content/vertical-traversal-image5-umLmDdn9">
<img src="https://static.takeuforward.org/content/vertical-traversal-image6-C7TnRsK4">
<p><strong>2. Using Horizontal Distance:</strong></p>
<ul>
  <li>We use "horizontal distance" to track a node's position from the root node horizontally.</li>
  <li>The root node starts at a horizontal distance of <code>0</code>.</li>
  <li>Nodes to the left decrease the horizontal distance by <code>1</code> for each step left.</li>
  <li>Nodes to the right increase the horizontal distance by <code>1</code> for each step right.</li>
  <li>Example:</li>
  <pre>
      1
     / \
    2   3
  </pre>
  <ul>
    <li>Node <code>1</code> is at horizontal distance <code>0</code>.</li>
    <li>Node <code>2</code> is at horizontal distance <code>-1</code> (one step left).</li>
    <li>Node <code>3</code> is at horizontal distance <code>1</code> (one step right).</li>
  </ul>
</ul>

<p><strong>3. Level Tracking:</strong></p>
<ul>
  <li>Along with horizontal distance, we track the "level" or depth of the node in the tree.</li>
  <li>The root node is at level <code>0</code>.</li>
  <li>Each child node is at the level of its parent plus <code>1</code>.</li>
  <li>Example:</li>
  <pre>
      1 (Level 0)
     / \
    2   3 (Level 1)
  </pre>
</ul>

<p><strong>4. Traversal Using a Queue:</strong></p>
<ul>
  <li>Use a queue for level-order traversal (breadth-first traversal).</li>
  <li>Start with the root node, enqueue its children with updated horizontal distances and levels.</li>
  <li>Process each node, adding its value to a storage structure based on horizontal distance and level.</li>
</ul>

<p><strong>5. Storing Node Values:</strong></p>
<ul>
  <li>Store node values in a dictionary where:</li>
  <ul>
    <li>The key is the horizontal distance.</li>
    <li>The value is another dictionary with:</li>
    <ul>
      <li>The key being the level.</li>
      <li>The value being a list of node values at that level.</li>
    </ul>
  </ul>
  <li>Example:</li>
  <pre>
  store:
  {
    -1: {1: [2]},
     0: {0: [1], 1: [5]},
     1: {1: [3], 2: [7]},
     2: {2: [6]}
  }
  </pre>
</ul>
<img src="https://static.takeuforward.org/content/vertical-traversal-image8-ieYxlxXx">

<p><strong>6. Constructing the Final Result:</strong></p>
<ul>
  <li>After processing all nodes, sort the keys of the outer dictionary (horizontal distances) and then sort nodes at each level.</li>
  <li>Combine the sorted nodes for each horizontal distance into a single list.</li>
  <li>Example:</li>
  <pre>
  Final Result:
  [
    [4],        # Horizontal distance -2
    [2],        # Horizontal distance -1
    [1, 5],     # Horizontal distance 0
    [3, 7],     # Horizontal distance 1
    [6]         # Horizontal distance 2
  ]
  </pre>
</ul>
<img src="https://static.takeuforward.org/content/vertical-traversal-image10-OwfFCRvB">
<p><strong>Summary of Steps:</strong></p>
<ul>
  <li><strong>Initialization:</strong> Start with the root node and initialize a queue with the root and its horizontal distance <code>0</code>.</li>
  <li><strong>Level-order Traversal:</strong> Process nodes level by level using the queue, updating horizontal distances and levels.</li>
  <li><strong>Store Values:</strong> Use a dictionary to store node values grouped by horizontal distance and level.</li>
  <li><strong>Result Construction:</strong> Sort the stored values and combine them to form the final vertical order list.</li>
</ul>


```python
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque,defaultdict
def default():
    return defaultdict(list)
def solve(node):
    ans=[]
    if not node:
        return ans
    queue=deque()
    queue.append((node,0))
    level=0
    store=defaultdict(default)
    while queue:
        n=len(queue)
        for i in range(n):
            node,x=queue.popleft()
            store[x][level].append(node.data)
            if(node.left):
                queue.append((node.left,x-1))
            if(node.right):
                queue.append((node.right,x+1))
        level+=1
    temp=sorted(store.items(),key=lambda x:x[0])
    for x,l_values in temp:
        vertical=[]
        l_values=sorted(l_values.items(),key=lambda x:x[0])
        for level,values in l_values:
            vertical.extend(sorted(values))
        ans.append(vertical)
    return ans
        
        
    


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)

print(solve(root))

```

<p><strong>Time Complexity:</strong> O(N log N) – Sorting nodes adds a log factor, but each node is processed once.</p>
<p><strong>Space Complexity:</strong> O(N) – Space for the queue and the <code>store</code> dictionary, which stores all nodes.</p>


<br>
<br>

<h1>Top View Of Binary Tree</h1>
<p>Given a Binary Tree, return its Top View. The Top View of a Binary Tree is the set of nodes visible when we see the tree from the top.</p>
<p><strong>Examples</strong></p>
<p><strong>Input :</strong>Binary Tree: 1 2 3 4 10 9 11 -1 5 -1 -1 -1 -1 -1 -1 -1 6</p>
<img src="https://static.takeuforward.org/content/top-view-tree-image1-B4hVS6fx">
<p><strong>Output :</strong>Top View: [4, 2, 1, 3, 11]</p>
<p><strong>Explanation :</strong></p>
<img src="https://static.takeuforward.org/content/top-view-tree-image2-yzsmeIXv">
<br>
<p><strong>Input :</strong>Binary Tree: 2 7 5 2 6 -1 9 -1 -1 5 11 4 -1</p>
<img src="https://static.takeuforward.org/content/top-view-tree-image3-HzQGi34x">
<p><strong>Output :</strong>Top View: [2, 7, 2, 5, 9]</p>
<p><strong>Explanation :</strong></p>
<img src="https://static.takeuforward.org/content/top-view-tree-image4-IZBtc6WM">

<br>

<p><strong>Solution</strong></p>
<p><strong>Intuition Behind the Top View of a Binary Tree:</strong></p>

<p><strong>Goal:</strong></p>
<ul>
  <li>To print the top view of a binary tree, which includes the nodes that are visible when the tree is viewed from above.</li>
  <li>Specifically, we need to capture the nodes that appear at the top-most level for each vertical column of the tree.</li>
</ul>

<p><strong>Concepts Involved:</strong></p>

<ul>
  <li><strong>Horizontal Distance (HD):</strong></li>
  <ul>
    <li>Nodes are assigned a horizontal distance from the root node:</li>
    <ul>
      <li>The root node starts at horizontal distance <code>0</code>.</li>
      <li>Moving left decreases the horizontal distance by <code>1</code>.</li>
      <li>Moving right increases the horizontal distance by <code>1</code>.</li>
    </ul>
  </ul>
  <li><strong>Vertical Levels:</strong></li>
  <ul>
    <li>Nodes at the same horizontal distance but different levels (depths) will be printed based on the top-most level.</li>
    <li>The idea is to only keep track of the first node encountered at each horizontal distance, as this will be the top-most node for that column.</li>
  </ul>
</ul>

<p><strong>Steps of the Approach:</strong></p>
<ul>
  <li><strong>Initialization:</strong></li>
  <ul>
    <li>Use a queue for level-order traversal (breadth-first traversal) of the tree.</li>
    <li>Start with the root node at horizontal distance <code>0</code>.</li>
  </ul>
  <li><strong>Traversal:</strong></li>
  <ul>
    <li>Process each node in the queue, and for each node:</li>
    <ul>
      <li>Record its value if its horizontal distance is not already in the dictionary (<code>store</code>).</li>
      <li>Update the dictionary with the node's value for its horizontal distance if it's the first node encountered at that distance.</li>
      <li>Add the node’s left and right children to the queue with updated horizontal distances.</li>
    </ul>
  </ul>
  <li><strong>Result Construction:</strong></li>
  <ul>
    <li>After traversal, sort the dictionary by horizontal distance.</li>
    <li>Collect the node values from the sorted dictionary, which represent the top view of the tree.</li>
  </ul>
</ul>

<p><strong>Detailed Explanation of the Code:</strong></p>

```python
from collections import deque

def solve(node):
    ans = []
    if not node:
        return ans
    
    # Initialize a queue for level-order traversal
    queue = deque()
    queue.append((node, 0))  # (node, horizontal distance)
    
    # Dictionary to store the first node at each horizontal distance
    store = {}
    
    while queue:
        n = len(queue)  # Number of nodes at the current level
        for i in range(n):
            node, x = queue.popleft()  # Dequeue node and its horizontal distance
            
            # Store the node data if the horizontal distance is not already in the dictionary
            if x not in store:
                store[x] = node.data
            
            # Enqueue left and right children with updated horizontal distances
            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))
    
    # Sort the dictionary by horizontal distance
    temp = sorted(store.items(), key=lambda x: x[0])
    
    # Collect the values in sorted order
    for x, data in temp:
        ans.append(data)
    
    return ans
```

<p><strong>Explanation of the Code:</strong></p>

<ul>
  <li><strong>Queue Initialization:</strong> Start with the root node and its horizontal distance <code>0</code>.</li>
  <li><strong>Processing Nodes:</strong> Dequeue nodes, and for each node:</li>
  <ul>
    <li>Check if its horizontal distance is already in <code>store</code>. If not, add it.</li>
    <li>Add children to the queue with their respective horizontal distances.</li>
  </ul>
  <li><strong>Sorting and Collecting Results:</strong> After traversing the tree, sort the horizontal distances. Append node values to <code>ans</code> in the order of sorted horizontal distances.</li>
</ul>

<p><strong>Summary:</strong></p>
<ul>
  <li><strong>Top View:</strong> Captures nodes visible from above.</li>
  <li><strong>First Encountered Nodes:</strong> Only the first node at each horizontal distance is stored.</li>
  <li><strong>Sorting:</strong> Ensures nodes are collected in the correct order for output.</li>
</ul>

<p>This approach ensures that you accurately capture the top view of the binary tree by focusing on horizontal distance and the first visible nodes at each distance.</p>

<p><strong>Time Complexity:</strong> O(N), where N is the number of nodes in the tree. Each node is processed exactly once in level-order traversal.</p>

<p><strong>Space Complexity:</strong> O(N), where N is the number of nodes in the tree. Space is required for the queue and the dictionary to store nodes and their horizontal distances.</p>


<br>
<br>

<h2>Bottom View Of Binary Tree</h2>
<p>Given a Binary Tree, return its Bottom View. The Bottom View of a Binary Tree is the set of nodes visible when we see the tree from the bottom.</p>
<p><strong>Input :</strong>Binary Tree: 1 2 3 4 10 9 11 -1 5 -1 -1 -1 -1 -1 -1 -1 6</p>
<img src="https://static.takeuforward.org/content/top-view-tree-image1-B4hVS6fx">
<p><strong>Output :</strong>Bottom View Traversal: [4, 5, 6, 3, 11]</p>
<p><strong>Explanation :</strong>The bottom view of the binary tree would comprise of the nodes that are the last encountered nodes for each vertical index.</p>
<img src="https://static.takeuforward.org/content/bottom-view-tree-image1-I3NBaM0T">
<br>
<p><strong>Input :</strong>Binary Tree: 2 7 5 2 6 -1 9 -1 -1 5 11 4 -1</p>
<img src="https://static.takeuforward.org/content/top-view-tree-image3-HzQGi34x">
<p><strong>Output :Bottom View: [2 5 6 11 4 9]</strong></p>
<p><strong>Explanation :</strong></p>
<img src="https://static.takeuforward.org/content/bottom-view-tree-image2-x_0nezDl">

<br>

<p><strong>Solution</strong></p>
<p><strong>Goal:</strong></p>
<ul>
    <li>To print the bottom view of a binary tree, which includes the nodes that are visible when the tree is viewed from below.</li>
    <li>The bottom view captures the nodes that appear at the bottom-most level for each vertical column of the tree.</li>
</ul>
<p>So, we have to track last nodes of a vertical order, so we keep on updating dictionary, so at final it will contain last nodes of binary tree</p>

<p><strong>Code Explanation:</strong></p>


```python
from collections import deque

def solve(node):
    ans = []
    if not node:
        return ans
    
    # Initialize a queue for level-order traversal
    queue = deque()
    queue.append((node, 0))  # (node, horizontal distance)
    
    # Dictionary to store the last node at each horizontal distance
    store = {}
    
    while queue:
        n = len(queue)  # Number of nodes at the current level
        for i in range(n):
            node, x = queue.popleft()  # Dequeue node and its horizontal distance
            
            # Store or update the node data for the horizontal distance
            store[x] = node.data
            
            # Enqueue left and right children with updated horizontal distances
            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))
    
    # Sort the dictionary by horizontal distance
    temp = sorted(store.items(), key=lambda x: x[0])
    
    # Collect the values in sorted order
    for x, data in temp:
        ans.append(data)
    
    return ans
```

<p><strong>Detailed Intuition:</strong></p>
<ul>
    <li><strong>Horizontal Distance (HD):</strong></li>
    <ul>
        <li>Nodes are assigned a horizontal distance from the root node:</li>
        <ul>
            <li>Root node starts at horizontal distance <code>0</code>.</li>
            <li>Moving left decreases the horizontal distance by <code>1</code>.</li>
            <li>Moving right increases the horizontal distance by <code>1</code>.</li>
        </ul>
    </ul>
    <li><strong>Bottom View Nodes:</strong></li>
    <ul>
        <li>We need to capture the nodes that are at the bottom-most level for each vertical column.</li>
        <li>This means that if a node is at the same horizontal distance but at a lower level (deeper in the tree), it should be the one recorded.</li>
    </ul>
    <li><strong>Level-Order Traversal:</strong></li>
    <ul>
        <li>Use a queue to perform level-order traversal of the tree.</li>
        <li>For each node, update the dictionary to store the node's value for its horizontal distance. This ensures that the latest node encountered at that distance (i.e., the bottom-most node) is recorded.</li>
    </ul>
    <li><strong>Constructing Result:</strong></li>
    <ul>
        <li>After traversal, sort the dictionary by horizontal distance.</li>
        <li>Collect the node values from the sorted dictionary, which represent the bottom view of the tree.</li>
    </ul>
</ul>

<p><strong>Time and Space Complexity:</strong></p>
<p><strong>Time Complexity:</strong> O(N), where N is the number of nodes in the tree. Each node is processed exactly once in level-order traversal.</p>

<p><strong>Space Complexity:</strong> O(N), where N is the number of nodes in the tree. Space is required for the queue and the dictionary to store nodes and their horizontal distances.</p>

<p><strong>Summary:</strong></p>
<ul>
    <li><strong>Bottom View:</strong> Captures nodes visible from below.</li>
    <li><strong>Last Encountered Nodes:</strong> Only the last node at each horizontal distance is stored.</li>
    <li><strong>Sorting:</strong> Ensures nodes are collected in the correct order for output.</li>
</ul>

<p>This approach accurately captures the bottom view of the binary tree by focusing on the latest visible nodes at each horizontal distance.</p>


<br>
<br>

<h1>Left And Right View Of Binary Tree</h1>
<p>Given a Binary Tree, return its right and left views.</p>
<p>The Right View of a Binary Tree is a list of nodes that can be seen when the tree is viewed from the right side. The Left View of a Binary Tree is a list of nodes that can be seen when the tree is viewed from the left side.</p>

<p><strong>Examples</strong></p>
<p><strong>Input :</strong>Binary Tree: 1 2 3 4 10 9 11 -1 5 -1 -1 -1 -1 -1 -1 -1 6 </p>
<img src="https://static.takeuforward.org/content/right-left-tree-image1-LK79LuMP">
<p><strong>Output :</strong>Left View: [1, 2, 4, 5, 6] , Right View: [1, 3, 11, 5, 6]</p>
<p><strong>Explanation :</strong></p>
<img src="https://static.takeuforward.org/content/right-left-tree-image2-4lJ-ias4">
<br>
<p><strong>Input :</strong>Binary Tree: 2 7 5 2 6 -1 9 -1 -1 5 11 4 -1</p>
<img src="https://static.takeuforward.org/content/right-left-tree-image3-oyZSMVIG">
<p><strong>Output :</strong>Left View Traversal:[2,7,2,5], Right View Traversal:[2,5,9,4] </p>
<p><strong>Explanation :</strong></p>
<img src="https://static.takeuforward.org/content/right-left-tree-image4-bZR52MA_">

<br>

<p><strong>Iterative Solution</strong></p>
<p><strong>Goal:</strong></p>
<ul>
    <li><strong>Left View:</strong> Nodes visible when the tree is viewed from the left side.</li>
    <li><strong>Right View:</strong> Nodes visible when the tree is viewed from the right side.</li>
</ul>
<p><strong>Detailed Intuition:</strong></p>
<ul>
    <li><strong>Left and Right View Concepts:</strong></li>
    <ul>
        <li><strong>Left View:</strong> Nodes that are visible when looking at the tree from the left. These are typically the first nodes encountered at each level.</li>
        <li><strong>Right View:</strong> Nodes that are visible when looking at the tree from the right. These are typically the last nodes encountered at each level.</li>
    </ul>
    <li><strong>Level-Order Traversal:</strong></li>
    <ul>
        <li>Use a queue to perform level-order traversal (breadth-first traversal) of the tree. This ensures that nodes are processed level by level.</li>
        <li>For each level:
            <ul>
                <li><strong>Left View:</strong> Record the first node encountered at the level.</li>
                <li><strong>Right View:</strong> Record the last node encountered at the level.</li>
            </ul>
        </li>
    </ul>
    <li><strong>Processing Nodes:</strong></li>
    <ul>
        <li>As nodes are processed at each level, collect the first and last node values of that level to build the left and right views, respectively.</li>
    </ul>
    <li><strong>Constructing Result:</strong></li>
    <ul>
        <li>After traversal, the collected nodes for each view represent the left and right views of the binary tree.</li>
    </ul>
</ul>

```python
from collections import deque

def solve(node):
    left, right = [], []
    if not node:
        return left, right
    
    queue = deque()
    queue.append(node)
    level = []
    
    while queue:
        n = len(queue)  # Number of nodes at the current level
        for i in range(n):
            node = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Append the first and last element of the current level
        left.append(level[0])
        right.append(level[n-1])
        level = []
    
    return left, right
```

<p><strong>Time and Space Complexity:</strong></p>
<p><strong>Time Complexity:</strong> O(N), where N is the number of nodes in the tree. Each node is processed exactly once in level-order traversal.</p>

<p><strong>Space Complexity:</strong> O(N), where N is the number of nodes in the tree. Space is required for the queue and the level lists to store nodes at each level.</p>

<p><strong>Summary:</strong></p>
<ul>
    <li><strong>Left View:</strong> Captures the nodes visible from the left side of the tree.</li>
    <li><strong>Right View:</strong> Captures the nodes visible from the right side of the tree.</li>
    <li><strong>Level Order Traversal:</strong> Ensures nodes are processed level by level to correctly identify the left and right view nodes.</li>
</ul>

<p>This approach accurately captures the left and right views of the binary tree by focusing on the first and last nodes at each level during level-order traversal.</p>
<br>
<p><strong>Recursive Solution</strong></p>
<p><strong>Goal:</strong></p>
<ul>
    <li><strong>Left View:</strong> Nodes visible when the tree is viewed from the left side.</li>
    <li><strong>Right View:</strong> Nodes visible when the tree is viewed from the right side.</li>
</ul>

<p><strong>Detailed Intuition:</strong></p>
<ul>
    <li><strong>Left and Right View Concepts:</strong></li>
    <ul>
        <li><strong>Left View:</strong> Nodes that are visible when looking at the tree from the left. These are typically the first nodes encountered at each level.</li>
        <li><strong>Right View:</strong> Nodes that are visible when looking at the tree from the right. These are typically the first nodes encountered at each level.</li>
    </ul>
    <li><strong>Recursive Approach:</strong></li>
    <ul>
        <li>Use recursion to traverse the tree and collect the first node encountered at each level.</li>
        <li>For the <strong>left view</strong>:
            <ul>
                <li>Traverse the left subtree before the right subtree.</li>
            </ul>
        </li>
        <li>For the <strong>right view</strong>:
            <ul>
                <li>Traverse the right subtree before the left subtree.</li>
            </ul>
        </li>
    </ul>
    <li><strong>Processing Nodes:</strong></li>
    <ul>
        <li>For each node, check if it is the first node at its level (i.e., <code>level == len(ans)</code>).</li>
        <li>If it is, add the node's data to the result list <code>ans</code>.</li>
    </ul>
    <li><strong>Constructing Result:</strong></li>
    <ul>
        <li>The collected nodes for each view (stored in <code>ans</code>) represent the left and right views of the binary tree.</li>
    </ul>
</ul>


```python
def leftView(node, level, ans):
    if not node:
        return
    # If this is the first node of its level
    if level == len(ans):
        ans.append(node.data)
    # Recur for left subtree first, then right subtree
    leftView(node.left, level + 1, ans)
    leftView(node.right, level + 1, ans)

def rightView(node, level, ans):
    if not node:
        return
    # If this is the first node of its level
    if level == len(ans):
        ans.append(node.data)
    # Recur for right subtree first, then left subtree
    rightView(node.right, level + 1, ans)
    rightView(node.left, level + 1, ans)
```

<p><strong>Time and Space Complexity:</strong></p>
<p><strong>Time Complexity:</strong> O(N), where N is the number of nodes in the tree. Each node is processed exactly once.</p>

<p><strong>Space Complexity:</strong> O(H), where H is the height of the tree. Space is required for the recursion stack.</p>

<p><strong>Summary:</strong></p>
<ul>
    <li><strong>Left View:</strong> Captures the nodes visible from the left side of the tree by traversing the left subtree before the right subtree.</li>
    <li><strong>Right View:</strong> Captures the nodes visible from the right side of the tree by traversing the right subtree before the left subtree.</li>
    <li><strong>Recursive Approach:</strong> Ensures nodes are processed in the correct order to identify the left and right view nodes.</li>
</ul>

<p>This approach accurately captures the left and right views of the binary tree by focusing on the first nodes encountered at each level during recursive traversal.</p>


<br>
<br>