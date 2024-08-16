<h1>Binary Seach Tree (BST)</h1>
<p><strong>Binary Search Tree (BST)</strong> is a type of binary tree that is specifically structured to make searching for elements more efficient. Here’s a breakdown of what a Binary Search Tree is and how it works:</p>

<p><strong>Structure of a Binary Search Tree</strong></p>

<ul>
  <li><strong>Binary Tree Basics:</strong> A binary tree is a tree data structure where each node has at most two children, referred to as the left child and the right child.</li>
  <li><strong>BST Properties:</strong>
    <ul>
      <li><strong>Left Subtree:</strong> All nodes in the left subtree of a node have values less than the node’s value.</li>
      <li><strong>Right Subtree:</strong> All nodes in the right subtree of a node have values greater than the node’s value.</li>
    </ul>
  </li>
</ul>

<p>This rule applies recursively to all nodes in the tree, meaning each subtree also follows the BST property.</p>

<p><strong>Example of a BST</strong></p>

<p>Consider a BST with the following structure:</p>

<ul>
  <li>The root node is 15.</li>
  <li>The left subtree of 15 has nodes with values less than 15 (10, 8, 12).</li>
  <li>The right subtree of 15 has nodes with values greater than 15 (20, 17, 25).</li>
</ul>

<p>This pattern repeats for every node in the tree.</p>

<p><strong>Why Use a Binary Search Tree?</strong></p>

<p>The primary advantage of using a BST is that it allows for efficient searching, insertion, and deletion of elements. Here’s why:</p>

<ul>
  <li><strong>Efficient Searching:</strong> In a balanced BST, the height of the tree is proportional to <strong>log₂(N)</strong>, where <strong>N</strong> is the number of nodes. This ensures that the time complexity for searching is <strong>O(log N)</strong>, much faster than <strong>O(N)</strong> in an unstructured binary tree.</li>
</ul>

<p><strong>Searching Process:</strong></p>

<ol>
  <li>Begin at the root node.</li>
  <li>Compare the target value with the root.</li>
  <li>If the target value is less, move to the left subtree; if greater, move to the right subtree.</li>
  <li>Repeat this process until the target value is found or the subtree is empty (meaning the value is not in the tree).</li>
</ol>

<p><strong>Example of Searching in a BST</strong></p>

<p>Suppose you want to find the value 17 in the above tree:</p>

<ol>
  <li>Start at the root (15).</li>
  <li>Since 17 is greater than 15, move to the right child (20).</li>
  <li>Since 17 is less than 20, move to the left child (17).</li>
  <li>The target value 17 is found.</li>
</ol>

<p><strong>Balancing in a BST</strong></p>

<ul>
  <li><strong>Balanced vs. Unbalanced:</strong> A BST is said to be balanced when the height difference between the left and right subtrees of any node is minimal (often at most one).</li>
  <li>If a BST becomes unbalanced (one subtree is significantly taller than the other), the time complexity for operations can degrade to <strong>O(N)</strong>.</li>
</ul>

<p><strong>Variants of Binary Search Trees</strong></p>

<ul>
  <li><strong>Self-Balancing BSTs:</strong> There are several types of self-balancing BSTs, like <strong>AVL Trees</strong> and <strong>Red-Black Trees</strong>, which automatically adjust the tree's structure to maintain a balanced state after insertions and deletions.</li>
</ul>

<p><strong>Applications of BST</strong></p>

<ul>
  <li><strong>Searching:</strong> Fast search operations due to the ordered structure.</li>
  <li><strong>Sorting:</strong> In-order traversal of a BST will give the elements in sorted order.</li>
  <li><strong>Dynamic Data Structures:</strong> Efficient for maintaining a dynamically changing dataset, where elements need to be frequently inserted, deleted, or searched.</li>
</ul>

<p>In summary, a <strong>Binary Search Tree</strong> is an optimized binary tree that facilitates quick lookup, insertion, and deletion operations, making it a fundamental structure in computer science, particularly for applications requiring dynamic data handling.</p>

<p><strong>Real-Time Applications of Binary Search Trees (BST)</strong></p>

<ul>
  <li><strong>Database Indexing:</strong>
    <ul>
      <li><strong>Application:</strong> Databases use BSTs to implement indexing mechanisms, allowing for quick retrieval of records.</li>
      <li><strong>Example:</strong> When you search for a record in a large database, the database uses a BST-based index to quickly find the data.</li>
    </ul>
  </li>

  <li><strong>File Systems:</strong>
    <ul>
      <li><strong>Application:</strong> File systems use BSTs to manage directories and files efficiently.</li>
      <li><strong>Example:</strong> When you search for a file on your computer, the file system might use a BST to quickly locate the file among potentially thousands of others.</li>
    </ul>
  </li>

  <li><strong>Autocompletion and Spell Checkers:</strong>
    <ul>
      <li><strong>Application:</strong> BSTs are used to store dictionaries in applications that require fast lookup, like autocompletion and spell checkers.</li>
      <li><strong>Example:</strong> When you start typing in a search bar, the application quickly suggests completions based on a BST of possible words.</li>
    </ul>
  </li>

  <li><strong>Network Routing Algorithms:</strong>
    <ul>
      <li><strong>Application:</strong> BSTs help in optimizing routing decisions in network traffic.</li>
      <li><strong>Example:</strong> In Internet routing, BSTs are used to find the best path to forward data packets based on the destination address.</li>
    </ul>
  </li>

  <li><strong>Symbol Tables in Compilers:</strong>
    <ul>
      <li><strong>Application:</strong> Compilers use BSTs to implement symbol tables, which are used to store variables, functions, and other identifiers.</li>
      <li><strong>Example:</strong> When compiling code, the compiler uses a BST to quickly look up and manage variable names and their associated data.</li>
    </ul>
  </li>

  <li><strong>Memory Management:</strong>
    <ul>
      <li><strong>Application:</strong> Operating systems use BSTs for managing memory allocation efficiently.</li>
      <li><strong>Example:</strong> BSTs can help in quickly finding a free memory block of a required size during program execution.</li>
    </ul>
  </li>

  <li><strong>Version Control Systems:</strong>
    <ul>
      <li><strong>Application:</strong> BSTs are used in version control systems to manage different versions of files or software.</li>
      <li><strong>Example:</strong> When you retrieve a previous version of a file in a version control system like Git, the system might use a BST to manage and access these versions efficiently.</li>
    </ul>
  </li>

  <li><strong>Priority Queues:</strong>
    <ul>
      <li><strong>Application:</strong> BSTs can be used to implement priority queues, where elements are dequeued based on their priority.</li>
      <li><strong>Example:</strong> In job scheduling systems, BSTs help in managing tasks and processing them based on priority.</li>
    </ul>
  </li>
</ul>

<br>
<br>


<h1>Search Given Target In Binary Tree</h1>
<p><strong>Problem Statement</strong></p>
<p>Given the root of a Binary Search Tree (BST) and a target value, determine if the target value exists in the tree. The function should return <strong>True</strong> if the target is found in the tree, otherwise, it should return <strong>False</strong>.</p>

<p><strong>Sample Test Cases</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [4, 2, 7, 1, 3], target = 2</li>
            <li><strong>Output:</strong> True</li>
            <li><strong>Explanation:</strong> The target value 2 exists in the tree.</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [4, 2, 7, 1, 3], target = 5</li>
            <li><strong>Output:</strong> False</li>
            <li><strong>Explanation:</strong> The target value 5 does not exist in the tree.</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [], target = 1</li>
            <li><strong>Output:</strong> False</li>
            <li><strong>Explanation:</strong> The tree is empty, so the target cannot be found.</li>
        </ul>
    </li>
    <li><strong>Test Case 4:</strong>
        <ul>
            <li><strong>Input:</strong> root = [4, 2, 7, 1, 3], target = 4</li>
            <li><strong>Output:</strong> True</li>
            <li><strong>Explanation:</strong> The target value 4 is the root of the tree and exists.</li>
        </ul>
    </li>
</ol>

<p><strong>Approach</strong></p>

<p><strong>Intuition:</strong></p>
<p>The Binary Search Tree (BST) property allows us to search for a value efficiently. For any node, the left child contains values less than the node's value, and the right child contains values greater than the node's value. By comparing the target value with the current node, we can decide whether to move left or right, reducing the search space by half at each step.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Start at the root of the tree.</li>
    <li>Compare the target value with the value of the current node.</li>
    <li>If the target is equal to the current node's value, return <strong>True</strong>.</li>
    <li>If the target is greater, move to the right child; if it's smaller, move to the left child.</li>
    <li>Continue this process until the target is found or a <strong>None</strong> node is reached (indicating that the target does not exist in the tree).</li>
    <li>If the loop ends with a <strong>None</strong> node, return <strong>False</strong>.</li>
</ol>

<p><strong>Code</strong></p>

```python
class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def solve(root,target):
    node=root
    while node and node.data!=target:
        if(target>node.data):
            node=node.right
        else:
            node=node.left
    if(node):
        return True
    else:
        return False

root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)
target=int(input())
print(solve(root,target))

```

<p><strong>Time and Space Complexity</strong></p>

<ul>
    <li><strong>Time Complexity:</strong> The time complexity is <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. In the worst case, if the tree is completely unbalanced (like a linked list), <strong>h</strong> could be <strong>O(n)</strong>, where <strong>n</strong> is the number of nodes. In the best case, when the tree is balanced, <strong>h</strong> is <strong>O(log n)</strong>.</li>
    <li><strong>Space Complexity:</strong> The space complexity is <strong>O(1)</strong> because no additional data structures are used, and the function works in place.</li>
