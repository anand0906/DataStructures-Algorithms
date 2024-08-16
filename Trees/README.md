<h1>Tree Data Structure</h1>
<h3>Definition</h3>
<p>The Tree is a non-linear data structure that stores and organizes the data in HIERARCHICAL way.It can store the collection of data items called nodes,which are connected with each other by using edges to form HIERARCHY.</p>
<h3>Real Life Examples :</h3>
<p>A family tree with many generations such as grandparents, parents, children, etc. Family trees are organized hierarchically.</p>
<img src="https://miro.medium.com/max/1400/1*9xW9uddLqt7gujPYBpRp8g.png">
<p>The File System in a computer is arranged in the form of hierarchy as shown below</p>
<img src="https://andysbrainbook.readthedocs.io/en/stable/_images/UnixTree.png">
<p>In HTML, the document object model is represented as tree.The HTML tag contains other tags. We have a head tag and a body tag. Those tags contains specific elements. The head tag has meta and title tags. The body tag has elements that show in the user interface, for example, h1, a, li, etc.</p>
<img src="https://miro.medium.com/max/1118/1*P7lguZAgq5blMOqJyPHopQ.png">
<p>An organization’s structure is another example of a hierarchy.the employees are arranged based on their roles.</p>
<img src="https://cdn-media-1.freecodecamp.org/images/1*GsBCmW5E1GuJ3MpH3Zz0Ew.jpeg">
<h3>Applications.</h3>
<ol>
	<li>File System : folders and subfolders</li>
	<li>E-Commerce Websites : Category->SubCategory->products</li>
	<li>DataBases :B and B+ trees used for Indexing in databases used for fast searching</li>
	<li>Auto-Suggestions : Trie(Special kind of tree) used for fast and dynamic spell checking and suggestion of next words.</li>
	<li>It can be used in heap data structutre and priority queues.</li>
	<li>Syntax analysis in Compilers</li>
	<li>Routing Algorithms</li>
</ol>
<h3>Terminology In Tree Data structure</h3>
<ol>
	<li><b>Node</b>, The tree is a collection of data items called node.where each node contains a value or data.It may or may not have any child nodes.</li>
	<li><b>Root Node</b>, is the first node or top node of the tree, where all other parts are built up on. The tree contains only one root node. (or)The root of the tree is the only node in the tree that has no incoming edges.</li>
	<li><b>Edge</b> is a connection between two nodes.</li>
	<li><b>Parent Node</b>, Suppose a node connected with other nodes, then that node is called parent node and connected nodes are called as <b>child nodes</b>.</li>
	<li>The node which is a predecessor of a node is called the parent node</li>
	<li>The node which is the immediate successor of a node is called the child node of that node</li>
	<li>The topmost node of a tree or the node which does not have any parent node is called the root node</li>
	<li><b>Ansestor</b> of any node is Predessesor node of that node from root node to that node.</li>
	<li><b>Descendent</b> of any node is successor node of that node from node to tha leaf nodes.</li>
	<li>The node and corresponding descendents collectively knowns as subtree</li>
	<li><b>Degree of the node</b> is the total count of child nodes/subtrees attached to that node is called the degree of the node</li>
	<li>The node which doesn't have any child nodes/successive nodes is known as <b>leaf nodes/External node</b>.</li>
	<li>Nodes which are having same parent node is known as <b>siblings</b></li>
	<li>A node with at least one child is called <b>Internal Node</b></li>
	<li>A path is an ordered list of nodes that are connected by edges.</li>
	<li><b>Depth</b> of a node will be the length of path(number of edges) from root node to that node.depth of root is zero.maximum depth of nodes is the depth of tree.</li>
	<li><b>Height</b> of node is length longest path between its node and leaf mode.hight of root node will be the height of tree.hight of leaf node is zero</li>
	<li><b>Level</b> of node will be the depth of tree.</li>
</ol>
<h3>Types Of Tree DataStructure</h3>
<ol>
	<li>General Tree</li>
	<li>Binary Tree</li>
	<li>Binary Search Tree</li>
	<li>AVL Tree</li>
	<li>Red Black Tree</li>
</ol>
<h3>General Tree</h3>
<p>The general tree is one of the types of tree data structure. In the general tree, a node can have either 0 or maximum n number of nodes. There is no restriction imposed on the degree of the node (the number of nodes that a node can contain). The topmost node in a general tree is known as a root node. The children of the parent node are known as subtrees.</p>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsmGJw2gxctsfkR5Djfa3iwwaFu0aQ-u9UVA&s">
<h3>Binary Tree</h3>
<p>Binary Tree is a tree in which each parent contains almost 2 children,i.e left and right child.</p>
<img src="https://cdn-media-1.freecodecamp.org/images/1*ofbwuz4inpf2OlB-l9gtHw.jpeg">
<h4>Properties Of Binary Tree.</h4>
<ul>
	<li>Each node in binary tree contains,data,left and right child.</li>
	<li>The Maximum Number of nodes at level x of a binary tree is 2<sup>x</sup>.For root level,2<sup>0</sup>=1 node.For level 1=2<sup>1</sup>=2.</li>
	<li>Maximum Number of nodes of a tree of height h is 2<sup>(h+1)</sup>-1.For a root node,h=0,Number of nodes=2<sup>(0+1)</sup>-1=2-1=1.For a tree of hight h=1,Number of nodes=2<sup>(1+1)</sup>-1=4-1=3</li>
	<li>The Height of a tree with n nodes is |log(n+1)|-1. For n=1,|log(1+1)|-1=|log(2)|-1=1-1=0</li>
	<li>A Binary Tree with L leaves has at least | Log2L |+ 1   levels. </li>
	<li>In Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children.</li>
</ul>
<h3>Types of Binary Trees</h3>
<ol>
	<li>Full Binary Tree</li>
	<li>Complete Binary Tree</li>
	<li>Perfect Binary Tree</li>
	<li>Degenerate Binary Tree</li>
	<li>Balenced Binary Tree</li>
</ol>
<img src="https://www.theknowledgeacademy.com/_files/images/Types_of_Binary_Trees.png">
<h4>Full Binary Tree</h4>
<p>A Tree said to be full binary tree if and only if all the nodes of a tree contains either zero or two childrens.</p>
<p>It is also called as Strict/Proper Binary Tree</p>
<h4>Complete Binary Tree</h4>
<p>The complete binary tree is a tree in which all the nodes are completely filled except the last level. In the last level, all the nodes must be as left as possible. In a complete binary tree, the nodes should be added from the left.</p>
<h4>Perfect Binary Tree</h4>
<p>A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level.</p>
<h4>Degenerate Binary Tree</h4>
<p>The degenerate binary tree is a tree in which all the internal nodes have only one children.</p>
<p>The above tree is a degenerate binary tree because all the nodes have only one child. It is also known as a right-skewed tree as all the nodes have a right child only.</p>
<p>The above tree is also a degenerate binary tree because all the nodes have only one child. It is also known as a left-skewed tree as all the nodes have a left child only.</p>
<h4>Balenced Binary Tree</h4>
<p>A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes.</p>