</ul>


<br>
<br>

<h1>Find Min and Max Of Given BST</h1>
<p><strong>Problem Statement</strong></p>
<p>Given the root of a Binary Search Tree (BST), implement two functions:</p>
<ul>
    <li><strong>min(root):</strong> Returns the minimum value in the BST.</li>
    <li><strong>max(root):</strong> Returns the maximum value in the BST.</li>
</ul>

<p><strong>Sample Test Cases</strong></p>

<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [4, 2, 7, 1, 3]</li>
            <li><strong>Output (min):</strong> 1</li>
            <li><strong>Output (max):</strong> 7</li>
            <li><strong>Explanation:</strong> The minimum value in the BST is 1, and the maximum value is 7.</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [10, 5, 15, 2, 7, 12, 20]</li>
            <li><strong>Output (min):</strong> 2</li>
            <li><strong>Output (max):</strong> 20</li>
            <li><strong>Explanation:</strong> The minimum value in the BST is 2, and the maximum value is 20.</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8]</li>
            <li><strong>Output (min):</strong> 8</li>
            <li><strong>Output (max):</strong> 8</li>
            <li><strong>Explanation:</strong> The tree has only one node, so both the minimum and maximum values are 8.</li>
        </ul>
    </li>
</ol>

<p><strong>Approach</strong></p>

<p><strong>Intuition:</strong></p>
<p>In a Binary Search Tree (BST), the minimum value is always found at the leftmost node, and the maximum value is found at the rightmost node. By traversing to the leftmost node for the minimum and the rightmost node for the maximum, we can efficiently find the required values.</p>

<p><strong>Steps to Solve:</strong></p>

<ol>
    <li><strong>min(root):</strong>
        <ol>
            <li>Start at the root of the tree.</li>
            <li>Traverse left until you reach the leftmost node (where there is no left child).</li>
            <li>Return the value of this node as the minimum value in the tree.</li>
        </ol>
    </li>
    <li><strong>max(root):</strong>
        <ol>
            <li>Start at the root of the tree.</li>
            <li>Traverse right until you reach the rightmost node (where there is no right child).</li>
            <li>Return the value of this node as the maximum value in the tree.</li>
        </ol>
    </li>
</ol>

<p><strong>Code</strong></p>

```python
def min(root):
    node = root
    while node.left:
        node = node.left
    return node.data

def max(root):
    node = root
    while node.right:
        node = node.right
    return node.data

```

<p><strong>Time and Space Complexity</strong></p>

<ul>
    <li><strong>Time Complexity:</strong> The time complexity for both <strong>min</strong> and <strong>max</strong> functions is <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is because, in the worst case, you may need to traverse from the root to the deepest leaf node.</li>
    <li><strong>Space Complexity:</strong> The space complexity for both functions is <strong>O(1)</strong> because they only use a constant amount of additional space.</li>
</ul>


<br>
<br>

<h1>Check Given Inorder of binary tree is BST or not</h1>
<p><strong>Problem Statement</strong></p>
<p>Given the inorder traversal of a binary tree as a list, determine if the binary tree is a Binary Search Tree (BST). A binary tree is a BST if its inorder traversal results in a sorted list in strictly increasing order.</p>

<p><strong>Sample Test Cases</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> inorder = [1, 2, 3, 4, 5]</li>
            <li><strong>Output:</strong> True</li>
            <li><strong>Explanation:</strong> The list is sorted in strictly increasing order, so the binary tree is a BST.</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> inorder = [5, 3, 6, 2, 4]</li>
            <li><strong>Output:</strong> False</li>
            <li><strong>Explanation:</strong> The list is not sorted in strictly increasing order, so the binary tree is not a BST.</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> inorder = [7, 7, 8, 10]</li>
            <li><strong>Output:</strong> False</li>
            <li><strong>Explanation:</strong> The list has duplicate elements (7), which violates the BST property of strictly increasing order.</li>
        </ul>
    </li>
    <li><strong>Test Case 4:</strong>
        <ul>
            <li><strong>Input:</strong> inorder = [2, 3, 4]</li>
            <li><strong>Output:</strong> True</li>
            <li><strong>Explanation:</strong> The list is sorted in strictly increasing order, so the binary tree is a BST.</li>
        </ul>
    </li>
</ol>

<p><strong>Approach</strong></p>

<p><strong>Intuition:</strong></p>
<p>The inorder traversal of a Binary Search Tree (BST) should produce a list of elements in strictly increasing order (i.e., each element is greater than the one before it). If the given inorder list is sorted in strictly increasing order, then the binary tree is a BST.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Iterate through the given list from the first to the second-to-last element.</li>
    <li>For each element, check if it is greater than or equal to the next element.</li>
    <li>If any element is found to be greater than or equal to the next element, return <strong>False</strong> because this violates the BST property.</li>
    <li>If no such elements are found, return <strong>True</strong>.</li>
</ol>

<p><strong>Code</strong></p>

```python
def check(inorder):
    n=len(inorder)
    for i in range(n-1):
        if(inorder[i]>=inorder[i+1]):
            return False
    return True

inorder=list(map(int,input().split()))
print(check(inorder))

```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> The time complexity is <strong>O(n)</strong>, where <strong>n</strong> is the length of the inorder list. This is because we need to iterate through the list once to check the ordering of elements.</li>
    <li><strong>Space Complexity:</strong> The space complexity is <strong>O(1)</strong> because the function uses a constant amount of additional space.</li>
</ul>

<br>
<br>

<h1>Ceil and Floor Of Given Target in BST</h1>
<p><strong>Problem Statement</strong></p>
<p>Implement two functions <code>ceil(root, target)</code> and <code>floor(root, target)</code> that find the ceiling and floor of a given target value in a Binary Search Tree (BST).</p>
<ul>
    <li><strong>Ceiling (ceil):</strong> The smallest element in the BST that is greater than or equal to the target value.</li>
    <li><strong>Floor:</strong> The largest element in the BST that is less than or equal to the target value.</li>
</ul>

<p><strong>Intuition Behind the <code>ceil</code> and <code>floor</code> Functions</strong></p>
<p>In a Binary Search Tree (BST), the nodes are arranged such that:</p>
<ul>
    <li>The left subtree of a node contains only nodes with values less than the node's value.</li>
    <li>The right subtree of a node contains only nodes with values greater than the node's value.</li>
</ul>
<p>This property of the BST allows us to efficiently find the ceiling and floor of a given target value.</p>

<p><strong>Sample Test Cases</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14], target = 5</li>
            <li><strong>Output (Ceiling):</strong> 6</li>
            <li><strong>Output (Floor):</strong> 4</li>
            <li><strong>Explanation:</strong> The ceiling of 5 is 6, and the floor of 5 is 4.</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14], target = 13</li>
            <li><strong>Output (Ceiling):</strong> 14</li>
            <li><strong>Output (Floor):</strong> 12</li>
            <li><strong>Explanation:</strong> The ceiling of 13 is 14, and the floor of 13 is 12.</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14], target = 7</li>
            <li><strong>Output (Ceiling):</strong> 8</li>
            <li><strong>Output (Floor):</strong> 6</li>
            <li><strong>Explanation:</strong> The ceiling of 7 is 8, and the floor of 7 is 6.</li>
        </ul>
    </li>
</ol>


<p><strong>Ceiling Function (<code>ceil</code>):</strong></p>
<p><strong>Goal:</strong> Find the smallest value in the BST that is greater than or equal to the target value.</p>
<p><strong>Intuition:</strong></p>
<ul>
    <li>Start at the root of the tree.</li>
    <li>If the root’s value is exactly equal to the target, then the root’s value is the ceiling.</li>
    <li>If the target is greater than the root’s value, the ceiling must be in the right subtree because all values in the left subtree are smaller than the root.</li>
    <li>If the target is smaller than the root’s value, the root's value could potentially be the ceiling, but we still need to check the left subtree to see if there's an even smaller value that is still greater than or equal to the target.</li>
</ul>
<p>As we traverse the tree:</p>
<ul>
    <li>If the target is less than or equal to the current node's value, we move left (because a smaller or equal value might exist in the left subtree).</li>
    <li>If the target is greater than the current node's value, we move right (because any potential ceiling must be in the right subtree).</li>
</ul>
<p>Finally, the smallest node value that was greater than or equal to the target is our answer.</p>

<p><strong>Floor Function (<code>floor</code>):</strong></p>
<p><strong>Goal:</strong> Find the largest value in the BST that is less than or equal to the target value.</p>
<p><strong>Intuition:</strong></p>
<ul>
    <li>Start at the root of the tree.</li>
    <li>If the root’s value is exactly equal to the target, then the root’s value is the floor.</li>
    <li>If the target is less than the root’s value, the floor must be in the left subtree because all values in the right subtree are greater than the root.</li>
    <li>If the target is greater than the root’s value, the root's value could potentially be the floor, but we still need to check the right subtree to see if there's an even larger value that is still less than or equal to the target.</li>
</ul>
<p>As we traverse the tree:</p>
<ul>
    <li>If the target is greater than or equal to the current node's value, we move right (because a larger or equal value might exist in the right subtree).</li>
    <li>If the target is less than the current node's value, we move left (because any potential floor must be in the left subtree).</li>
</ul>
<p>Finally, the largest node value that was less than or equal to the target is our answer.</p>

<p><strong>Code</strong></p>

```python
def ceil(root, target):
    node = root
    ans = -1
    while node:
        if node.data == target:
            ans = node.data
            break
        elif target > node.data:
            node = node.right
        else:
            ans = node.data
            node = node.left
    return ans

def floor(root, target):
    node = root
    ans = -1
    while node:
        if node.data == target:
            ans = node.data
            break
        elif target > node.data:
            ans = node.data
            node = node.right
        else:
            node = node.left
    return ans
```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> The time complexity for both <code>ceil</code> and <code>floor</code> functions is <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is because, in the worst case, you may need to traverse from the root to a leaf node.</li>
    <li><strong>Space Complexity:</strong> The space complexity for both functions is <strong>O(1)</strong> because they only use a constant amount of additional space.</li>
</ul>


<br>
<br>

<h1>Insert Given Node in BST</h1>
<p><strong>Problem Statement</strong></p>
<p>Implement a function <code>insert(root, target)</code> that inserts a target value into a Binary Search Tree (BST). The function should maintain the BST property after insertion.</p>

<p><strong>Sample Test Cases (All Possible)</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [4, 2, 7, 1, 3] , val = 5</li>
            <li><strong>Output:</strong> The tree after insertion:  [4, 2, 7, 1, 3, 5]</li>
            <li><strong>Explanation:</strong> Below is image where the node 5 is inserted</li>
            <img src="https://static.takeuforward.org/content/ProblemSetter-E1RInkjk">
            <li>There is another way to insert the given val as shown below.</li>
            <img src="https://static.takeuforward.org/content/ProblemSetter-d5Zymok1">
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [40, 20, 60, 10, 30, 50, 70] , val = 25</li>
            <li><strong>Output:</strong> The tree after insertion: [40, 20, 60, 10, 25, 50, 70, null, null, null, 30]</li>
            <li><strong>Explanation:</strong> Below is image where the node 25 is inserted</li>
            <img src="https://static.takeuforward.org/content/ProblemSetter-5oXCfvkZ">
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6], target = 1</li>
            <li><strong>Output:</strong> The tree after insertion: [8, 4, 12, 2, 6, 1]</li>
            <li><strong>Explanation:</strong> The value 1 is inserted as the left child of 2, preserving the BST property.</li>
        </ul>
    </li>
</ol>

<p><strong>Approach</strong></p>
<ul>
    <li>Start at the root of the tree.</li>
    <li>If the root is <code>None</code> (i.e., the tree is empty), create a new node with the target value and return it as the new root.</li>
    <li>While traversing the tree:</li>
    <ul>
        <li>If the target value is greater than the current node’s value, move to the right child.</li>
        <li>If the right child is <code>None</code>, insert the target value here.</li>
        <li>If the target value is less than or equal to the current node’s value, move to the left child.</li>
        <li>If the left child is <code>None</code>, insert the target value here.</li>
    </ul>
    <li>Repeat until you find the correct spot for insertion.</li>
</ul>

<p><strong>Intuition</strong></p>
<p>In a Binary Search Tree (BST), the nodes are arranged such that:</p>
<ul>
    <li>The left subtree of a node contains only nodes with values less than the node's value.</li>
    <li>The right subtree of a node contains only nodes with values greater than the node's value.</li>
</ul>
<p>When inserting a new value, you need to maintain this property. Start from the root and move left or right based on whether the target value is smaller or larger than the current node's value. Insert the new node as a leaf when you find an appropriate spot where there is no existing child node in the direction you need to go.</p>

<p><strong>Code</strong></p>

```python
def insert(root, target):
    node = root
    if not node:
        root = Node(target)
        return root
    while True:
        if target > node.data:
            if node.right:
                node = node.right
            else:
                node.right = Node(target)
                break
        else:
            if node.left:
                node = node.left
            else:
                node.left = Node(target)
                break
    return root
```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> The time complexity for the <code>insert</code> function is <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. In the worst case, you may need to traverse from the root to a leaf node, which is proportional to the height of the tree.</li>
    <li><strong>Space Complexity:</strong> The space complexity is <strong>O(1)</strong> because the function only uses a constant amount of additional space beyond the input tree.</li>
</ul>


<br>
<br>

<h1>Delete Given Target Node In BST</h1>
<p><strong>Problem Statement</strong></p>
<p>Implement a function <code>solve(root, target)</code> that deletes a node with the given target value from a Binary Search Tree (BST). The function should maintain the BST property after deletion.</p>

<p><strong>Sample Test Cases (All Possible)</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [5, 3, 6, 2, 4, null, 7] , key = 3</li>
            <li><strong>Output:</strong> The tree after deletion: [5, 4, 6, 2, null, null, 7]</li>
            <li><strong>Explanation:</strong> Below is image of the original BST</li>
            <img src="https://static.takeuforward.org/content/ProblemSetter-PcCLLBxP">
            <li>Below is image where the node 3 is deleted</li>
            <img src="https://static.takeuforward.org/content/ProblemSetter-kSeVvzcS">
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14], target = 10</li>
            <li><strong>Output:</strong> The tree after deletion: [8, 4, 12, 2, 6, 14]</li>
            <li><strong>Explanation:</strong> The node with value 10 is deleted. It has no children, so it is simply removed from the tree.</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14], target = 8</li>
            <li><strong>Output:</strong> The tree after deletion: [10, 4, 12, 2, 6, 14]</li>
            <li><strong>Explanation:</strong> The node with value 8 is deleted. Its right subtree [12, 10, 14] replaces it, with 10 becoming the new root of the subtree.</li>
        </ul>
    </li>
     <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [5, 3, 6, 2, 4, null, 7] , key = 0</li>
            <li><strong>Output:</strong> The tree after deletion: [5, 3, 6, 2, 4, null, 7]</li>
            <li><strong>Explanation:</strong> The tree does not have node with value 0.</li>
        </ul>
    </li>
</ol>

<p><strong>Approach</strong></p>
<ul>
    <li>Find the node with the target value in the BST.</li>
    <li>Use the <code>helper</code> function to handle the deletion, which considers three cases:</li>
    <ul>
        <li>If the node has no left child, return its right child.</li>
        <li>If the node has no right child, return its left child.</li>
        <li>If the node has both children, find the rightmost node in the left subtree (inorder predecessor), attach the right child of the node to this rightmost node, and return the left child of the node.</li>
    </ul>
    <li>Adjust the parent of the node to be deleted to point to the new subtree (if needed).</li>
    <li>Repeat until the target node is found and deleted.</li>
</ul>

<p><strong>Intuition</strong></p>
<p>When deleting a node from a BST, you must maintain the BST property. This involves handling three possible scenarios:</p>
<ul>
    <li>If the node has no children, simply remove it.</li>
    <li>If the node has one child, replace it with its child.</li>
    <li>If the node has two children, find its inorder predecessor (the rightmost node in the left subtree), replace the node with this predecessor, and attach the right subtree of the node to the predecessor.</li>
</ul>
<p>This ensures that the BST property is maintained after the deletion.</p>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Start by checking if the root is <code>None</code>. If so, return <code>None</code> since the tree is empty.</li>
    <li>If the root node's value is the target value, use the <code>helper</code> function to delete this node and return the modified subtree.</li>
    <li>If the root's value is not the target, traverse the tree:</li>
    <ul>
        <li>If the target value is greater than the current node's value, move to the right child and check if the target is present there. If so, use the <code>helper</code> function to delete the node.</li>
        <li>If the target value is less than or equal to the current node's value, move to the left child and check if the target is present there. If so, use the <code>helper</code> function to delete the node.</li>
    </ul>
    <li>Continue this process until the target node is found and deleted.</li>
    <li>Return the root of the modified BST.</li>
</ol>

<img src="https://static.takeuforward.org/premium/Binary%20Search%20Trees/Medium/Delete%20a%20node%20in%20BST/Delete-a-node-in-bst1.drawio.png-Qyl9-7gt">
<img src="https://static.takeuforward.org/premium/Binary%20Search%20Trees/Medium/Delete%20a%20node%20in%20BST/Delete-a-node-in-bst1.drawio.png-Qyl9-7gt">
<img src="https://static.takeuforward.org/premium/Binary%20Search%20Trees/Medium/Delete%20a%20node%20in%20BST/Delete-a-node-in-bst3.drawio.png-GvOdrzFc">
<img src="https://static.takeuforward.org/premium/Binary%20Search%20Trees/Medium/Delete%20a%20node%20in%20BST/Delete-a-node-in-bst4.drawio.png-AKOWkVZ4">
<img src="https://static.takeuforward.org/premium/Binary%20Search%20Trees/Medium/Delete%20a%20node%20in%20BST/Delete-a-node-in-bst5.drawio.png-_Trn-YJf">
<img src="https://static.takeuforward.org/premium/Binary%20Search%20Trees/Medium/Delete%20a%20node%20in%20BST/Delete-a-node-in-bst6.drawio.png-bVYCBKFg">


<p><strong>Code</strong></p>

```python
def helper(node):
    if node.left is None:
        return node.right
    elif node.right is None:
        return node.left
    else:
        rightMost = node.left
        while rightMost.right:
            rightMost = rightMost.right
        rightMost.right = node.right
        return node.left

def solve(root, target):
    if not root:
        return None
    if root.data == target:
        return helper(root)
    node = root
    while node:
        if target > node.data:
            if node.right and node.right.data == target:
                node.right = helper(node.right)
            else:
                node = node.right
        else:
            if node.left and node.left.data == target:
                node.left = helper(node.left)
            else:
                node = node.left
    return root
```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> The time complexity for the <code>solve</code> function is <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. In the worst case, you may need to traverse from the root to a leaf node and handle the deletion.</li>
    <li><strong>Space Complexity:</strong> The space complexity is <strong>O(1)</strong> because the function only uses a constant amount of additional space beyond the input tree.</li>
</ul>


<br>
<br>

<h1>Kth Largest Node IN BST</h1>
<p><strong>Problem Statement</strong></p>
<p>Implement a function <code>smallestBruteForce(root, k)</code> and a function <code>smallestOptimized(root, k)</code> that return the <code>k</code>th smallest element in a Binary Search Tree (BST). Provide solutions for both brute force and optimized approaches.</p>

<p><strong>Sample Test Cases (All Possible)</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14], k = 3</li>
            <li><strong>Output:</strong> 6</li>
            <li><strong>Explanation:</strong> The inorder traversal of the BST is [2, 4, 6, 8, 10, 12, 14]. The 3rd smallest element is 6.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 8
               /   \
              4     12
             / \   /  \
            2   6 10  14
            </pre>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [5, 3, 8, 2, 4, 7, 9], k = 5</li>
            <li><strong>Output:</strong> 7</li>
            <li><strong>Explanation:</strong> The inorder traversal of the BST is [2, 3, 4, 5, 7, 8, 9]. The 5th smallest element is 7.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 5
               /   \
              3     8
             / \   / \
            2   4 7   9
            </pre>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [7, 3, 9, 2, 5, 8, 10], k = 1</li>
            <li><strong>Output:</strong> 2</li>
            <li><strong>Explanation:</strong> The inorder traversal of the BST is [2, 3, 5, 7, 8, 9, 10]. The 1st smallest element is 2.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 7
               /   \
              3     9
             / \   / \
            2   5 8   10
            </pre>
        </ul>
    </li>
</ol>

<p><strong>Brute Force Approach</strong></p>
<p>1. Perform an inorder traversal of the BST to get a sorted list of elements.</p>
<p>2. Access the <code>k</code>th element of the sorted list.</p>
<p>3. Return this element as the result.</p>

<p><strong>Intuition</strong></p>
<p>Inorder traversal of a BST yields elements in ascending order. By traversing the entire tree and collecting elements in a list, you can directly access the <code>k</code>th smallest element from this sorted list.</p>

<p><strong>Code</strong></p>

```python
def inorder(node, arr):
    if not node:
        return
    inorder(node.left, arr)
    arr.append(node.data)
    inorder(node.right, arr)

def smallestBruteForce(root, k):
    ans = None
    if not root:
        return ans
    arr = []
    inorder(root, arr)
    n = len(arr)
    if k > n:
        return ans
    ans = arr[k - 1]
    return ans
```

<p><strong>Time and Space Complexity (Brute Force)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n)</strong>, where <strong>n</strong> is the number of nodes in the tree. This is because the inorder traversal visits every node in the tree.</li>
    <li><strong>Space Complexity:</strong> <strong>O(n)</strong>, as we need to store the elements of the tree in a list.</li>
</ul>

<p><strong>Optimized Approach</strong></p>
<p>1. Perform an inorder traversal of the BST, but stop as soon as you have visited <code>k</code> nodes.</p>
<p>2. Maintain a counter to keep track of the number of nodes visited.</p>
<p>3. When the counter reaches <code>k</code>, return the current node’s value as the result.</p>

<p><strong>Intuition</strong></p>
<p>Instead of traversing the entire tree and sorting all elements, you can stop as soon as you have visited the <code>k</code>th node. This approach is more efficient as it only traverses the minimum number of nodes required to find the <code>k</code>th smallest element.</p>

<p><strong>Code</strong></p>

```python
def inOrder(node, k, count, ans):
    if not node:
        return
    inOrder(node.left, k, count, ans)
    count[0] += 1
    if count[0] == k:
        ans[0] = node.data
        return
    inOrder(node.right, k, count, ans)

def smallestOptimized(root, k):
    ans = [None]
    count = [0]
    inOrder(root, k, count, ans)
    return ans[0]
```

<p><strong>Time and Space Complexity (Optimized)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is because we stop as soon as we have visited <code>k</code> nodes, and the height of the tree is the upper bound on the number of nodes visited.</li>
    <li><strong>Space Complexity:</strong> <strong>O(h)</strong>, due to the recursion stack in the worst case (when the tree is skewed). For a balanced tree, the space complexity is <strong>O(log n)</strong>.</li>
</ul>


<br>
<br>

<h1>Validate Given Binary Tree is BST</h1>
<p><strong>Problem Statement</strong></p>
<p>Implement a function <code>solve(root)</code> that checks whether a given binary tree is a Binary Search Tree (BST). A BST is a binary tree where for every node, the values in the left subtree are less than the node’s value, and the values in the right subtree are greater than the node’s value.</p>

<p><strong>Sample Test Cases (All Possible)</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14]</li>
            <li><strong>Output:</strong> True</li>
            <li><strong>Explanation:</strong> The tree satisfies the BST property for all nodes.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 8
               /   \
              4     12
             / \   /  \
            2   6 10  14
            </pre>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 10, 6, 14]</li>
            <li><strong>Output:</strong> False</li>
            <li><strong>Explanation:</strong> The node with value 10 is in the left subtree of 12, which violates the BST property.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 8
               /   \
              4     12
             / \   /  \
            2  10 6   14
            </pre>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [5, 3, 8, 2, 4, 7, 9]</li>
            <li><strong>Output:</strong> True</li>
            <li><strong>Explanation:</strong> The tree satisfies the BST property for all nodes.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 5
               /   \
              3     8
             / \   / \
            2   4 7   9
            </pre>
        </ul>
    </li>
</ol>

<p><strong>Brute Force Approach</strong></p>
<p>1. Perform an inorder traversal of the BST to get a list of elements in sorted order.</p>
<p>2. Check if this list is sorted in ascending order. If it is, then the tree is a BST; otherwise, it is not.</p>

<p><strong>Intuition</strong></p>
<p>Inorder traversal of a BST yields elements in ascending order. By checking if the inorder traversal list is sorted, you can determine if the tree satisfies the BST property.</p>

<p><strong>Steps to Solve (Brute Force)</strong></p>
<ol>
    <li>Perform an inorder traversal of the tree and store the elements in a list.</li>
    <li>Check if the list is sorted in ascending order.</li>
    <li>Return <code>True</code> if the list is sorted; otherwise, return <code>False</code>.</li>
</ol>

<p><strong>Code (Brute Force)</strong></p>

```python
def inorderTraversal(node, arr):
    if not node:
        return
    inorderTraversal(node.left, arr)
    arr.append(node.data)
    inorderTraversal(node.right, arr)

def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

def solve(root):
    if not root:
        return True
    arr = []
    inorderTraversal(root, arr)
    return isSorted(arr)
```

<p><strong>Time and Space Complexity (Brute Force)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n)</strong>, where <strong>n</strong> is the number of nodes in the tree. This is due to the inorder traversal and checking if the list is sorted.</li>
    <li><strong>Space Complexity:</strong> <strong>O(n)</strong>, as we need to store the elements of the tree in a list.</li>
</ul>

<p><strong>Optimized Approach</strong></p>
<p>1. Use a recursive function to validate each node in the tree by ensuring its value is within the range defined by its ancestors.</p>
<p>2. The left subtree should contain values less than the current node's value, and the right subtree should contain values greater than the current node's value.</p>
<p>3. Return <code>True</code> if all nodes satisfy the BST property; otherwise, return <code>False</code>.</p>

<p><strong>Intuition</strong></p>
<p>A binary tree is a BST if for every node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than the node's value. By recursively checking each node and ensuring it falls within the valid range defined by its ancestors, you can validate whether the entire tree satisfies the BST property.</p>

<p><strong>Steps to Solve (Optimized)</strong></p>
<ol>
    <li>Start with the root node and initialize the valid range as <code>(-∞, ∞)</code>.</li>
    <li>Recursively validate the left child of the node with the updated maximum value (the current node’s value).</li>
    <li>Recursively validate the right child of the node with the updated minimum value (the current node’s value).</li>
    <li>If any node does not satisfy the condition <code>minVal < node.data < maxVal</code>, return <code>False</code>.</li>
    <li>Return <code>True</code> if all nodes satisfy the condition.</li>
</ol>

<p><strong>Code (Optimized)</strong></p>

```python
def validate(node, minVal, maxVal):
    if not node:
        return True
    if not (minVal < node.data < maxVal):
        return False
    left = validate(node.left, minVal, node.data)
    right = validate(node.right, node.data, maxVal)
    return left and right

def solve(root):
    if not root:
        return True
    ans = validate(root, float('-inf'), float('inf'))
    return ans
```

<p><strong>Time and Space Complexity (Optimized)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n)</strong>, where <strong>n</strong> is the number of nodes in the tree. Each node is visited once.</li>
    <li><strong>Space Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is due to the recursion stack in the worst case (when the tree is skewed). For a balanced tree, the space complexity is <strong>O(log n)</strong>.</li>
</ul>


<br>
<br>

<h1>Lowest Common Ancester (LCA)</h1>
<p><strong>Problem Statement</strong></p>
<p>Implement a function <code>solve(root, node1, node2)</code> to find the Lowest Common Ancestor (LCA) of two given nodes (<code>node1</code> and <code>node2</code>) in a Binary Search Tree (BST). The LCA of two nodes is defined as the deepest node that is an ancestor of both nodes.</p>

<p><strong>Sample Test Cases</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14], node1 = 2, node2 = 6</li>
            <li><strong>Output:</strong> 4</li>
            <li><strong>Explanation:</strong> The LCA of nodes 2 and 6 is 4.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 8
               /   \
              4     12
             / \   /  \
            2   6 10  14
            </pre>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [8, 4, 12, 2, 6, 10, 14], node1 = 10, node2 = 14</li>
            <li><strong>Output:</strong> 12</li>
            <li><strong>Explanation:</strong> The LCA of nodes 10 and 14 is 12.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 8
               /   \
              4     12
             / \   /  \
            2   6 10  14
            </pre>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> root = [5, 3, 8, 2, 4, 7, 9], node1 = 2, node2 = 9</li>
            <li><strong>Output:</strong> 5</li>
            <li><strong>Explanation:</strong> The LCA of nodes 2 and 9 is 5.</li>
            <li><strong>Tree Structure:</strong></li>
            <pre>
                 5
               /   \
              3     8
             / \   / \
            2   4 7   9
            </pre>
        </ul>
    </li>
</ol>

<p><strong>Brute Force Approach</strong></p>
<p>1. Perform a traversal of the tree to find the path from the root to <code>node1</code> and the path from the root to <code>node2</code>.</p>
<p>2. Store the path to each node in separate lists.</p>
<p>3. Compare the two lists to find the common nodes and determine the deepest common node which will be the LCA.</p>

<p><strong>Intuition</strong></p>
<p>By finding and comparing the paths from the root to each of the nodes, you can identify where the paths diverge, which helps in determining the deepest common ancestor.</p>

<p><strong>Steps to Solve (Brute Force)</strong></p>
<ol>
    <li>Find the path from the root to <code>node1</code> and store it in a list.</li>
    <li>Find the path from the root to <code>node2</code> and store it in another list.</li>
    <li>Compare the two lists to find the common elements and determine the last common element.</li>
    <li>Return this common element as the LCA.</li>
</ol>

<p><strong>Code (Brute Force)</strong></p>

```python
def findPath(root, node, path):
    if not root:
        return False
    path.append(root.data)
    if root.data == node.data:
        return True
    if ((root.left and findPath(root.left, node, path)) or
        (root.right and findPath(root.right, node, path))):
        return True
    path.pop()
    return False

def lcaBruteForce(root, node1, node2):
    path1 = []
    path2 = []
    if (not findPath(root, node1, path1) or
        not findPath(root, node2, path2)):
        return None
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1] if i > 0 else None

def solve(root, node1, node2):
    if not root:
        return None
    ans = lcaBruteForce(root, node1, node2)
    return ans
```

<p><strong>Time and Space Complexity (Brute Force)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n)</strong>, where <strong>n</strong> is the number of nodes in the tree. This is because finding paths to each node requires traversing the tree.</li>
    <li><strong>Space Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is due to the space used to store the paths in lists.</li>
</ul>

<p><strong>Optimized Approach</strong></p>
<p>1. Use the properties of a Binary Search Tree (BST) to determine the LCA efficiently without storing paths.</p>
<p>2. Compare the values of the nodes to determine whether to move left or right in the tree.</p>
<p>3. Return the node where the paths to <code>node1</code> and <code>node2</code> diverge.</p>

<p><strong>Intuition</strong></p>
<p>In a BST, the LCA is the first node where the values of the two nodes being searched are on different sides of the current node. This property allows for a more efficient solution compared to the brute force approach.</p>

<p><strong>Steps to Solve (Optimized)</strong></p>
<ol>
    <li>Start from the root node.</li>
    <li>If both <code>node1</code> and <code>node2</code> are smaller than the current node, move to the left subtree.</li>
    <li>If both <code>node1</code> and <code>node2</code> are larger than the current node, move to the right subtree.</li>
    <li>If one of <code>node1</code> or <code>node2</code> is smaller and the other is larger, the current node is the LCA.</li>
    <li>Return the data of the LCA node.</li>
</ol>

<p><strong>Recursion Flow for Optimized Approach</strong></p>
<p>Consider the following BST:</p>
<pre>
     8
   /   \
  4     12
 / \   / \
2   6 10  14
</pre>
<p>Let's find the LCA of nodes 2 and 6:</p>
<ul>
    <li>Start at the root (8).</li>
    <pre>
         8
       /   \
      4     12
     / \   / \
    2   6 10  14
    </pre>
    <li>Both 2 and 6 are smaller than 8, so move to the left subtree.</li>
    <pre>
         8
       /   
      4     
     / \   
    2   6 
    </pre>
    <li>Current node is 4.</li>
    <li>Both 2 and 6 are not smaller than 4, so 4 is the LCA.</li>
</ul>

<p>Now, let's find the LCA of nodes 10 and 14:</p>
<ul>
    <li>Start at the root (8).</li>
    <pre>
         8
       /   \
      4     12
           / \
          10  14
    </pre>
    <li>Both 10 and 14 are larger than 8, so move to the right subtree.</li>
    <pre>
         12
       / \
      10  14
    </pre>
    <li>Current node is 12.</li>
    <li>Both 10 and 14 are not larger than 12, so 12 is the LCA.</li>
</ul>

<p><strong>Code (Optimized)</strong></p>

```python
def lca(node, node1, node2):
    if not node:
        return None
    current = node.data
    if current > node1.data and current > node2.data:
        return lca(node.left, node1, node2)
    elif current < node1.data and current < node2.data:
        return lca(node.right, node1, node2)
    else:
        return node

def solve(root, node1, node2):
    if not root:
        return None
    ans = lca(root, node1, node2)
    return ans.data
```

<p><strong>Time and Space Complexity (Optimized)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is because, in the worst case, we might traverse from the root to the leaf node.</li>
    <li><strong>Space Complexity:</strong> <strong>O(1)</strong>, as we are only using a constant amount of extra space apart from the input tree.</li>
</ul>


<br>
<br>

<h1>Construct BST Using Preorder</h1>
<p><strong>Problem Statement</strong></p>
<p>Given a preorder traversal of a binary search tree (BST), construct the BST.</p>

<p><strong>Sample Test Cases</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> preorder = [10, 5, 1, 7, 40, 50]</li>
            <li><strong>Output:</strong> The BST constructed from this preorder traversal is:</li>
            <pre>
                 10
               /    \
              5     40
             / \      \
            1   7     50
            </pre>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> preorder = [8, 5, 1, 7, 10, 12]</li>
            <li><strong>Output:</strong> The BST constructed from this preorder traversal is:</li>
            <pre>
                 8
               /   \
              5    10
             / \     \
            1   7    12
            </pre>
        </ul>
    </li>
</ol>

<p><strong>Brute Force Approach</strong></p>
<p>1. To construct the BST from the preorder traversal, we first need to sort the preorder list to get the inorder traversal of the BST.</p>
<p>2. Use the sorted preorder list as the inorder traversal and then use the given preorder list to construct the tree using the <code>buildTree</code> function.</p>

<p><strong>Intuition</strong></p>
<p>Sorting the preorder list gives us the inorder traversal. With the inorder traversal and preorder traversal, we can reconstruct the BST by recursively determining the root and left and right subtrees.</p>

<p><strong>Steps to Solve (Brute Force)</strong></p>
<ol>
    <li>Sort the preorder list to get the inorder list.</li>
    <li>Use the inorder and preorder lists to reconstruct the BST using the <code>buildTree</code> function.</li>
    <li>Return the constructed BST.</li>
</ol>

<p><strong>Recursion Flow (Brute Force)</strong></p>
<p>Consider the following preorder traversal:</p>
<pre>
    [10, 5, 1, 7, 40, 50]
</pre>
<p>We build the tree as follows:</p>
<ul>
    <li>Sort the preorder list to get the inorder list:</li>
    <pre>
        inorder = [1, 5, 7, 10, 40, 50]
    </pre>
    <li>Construct the tree using <code>buildTree</code>:</li>
    <ul>
        <li>Start with root = 10 (first element in preorder).</li>
        <pre>
             10
        </pre>
        <li>Build left subtree of 10:</li>
        <ul>
            <li>Root of left subtree = 5 (next element in preorder).</li>
            <pre>
                 10
                /
               5
            </pre>
            <li>Build left subtree of 5:</li>
            <ul>
                <li>Root of left subtree = 1 (next element in preorder).</li>
                <pre>
                 10
                /
               5
              /
             1
                </pre>
            </ul>
            <li>Build right subtree of 5:</li>
            <ul>
                <li>Root of right subtree = 7 (next element in preorder).</li>
                <pre>
                 10
                /
               5
              / \
             1   7
                </pre>
            </ul>
        </ul>
        <li>Build right subtree of 10:</li>
        <ul>
            <li>Root of right subtree = 40 (next element in preorder).</li>
            <pre>
                 10
                /  \
               5   40
              / \
             1   7
            </pre>
            <li>Build right subtree of 40:</li>
            <ul>
                <li>Root of right subtree = 50 (next element in preorder).</li>
                <pre>
                 10
                /  \
               5   40
              / \    \
             1   7   50
                </pre>
            </ul>
        </ul>
    </ul>
</p>

<p><strong>Code (Brute Force)</strong></p>

```python
def buildTree(preOrder, preStart, preEnd, inOrder, inStart, inEnd, index):
    if preStart > preEnd or inStart > inEnd:
        return None
    root = Node(preOrder[preStart])
    inRoot = index[preOrder[preStart]]
    numsLeft = inRoot - inStart
    root.left = buildTree(preOrder, preStart + 1, preStart + numsLeft, inOrder, inStart, inRoot - 1, index)
    root.right = buildTree(preOrder, preStart + numsLeft + 1, preEnd, inOrder, inRoot + 1, inEnd, index)
    return root

def solve(n, inorder, preorder):
    root = None
    if n == 0:
        return root
    index = {}
    for i in range(n):
        index[inorder[i]] = i
    preStart, preEnd = 0, n - 1
    inStart, inEnd = 0, n - 1
    root = buildTree(preorder, preStart, preEnd, inorder, inStart, inEnd, index)
    return root

def bruteForce(preorder):
    if not preorder:
        return None
    inorder = sorted(preorder)
    n = len(preorder)
    root = solve(n, inorder, preorder)
    return root
```

<p><strong>Time and Space Complexity (Brute Force)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n log n)</strong> for sorting the preorder list, and <strong>O(n)</strong> for constructing the tree, resulting in a total of <strong>O(n log n)</strong>.</li>
    <li><strong>Space Complexity:</strong> <strong>O(n)</strong> for storing the inorder list and recursion stack.</li>
</ul>

<p><strong>Optimized Approach</strong></p>
<p>1. Construct the BST directly from the preorder traversal using a helper function that maintains a range for valid node values.</p>
<p>2. Use the preorder list to create nodes and adjust the range for each subtree accordingly.</p>

<p><strong>Intuition</strong></p>
<p>In a BST, the first element of preorder traversal is always the root. Using this property, we can recursively construct the left and right subtrees by adjusting the valid range for the node values.</p>

<p><strong>Steps to Solve (Optimized)</strong></p>
<ol>
    <li>Initialize the index to track the current position in the preorder list.</li>
    <li>Use the helper function to construct the tree by recursively creating nodes and adjusting the valid range for each node.</li>
    <li>Return the root of the constructed BST.</li>
</ol>

<p><strong>Recursion Flow (Optimized Approach)</strong></p>
<p>Consider the following preorder traversal:</p>
<pre>
    [10, 5, 1, 7, 40, 50]
</pre>
<p>We build the tree as follows:</p>
<ul>
    <li>Start with the first element 10 as the root.</li>
    <pre>
         10
    </pre>
    <li>Next element 5 is smaller than 10, so it goes to the left subtree of 10.</li>
    <pre>
         10
        /
       5
    </pre>
    <li>Next element 1 is smaller than 5, so it goes to the left subtree of 5.</li>
    <pre>
         10
        /
       5
      /
     1
    </pre>
    <li>Next element 7 is greater than 5 but less than 10, so it goes to the right subtree of 5.</li>
    <pre>
         10
        /
       5
      / \
     1   7
    </pre>
    <li>Next element 40 is greater than 10, so it goes to the right subtree of 10.</li>
    <pre>
         10
        /  \
       5   40
      / \
     1   7
    </pre>
    <li>Finally, element 50 is greater than 40, so it goes to the right subtree of 40.</li>
    <pre>
         10
        /  \
       5   40
      / \    \
     1   7   50
    </pre>
</ul>

<p><strong>Code (Optimized)</strong></p>

```python
def build(preorder, index, maxVal):
    if index[0] >= len(preorder) or preorder[index[0]] > maxVal:
        return None
    node = Node(preorder[index[0]])
    index[0] += 1
    node.left = build(preorder, index, node.data)
    node.right = build(preorder, index, maxVal)
    return node

def optimized(preorder):
    if not preorder:
        return None
    index = [0]
    root = build(preorder, index, float('inf'))
    return root
```

<p><strong>Time and Space Complexity (Optimized)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n)</strong>, where <strong>n</strong> is the number of nodes. Each node is processed once.</li>
    <li><strong>Space Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is due to the recursion stack.</li>
</ul>


<br>
<br>

<h1>Find Successer Of Given Val In Inorder Traversal</h1>
<p><strong>Problem Statement</strong></p>
<p>Given a BST and a value <code>k</code>, find the successor of <code>k</code> in the inorder traversal of the BST. The successor is the smallest value in the BST that is greater than <code>k</code>.</p>

<p><strong>Sample Test Cases</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> root = [10, 5, 1, 7, 40, 50], k = 7</li>
            <li><strong>Output:</strong> 10</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> root = [20, 10, 5, 15, 30, 25, 35], k = 25</li>
            <li><strong>Output:</strong> 30</li>
        </ul>
    </li>
</ol>

<p><strong>Brute Force Approach</strong></p>
<p>The brute force approach involves performing an inorder traversal of the BST, storing the elements in a list, and then finding the successor using binary search.</p>

<p><strong>Intuition</strong></p>
<p>Inorder traversal of a BST gives us the nodes in sorted order. By finding the position of <code>k</code> in this sorted list, we can determine the successor.</p>

<p><strong>Steps to Solve (Brute Force)</strong></p>
<ol>
    <li>Perform an inorder traversal of the BST and store the elements in a list.</li>
    <li>Use binary search to find the smallest element in the list that is greater than <code>k</code>.</li>
    <li>Return the found element as the successor or <code>-1</code> if no such element exists.</li>
</ol>

<p><strong>Recursion Flow (Brute Force)</strong></p>
<p>Consider the following BST:</p>
<pre>
    10
   /  \
  5   40
 / \    \
1   7   50
</pre>
<p>To find the successor of <code>7</code>:</p>
<ul>
    <li>Perform inorder traversal to get: [1, 5, 7, 10, 40, 50]</li>
    <li>Binary search to find the smallest element greater than 7 results in index 3 with value 10.</li>
</ul>

<p><strong>Code (Brute Force)</strong></p>

```python
def inorder(node, arr):
    if not node:
        return
    inorder(node.left, arr)
    arr.append(node.data)
    inorder(node.right, arr)

def findUpperBound(n, arr, k):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def bruteforce(root, k):
    ans = None
    if not root:
        return ans
    arr = []
    inorder(root, arr)
    n = len(arr)
    index = findUpperBound(n, arr, k)
    if index == n:
        return -1
    ans = arr[index]
    return ans
```

<p><strong>Time and Space Complexity (Brute Force)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n log n)</strong> for inorder traversal and binary search, where <strong>n</strong> is the number of nodes.</li>
    <li><strong>Space Complexity:</strong> <strong>O(n)</strong> for storing the inorder traversal in a list.</li>
</ul>

<p><strong>Optimized Approach</strong></p>
<p>The optimized approach involves traversing the BST to find the successor directly without constructing an additional list.</p>

<p><strong>Intuition</strong></p>
<p>Using properties of BSTs, we can find the successor by traversing the tree. If <code>k</code> is less than the current node's data, the successor is in the left subtree. Otherwise, it is in the right subtree or the parent nodes.</p>

<p><strong>Steps to Solve (Optimized)</strong></p>
<ol>
    <li>Start at the root and traverse the BST.</li>
    <li>If <code>k</code> is less than the current node's data, move to the left subtree and update the successor.</li>
    <li>If <code>k</code> is greater than or equal to the current node's data, move to the right subtree.</li>
    <li>Continue until you have traversed the BST or found the successor.</li>
</ol>

<p><strong>Recursion Flow (Optimized Approach)</strong></p>
<p>Consider the following BST:</p>
<pre>
    10
   /  \
  5   40
 / \    \
1   7   50
</pre>
<p>To find the successor of <code>7</code>:</p>
<ul>
    <li>Start at root 10:</li>
    <pre>
         10
        /  \
       5   40
      / \    \
     1   7   50
    </pre>
    <li>Since 7 < 10, update successor to 10 and move to the left subtree:</li>
    <pre>
         10
        /  
       5   
      / \  
     1   7
    </pre>
    <li>Since 7 is the right child of 5 and there is no right subtree, the traversal ends with 10 as the successor.</li></ul>

<p><strong>Code (Optimized)</strong></p>

```python
def optimized(root, k):
    ans = None
    if not root:
        return ans
    node = root
    while node:
        if k >= node.data:
            node = node.right
        else:
            ans = node.data
            node = node.left
    if not ans:
        return -1
    return ans
```

<p><strong>Time and Space Complexity (Optimized)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree, as each node is visited once.</li>
    <li><strong>Space Complexity:</strong> <strong>O(1)</strong>, as no additional space is used apart from a few variables.</li>
</ul>


<br>
<br>

<h1>BST Iterator</h1>

<p><strong>Problem Statement</strong></p>
<p>Implement an iterator for a Binary Search Tree (BST) that performs in-order traversal. The iterator should provide the following functionalities:</p>
<ul>
    <li><strong>hasNext:</strong> Returns <code>true</code> if there are more elements in the BST to iterate over.</li>
    <li><strong>next:</strong> Returns the next element in the in-order traversal of the BST.</li>
</ul>

<p><strong>Intuition</strong></p>
<p>In-order traversal of a BST visits nodes in ascending order. To efficiently implement an iterator for this traversal, we use a stack to keep track of nodes. The stack helps us traverse the tree while maintaining the order of nodes to visit:</p>
<ul>
    <li>Initially, push all left children of the root onto the stack. This ensures that we start with the smallest node.</li>
    <li>When calling <code>next</code>, pop the top node from the stack. This node is guaranteed to be the next node in the in-order traversal.</li>
    <li>After popping a node, push all left children of its right child onto the stack. This step maintains the order of traversal by preparing the next set of nodes to visit.</li>
    <li>Repeat the process until all nodes are visited.</li>
</ul>

<p><strong>Code Explanation</strong></p>
<ul>
    <li><strong>Node Class:</strong> Represents a node in the BST. Each node has data, a left child, and a right child.</li>
    <li><strong>Iterator Class:</strong> Implements the iterator for in-order traversal.</li>
    <ul>
        <li><strong>__init__:</strong> Initializes the iterator with the root of the BST and pushes all left nodes onto the stack.</li>
        <li><strong>pushAllLeft:</strong> Pushes all left children of the given node onto the stack.</li>
        <li><strong>hasNext:</strong> Checks if there are more nodes to visit in the BST.</li>
        <li><strong>next:</strong> Pops the top node from the stack, pushes all left children of its right child, and returns the node's data.</li>
    </ul>
</ul>

<p><strong>Code</strong></p>

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Iterator:
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.pushAllLeft(root)

    def pushAllLeft(self, root):
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return len(self.stack) != 0

    def next(self):
        top = self.stack.pop()
        self.pushAllLeft(top.right)
        return top.data

# Example usage
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(10)

iterable = Iterator(root)
print(iterable.next())  # 2
print(iterable.next())  # 3
print(iterable.next())  # 4
print(iterable.next())  # 5
print(iterable.hasNext())  # True
print(iterable.next())  # 6
print(iterable.next())  # 8
print(iterable.next())  # 10
print(iterable.hasNext())  # False
```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(1)</strong> for <code>hasNext</code> and <code>next</code> methods on average, as each node is pushed and popped from the stack exactly once.</li>
    <li><strong>Space Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree, due to the stack storing nodes on the path from the root to the current node.</li>
</ul>

<br>
<br>

<h1>Two Sum</h1>
<p><strong>Problem Statement</strong></p>
<p>Given a Binary Search Tree (BST) and an integer <code>target</code>, determine if there exist two distinct nodes in the BST whose values sum up to <code>target</code>.</p>

<p><strong>Sample Test Cases (All Possible) With Tree Structure</strong></p>
<ul>
    <li>
        <strong>Example 1:</strong>
        <pre>
        Input: 
            5
           / \
          3   8
         / \ / \
        2  4 6 10
        
        Target: 11
        
        Output: True (Nodes 5 and 6 sum up to 11)
        </pre>
    </li>
    <li>
        <strong>Example 2:</strong>
        <pre>
        Input: 
            5
           / \
          3   8
         / \   \
        2  4   10
        
        Target: 15
        
        Output: True (Nodes 5 and 10 sum up to 15)
        </pre>
    </li>
    <li>
        <strong>Example 3:</strong>
        <pre>
        Input: 
            5
           / \
          3   8
         / \   \
        2  4   9
        
        Target: 20
        
        Output: False (No two nodes sum up to 20)
        </pre>
    </li>
</ul>

<p><strong>Approach</strong></p>
<p>Use two iterators to traverse the BST:</p>
<ul>
    <li><strong>Iterator:</strong> Traverse the BST in ascending order.</li>
    <li><strong>ReverseIterator:</strong> Traverse the BST in descending order.</li>
</ul>
<p>Check pairs of values from these iterators to see if their sum equals the target. Adjust the iterators based on whether the sum is less than or greater than the target.</p>

<p><strong>Intuition</strong></p>
<p>The solution leverages the properties of BST to efficiently find two numbers that sum up to the target:</p>
<ul>
    <li>One iterator starts from the smallest value and moves right (ascending).</li>
    <li>Another iterator starts from the largest value and moves left (descending).</li>
    <li>By moving the iterators towards each other, you can find pairs of values that sum up to the target without checking every possible pair.</li>
</ul>

<p><strong>Steps To Solve</strong></p>
<ol>
    <li>Initialize two iterators: one for in-order traversal (ascending) and one for reverse in-order traversal (descending).</li>
    <li>Start both iterators at the beginning of their respective traversals.</li>
    <li>While the left iterator's value is less than the right iterator's value:</li>
        <ul>
            <li>Calculate the sum of the values pointed to by both iterators.</li>
            <li>If the sum equals the target, return <code>true</code>.</li>
            <li>If the sum is less than the target, advance the left iterator to get a larger value.</li>
            <li>If the sum is greater than the target, advance the right iterator to get a smaller value.</li>
        </ul>
    <li>If the loop ends without finding the target, return <code>false</code>.</li>
</ol>

<p><strong>Code</strong></p>

```python
class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

class ReverseIterator:
  def __init__(self, root):
      self.root = root
      self.stack = []
      self.pushAllRight(root)

  def pushAllRight(self, root):
      node = root
      while node:
          self.stack.append(node)
          node = node.right

  def hasNext(self):
      return len(self.stack) != 0

  def next(self):
      top = self.stack.pop()
      self.pushAllRight(top.left)
      return top.data

class Iterator:
  def __init__(self, root):
      self.root = root
      self.stack = []
      self.pushAllLeft(root)

  def pushAllLeft(self, root):
      node = root
      while node:
          self.stack.append(node)
          node = node.left

  def hasNext(self):
      return len(self.stack) != 0

  def next(self):
      top = self.stack.pop()
      self.pushAllLeft(top.right)
      return top.data

def solve(root, target):
  if not root:
      return False
  left = Iterator(root)
  right = ReverseIterator(root)
  l, r = left.next(), right.next()
  while l < r:
      if l + r == target:
          return True
      elif l + r < target:
          l = left.next()
      else:
          r = right.next()
  return False

```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n)</strong> in the worst case, where <strong>n</strong> is the number of nodes in the BST. Each node is pushed and popped from the stack exactly once.</li>
    <li><strong>Space Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is due to the space required for the stacks used by the iterators.</li>
</ul>

<br>
<br>

<h1>Recover BST From Swapped Elements</h1>
<p><strong>Problem Statement</strong></p>
<p>Given a Binary Search Tree (BST) where two nodes have been swapped, recover the BST to restore its original properties. The goal is to identify the two swapped nodes and correct the BST.</p>

<p><strong>Sample Test Cases</strong></p>
<ol>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> Tree before correction:
                <pre>
                    10
                   /  \
                 40   50
                / \
               5   7
                </pre>
            </li>
            <li><strong>Output:</strong> Corrected Tree:
                <pre>
                    10
                   /  \
                  5   50
                 / \
                7   40
                </pre>
            </li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> Tree before correction:
                <pre>
                    20
                   /  \
                 10   30
                / \   / \
               5  15 25  35
                </pre>
            </li>
            <li><strong>Output:</strong> Corrected Tree:
                <pre>
                    20
                   /  \
                 10   30
                / \   / \
               5  15 25  35
                </pre>
            </li>
        </ul>
    </li>
</ol>

<p><strong>Brute Force Approach</strong></p>

<p><strong>Approach</strong></p>
<ul>
    <li>Perform an in-order traversal of the BST to gather the node values into an array.</li>
    <li>Sort this array to get the correct in-order sequence of the BST.</li>
    <li>Traverse the BST again using in-order traversal, comparing each node's value with the corresponding value in the sorted array.</li>
    <li>When a mismatch is found between a node's value and the value from the sorted array, update the BST node with the correct value from the sorted array.</li>
    <li>Return the modified BST.</li>
</ul>

<p><strong>Intuition</strong></p>
<p>To fix a BST with two swapped nodes, the key is to recognize that an in-order traversal of a BST yields a sorted sequence. First, collect the node values using an in-order traversal, which will provide an array of values. Sorting this array reveals what the in-order sequence should be if the BST were correct. By comparing the BST's actual in-order traversal with this sorted array, it's possible to identify where the nodes are out of order. The task then is to correct these discrepancies by updating the BST nodes with the appropriate values from the sorted array, thereby restoring the BST's correct structure without altering its overall form.</p>

<p><strong>Steps to Solve (Brute Force)</strong></p>
<ol>
    <li>Perform an in-order traversal of the BST and store the node values in an array.</li>
    <li>Sort this array to obtain the correct in-order sequence.</li>
    <li>Traverse the BST again and update each node's value with the corresponding value from the sorted array if there is a mismatch.</li>
</ol>

<p><strong>Code (Brute Force Approach)</strong></p>

```python
def inorder(node, arr):
    if not node:
        return
    inorder(node.left, arr)
    arr.append(node.data)
    inorder(node.right, arr)

def findUpperBound(n, arr, k):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def bruteForce(root, k):
    ans = None
    if not root:
        return ans
    arr = []
    inorder(root, arr)
    n = len(arr)
    index = findUpperBound(n, arr, k)
    if index == n:
        return -1
    ans = arr[index]
    return ans
```

<p><strong>Time and Space Complexity (Brute Force)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n log n)</strong>, where <strong>n</strong> is the number of nodes in the tree. This is due to the sorting operation.</li>
    <li><strong>Space Complexity:</strong> <strong>O(n)</strong>, for storing the node values in an array.</li>
</ul>

<p><strong>Optimized Approach</strong></p>

<p><strong>Approach</strong></p>
<ul>
    <li>Perform an in-order traversal while tracking the previous node.</li>
    <li>Detect the two nodes where the BST order is violated.</li>
    <li>Identify the exact swapped nodes based on detected violations.</li>
    <li>Swap the values of the identified nodes to correct the BST.</li>
    <li>Return the corrected BST.</li>
</ul>

<p><strong>Intuition</strong></p>
<p>When two nodes are swapped in a BST, the in-order traversal of the BST will have discrepancies. By performing an in-order traversal, you can identify these discrepancies. The nodes where the violations occur are the swapped nodes. Correcting the BST involves identifying these nodes and swapping their values back to restore the BST properties.</p>

<p><strong>Steps to Solve (Optimized)</strong></p>
<ol>
    <li>Perform an in-order traversal of the BST while maintaining the previous node's reference.</li>
    <li>Detect the nodes where the BST property is violated (i.e., nodes where the previous node's value is greater than the current node's value).</li>
    <li>Identify the two swapped nodes by examining where the discrepancies occur.</li>
    <li>Swap the values of the identified nodes to restore the BST properties.</li>
</ol>

<p><strong>Recursion Flow (Optimized)</strong></p>
<p>Consider the following BST where nodes 5 and 40 are swapped:</p>
<pre>
    10
   /  \
  40   50
 / \
5   7
</pre>
<p>To recover the BST:</p>
<ul>
    <li><strong>Start at the root (10):</strong> Move to the left child (40).</li>
    <li><strong>From 40, move to its left child (5):</strong> Visit 5, then move to 7. Since 7 is greater than 10, no issue here.</li>
    <li><strong>Return to 10:</strong> Detect that 40 (left child) is greater than 10 (current node). This is the first violation.</li>
    <li><strong>Move to the right child of 10 (50):</strong> Check the second violation where 7 is less than 40 (previous node).</li>
    <li><strong>Identify swapped nodes:</strong> Nodes 5 and 40 are swapped. Swap these values to correct the BST:</li>
    <pre>
        Corrected BST:
            10
           /  \
          5   50
         / \
        7  40
    </pre>
</ul>

<p><strong>Purpose of the Three Variables in <code>swapped</code></strong></p>
<ul>
    <li><strong>First Swapped Node (<code>swapped[0]</code>):</strong>
        <p>This variable holds the first node that is identified as being out of order. This node is typically the node that should have a larger value but is found to have a smaller value in comparison to its successor. This node is detected when a previous node's value is greater than the current node's value during the in-order traversal.</p>
    </li>
    <li><strong>Second Swapped Node (<code>swapped[1]</code>):</strong>
        <p>This variable holds the second node that is identified as being out of order. This node is typically the node that should have a smaller value but is found to have a larger value. This node is detected when a subsequent node's value is smaller than the current node's value during the in-order traversal.</p>
    </li>
    <li><strong>Third Swapped Node (<code>swapped[2]</code>):</strong>
        <p>This variable is used to handle cases where the swapped nodes are not adjacent in the in-order traversal. If the first out-of-order pair is detected and then another out-of-order pair is found later in the traversal, this variable will hold the second node in the later pair. This allows the algorithm to correctly identify and swap both nodes in cases where the swapped nodes are not immediately adjacent to each other.</p>
    </li>
</ul>

<p><strong>Explanation</strong></p>
<ul>
    <li><strong>Handling Adjacent Nodes:</strong>
        <p>If the two swapped nodes are adjacent in the in-order traversal (e.g., nodes <code>5</code> and <code>40</code> in an incorrect BST), the <code>swapped[0]</code> and <code>swapped[1]</code> variables will be sufficient. The first variable (<code>swapped[0]</code>) will hold the node that is incorrectly placed, and the second variable (<code>swapped[1]</code>) will be the node that follows it in the traversal.</p>
    </li>
    <li><strong>Handling Non-Adjacent Nodes:</strong>
        <p>If the swapped nodes are not adjacent (e.g., nodes <code>5</code> and <code>50</code>), the <code>swapped[2]</code> variable will be used to correctly identify the second out-of-order node. In this case, <code>swapped[0]</code> and <code>swapped[2]</code> will represent the two nodes that need to be swapped to correct the BST.</p>
    </li>
</ul>

<p><strong>Example</strong></p>
<p>Consider the following tree where nodes <code>5</code> and <code>40</code> are swapped:</p>
<pre>
    10
   /  \
  40   50
 / \
5   7
</pre>
<p>During the in-order traversal:</p>
<ol>
    <li><strong>First Violation:</strong> When visiting node <code>40</code> (first out-of-order node), <code>5</code> is found to be less than <code>40</code>, so <code>swapped[0]</code> is set to <code>40</code> and <code>swapped[1]</code> is set to <code>5</code>.</li>
    <li><strong>Second Violation:</strong> As we continue traversing, another violation occurs when visiting <code>50</code> (next node after <code>7</code>), indicating <code>50</code> should be swapped with <code>40</code> (already noted). Here, <code>swapped[2]</code> is set to <code>50</code>.</li>
</ol>
<p>The final correction involves swapping the values in <code>swapped[0]</code> and <code>swapped[2]</code>, i.e., <code>40</code> and <code>50</code>.</p>

<p><strong>Summary</strong></p>
<p>The three variables in the <code>swapped</code> array ensure that both adjacent and non-adjacent swapped nodes can be correctly identified and corrected, making the algorithm robust for various cases of BST node swapping.</p>


<p><strong>Code (Optimized Approach)</strong></p>

```python
def inorder(node, prev, swapped):
    if not node:
        return None
    inorder(node.left, prev, swapped)
    if prev[0] and node.data < prev[0].data:
        if swapped[0] is None:
            swapped[0] = prev[0]
            swapped[1] = node
        else:
            swapped[2] = node
    prev[0] = node
    inorder(node.right, prev, swapped)

def solve(root):
    if not root:
        return None
    swapped = [None, None, None]
    prev = [None]
    inorder(root, prev, swapped)
    if swapped[0] and swapped[2]:
        swapped[0].data, swapped[2].data = swapped[2].data, swapped[0].data
    else:
        swapped[0].data, swapped[1].data = swapped[1].data, swapped[0].data
    return root
```
<p><strong>Time and Space Complexity (Optimized)</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n)</strong>, where <strong>n</strong> is the number of nodes in the tree. This is because each node is visited once during the in-order traversal.</li>
    <li><strong>Space Complexity:</strong> <strong>O(h)</strong>, where <strong>h</strong> is the height of the tree. This is due to the recursion stack used during the in-order traversal.</li>
</ul>



<br>
<br>

<h1>Largest BST in Given Binary Tree</h1>
<p><strong>Problem Statement:</strong> Given a binary tree, you need to find the size of the largest subtree which is a BST.</p>

<p><strong>Sample Test Cases</strong></p>

<ol>
    <li>
        <p><strong>Sample Test Case 1</strong></p>
        <p><strong>Input:</strong></p>
        <pre>
            10
           /  \
          5    15
         / \     \
        1   8     7
        </pre>
        <p><strong>Output:</strong> 3 (The largest BST is the subtree with root 5, which contains nodes 5, 1, and 8)</p>
    </li>
    <li>
        <p><strong>Sample Test Case 2</strong></p>
        <p><strong>Input:</strong></p>
        <pre>
            10
           /  \
          5    15
         / \     \
        1   3     7
        </pre>
        <p><strong>Output:</strong> 2 (The largest BST is the subtree with root 15, which contains nodes 15 and 7)</p>
    </li>
</ol>

<p><strong>Brute Force Approach</strong></p>

<p><strong>Intuition:</strong> To determine if a subtree is a BST and calculate its size, you need to check all possible subtrees. This involves a lot of redundant checks and comparisons.</p>

<p><strong>Steps to Solve:</strong></p>
<ul>
    <li>For each node in the tree, consider it as the root of a subtree.</li>
    <li>Check if this subtree is a BST.</li>
    <li>If it is a BST, calculate the size of this subtree.</li>
    <li>Track the maximum size among all BSTs found.</li>
</ul>

<p><strong>Recursion Flow with Tree Structure:</strong></p>
<ul>
    <li>Traverse all nodes.</li>
    <li>For each node, check if its left and right subtrees are BSTs and if the current node fits the BST property.</li>
    <li>Return the size of the largest BST.</li>
</ul>

<p><strong>Code:</strong></p>

```python
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def is_bst(node, min_val, max_val):
  if not node:
      return True, 0
  if node.val <= min_val or node.val >= max_val:
      return False, 0
  left_is_bst, left_size = is_bst(node.left, min_val, node.val)
  right_is_bst, right_size = is_bst(node.right, node.val, max_val)
  if left_is_bst and right_is_bst:
      return True, 1 + left_size + right_size
  return False, 0

def largest_bst_size(root):
  _, size = is_bst(root, float('-inf'), float('inf'))
  return size
```
  
<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(N^2) in the worst case, where N is the number of nodes. This is because each node is checked for being the root of a BST.</li>
    <li><strong>Space Complexity:</strong> O(N) for recursion stack space.</li>
</ul>

<p><strong>Optimized Approach</strong></p>

<p><strong>Intuition:</strong> Instead of recalculating the BST property for each node and subtree multiple times, maintain additional information with each node: the size of the largest BST subtree, minimum and maximum values of the subtree, and whether the subtree is a BST.</p>

<p><strong>Steps to Solve:</strong></p>
<ul>
    <li>Traverse the tree in a post-order fashion to ensure you process children before the parent.</li>
    <li>For each node, compute the minimum value, maximum value, size of the largest BST, and whether the current subtree is a BST.</li>
    <li>Use this information to update the size of the largest BST found so far.</li>
</ul>

<p><strong>Recursion Flow with Tree Structure:</strong></p>
<ul>
    <li>Traverse left subtree.</li>
    <li>Traverse right subtree.</li>
    <li>Check if the current subtree is a BST using the results from the left and right subtrees.</li>
    <li>Update the largest BST size based on the current subtree.</li>
</ul>

<p><strong>Code:</strong></p>

```python
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def largest_bst_subtree(node):
  def helper(node):
      if not node:
          return True, float('inf'), float('-inf'), 0
      
      left_is_bst, left_min, left_max, left_size = helper(node.left)
      right_is_bst, right_min, right_max, right_size = helper(node.right)
      
      if left_is_bst and right_is_bst and node.val > left_max and node.val < right_min:
          size = left_size + right_size + 1
          return True, min(node.val, left_min), max(node.val, right_max), size
      else:
          return False, float('-inf'), float('inf'), max(left_size, right_size)
  
  _, _, _, max_bst_size = helper(node)
  return max_bst_size
```
  
<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(N), where N is the number of nodes. Each node is processed once.</li>
    <li><strong>Space Complexity:</strong> O(H), where H is the height of the tree due to recursion stack.</li>
</ul>
