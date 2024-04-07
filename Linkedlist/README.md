<h1>Linkedlist</h1>
<p>Linkedlist is a linear data structure which stores sequence of elements called as nodes, where each node consists of two fields, i.e data field and link/address field which stores the address of successive node</p>
<p>It is a ordered set of data items which are not stored in contigous locations</p>
<p>We know that arrays will take much time for insertion and deletion of items and also its size is fixed</p>
<p>Inorder to overcome these problems with arrays , we are using linked list</p>
<p><strong>Applications</strong></p>
<ul>
	<li>Dynamic Memory Allocation: Linked lists are useful for implementing dynamic data structures, such as stacks, queues, and associative arrays (hash tables), where the size of the data structure can change dynamically during program execution.</li>
	<li>Memory Management: Linked lists are commonly used in memory management algorithms, such as memory allocation and garbage collection. They allow for efficient allocation and deallocation of memory blocks of varying sizes.</li>
	<li>Text Editors: Linked lists can be used to implement the buffer in text editors, where each node represents a line of text, and the pointers link the lines together.</li>
	<li>Navigation Systems: Linked lists can be used in navigation systems to store a sequence of directions or waypoints, where each node represents a step in the journey, and the pointers link the steps together.</li>
	<li>Pages traversal in web browser</li>
</ul>
<p>Linked lists come in several forms:</p>
<ul>
	<li>Singly Linked List</li>
	<li>Doubly Linked List</li>
	<li>Circular Linked List</li>
</ul>
<h2>Singly Linked List</h2>
<p>A singly linked list is a linear data structure consisting of a sequence of elements called nodes. Each node contains two parts: the data, which holds the value of the element, and a pointer/reference to the next node in the sequence. The last node in the list typically points to a null reference, indicating the end of the list.</p>
<p>In this type, each node points to its successive node address only</p>
<p><strong>Node Structure</strong></p>
<p>Each node in a singly linked list contains two fields: data and next.</p>
<p>The data field holds the value of the element stored in the node.</p>
<p>The next field is a reference (pointer) to the next node in the sequence.</p>
<p>We can use classes in python to represent the nodes in linked list</p>

```python
class Node:
	def __init__(self,data,next=None):
		self.data=data
		self.next=next
```
<p><strong>Head Pointer:</strong></p>
<p>Linked lists maintain a reference to the first node in the list, often called the head.	</p>
<p>The head pointer serves as the entry point for accessing the elements of the list.</p>
<p><strong>Advantages</strong></p>
<p>Singly linked lists offer efficient insertion and deletion operations, particularly when performed at the beginning or middle of the list.</p>
<p>They have a simple and lightweight node structure, making them memory-efficient.</p>
<p><strong>Disadvantages</strong></p>
<p>Singly linked lists do not support efficient access to elements by index (random access), as traversal is required to reach a specific element.</p>
<p>They consume additional memory for storing the next pointers, compared to arrays.</p>

<h3>Conversion of array into linked list</h3>
<p>You are given an array ‘Arr’ of size ‘N’ consisting of positive integers.</p>
<p>Make a linked list from the array and return the head of the linked list.</p>
<p>The head of the linked list is the first element of the array, and the tail of the linked list is the last element.</p>
<p><strong>Example</strong></p>
<p>Input: ‘Arr’ = [4, 2, 5, 1]</p>
<p>Output: 4 2 5 1</p>
<p>Explanation: Linked List for the array ‘Arr’ = [4, 2, 5, 1] is 4 -> 2 -> 5 -> 1.</p>
<p><strong>Solution : </strong></p>
<ul>
	<li>Take input array</li>
	<li>Create head node by first element of array since it is first node</li>
	<li>Store head node in current variable, so that its next position can be update later</li>
	<li>Loop through remaining elements from second element and perform following operations</li>
	<ul>
		<li>Create node for array element</li>
		<li>Update current node's next position to newly created node</li>
		<li>Update current node to newly created node</li>
	</ul>
	<li>return head node as output</li>
</ul>

```python
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def convert(arr):
    n=len(arr)
    head=Node(arr[0])
    current=head
    for i in range(1,n):
        temp=Node(arr[i])
        current.next=temp
        current=temp
    return head

def printLinkedList(head):
    while head:
        print(head.data,end="->")
        head=head.next

arr=list(map(int,input().split()))
head=convert(arr)
printLinkedList(head)
```

<p>TC : O(N)</p>
<p>SC : O(N)</p>

<h2>Print Linked List</h2>
<p>Given an head node of a linked list, we have to print the linked list</p>
<ul>
	<li>store head node in a temp varible</li>
	<li>Loop untill temp is None</li>
	<ul>
		<li>print current node data</li>
		<li>assing temp to current node's next</li>
	</ul>
</ul>

```python
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def printLinkedList(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
printLinkedList(head)
```
<p>TC : O(N)</p>
<p>SC : O(N)</p>

<h2>Length Of Linked List</h2>
<p>Given an head node of a linked list, we have to find length of the linked list</p>
<ul>
	<li>store head node in a temp varible</li>
	<li>create count and initialise with zero</li>
	<li>Loop untill temp is None</li>
	<ul>
		<li>increament count by one</li>
		<li>assing temp to current node's next</li>
	</ul>
	<li>return count</li>
</ul>

```python
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def length(head):
    count=0
    temp=head
    while temp:
        count+=1
        temp=temp.next
    return count

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
print(length(head))
```
<p>TC : O(N)</p>
<p>SC : O(N)</p>

<h2>Search An Element In Linked List</h2>
<p>Given an head node of a linked list and data to search, we have to check data is present in linked list or not</p>
<ul>
	<li>store head node in a temp varible</li>
	<li>Loop untill temp is None</li>
	<ul>
		<li>check temp data is equal to searchData, if matches return found</li>
		<li>assing temp to current node's next</li>
	</ul>
	<li>if not matches, return Not Found</li>
</ul>

```python
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def search(head,searchData):
    count=0
    temp=head
    while temp:
        if(temp.data==searchData):
            return True
        temp=temp.next
    return False

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
print(search(head,10))
print(search(head,100))
```
<p>TC : O(N)</p>
<p>SC : O(N)</p>



<h2>Deleting Node In Single Linked List</h2>
<p>Deleting a node in linked list can be performed in several ways such as</p>
<ul>
	<li>Deleting Head Node</li>
	<li>Deleting Tail Node</li>
	<li>Deleting Node Based On Position</li>
	<li>Deleting Node Based On Value</li>
</ul>
<p><strong>Deleting Head Node</strong></p>
<p>When removing head node, we have to make head.next node as a head node</p>

```python
def deleteHead(head):
    if(head==None):
        return None
    temp=head
    head=head.next
    return head
```
<p><strong>Deleting Tail Node</strong></p>
<p>To Remove Tail Node, We have to reach tail nodes previous node</p>
<p>Then, make tail-previous next position as None, then it will be tail node</p>

```python
def deleteTail(head):
    if(head==None or head.next==None):
        return None
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head
```

<p><strong>Deleting Node Based On Position</strong></p>
<p>We have to delete node based on given position</p>
<p>When we are dealing with linked list problems, we have to think base cases first</p>
<ul>
	<li>Check position is 1, then delete head node as discussed proviously</li>
	<li>Otherwise, Use count to find node at given position</li>
	<li>Since we need to remove node at that position , find its previous node</li>
	<li>Then, set its next position to its next nodes next</li>
</ul>

```python
def deleteByPosition(head,pos):
    if(head==None):
        return None
    if(pos==1):
        temp=head
        head=head.next
        return head
    previous=None
    temp=head
    count=0
    while temp:
        count+=1
        if(count==pos):
            previous.next=temp.next
            return head
        previous=temp
        temp=temp.next
    return head
```
<p><strong>Deleting Node Based On Positions</strong></p>
<p>We have to delete node based on given value</p>
<ul>
	<li>Check, if head's data matches with given value, if it is then delete head node</li>
	<li>loop through each node, and track its privous node also</li>
	<li>when node's data matches with the given value, change its previous node's next to node's next</li>
</ul>

```python
def deleteByValue(head,value):
    if(head==None):
        return None
    if(head.data==value):
        temp=head
        head=head.next
        return head
    previous=None
    temp=head
    while temp:
        if(temp.data==value):
            previous.next=temp.next
            return head
        previous=temp
        temp=temp.next
    return head
```


<h2>Inserting Node In Single Linked List</h2>
<p>Inserting a node in linked list can be performed in several ways such as</p>
<ul>
	<li>Inserting Head Node</li>
	<li>Inserting Tail Node</li>
	<li>Inserting Node Based On Position</li>
	<li>Inserting Node Based On Value</li>
</ul>
<p><strong>Inserting Head Node</strong></p>
<p>When Inserting head node, we have to make new node as head and its next to existing head</p>

```python
def insertAtHead(head,data):
    temp=Node(data)
    temp.next=head
    return temp
```
<p><strong>Inserting Tail Node</strong></p>
<p>To Insert Tail Node, We have to reach tail node</p>
<p>Then, make tail next position to new Node</p>

```python
def insertAtTail(head,data):
    if(head==None):
        return Node(data)
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=Node(data)
    return head
```

<p><strong>Inserting Node Based On Position</strong></p>
<p>We have to Insert node based on given position</p>
<p>When we are dealing with linked list problems, we have to think base cases first</p>
<ul>
	<li>Check if position is 1, if it is, then add node at head</li>
	<li>Since we need to add node at certain position, since there may be already node existed at given position, so we have to find its previous positiona and make next to new node</li>
	<li>Use count to track position, if count equals to given position - 1, then add new node to its next and new nodes to next to existing one</li>
</ul>

```python
def insertAtPosition(head,data,pos):
    if(head==None):
        if(pos==1):
            return Node(data)
        return head
    if(pos==1):
        temp=Node(data)
        temp.next=head
        return temp
    count=0
    temp=head
    while temp:
        count+=1
        if(count==pos-1):
            new=Node(data,temp.next)
            temp.next=new
            break
        temp=temp.next
    return head
```
<p><strong>Inserting Node Based On Positions</strong></p>
<p>We have to Inserting node based on given value</p>
<ul>
	<li>Check if heads data matches with given value, if it is, then add node at head</li>
	<li>Since we need to add node at certain position where it matches node'a data, since there may be already node existed at given position, so we have to find its previous positiona and make next to new node</li>
	<li>Loop through linked list, if current nodes next data equals to given value, then add new node to its next and new nodes to next to existing one</li>
</ul>

```python
def insertAtValue(head,data,value):
    if(head==None):
        return None
    if(head.data==value):
        temp=Node(data)
        temp.next=head
        return temp
    temp=head
    while temp:
        if(temp.next!=None and temp.next.data==value):
            new=Node(data,temp.next)
            temp.next=new
            break
        temp=temp.next
    return head
```

<h2>Doubly Linked List</h2>
<p>A doubly linked list is a type of linked list in which each node contains three fields: the data, a pointer/reference to the next node (commonly named next), and a pointer/reference to the previous node (commonly named prev). </p>
<p>This structure allows traversal in both forward and backward directions.</p>
<p><strong>Advantages</strong></p>
<ul>
	<li>Bidirectional Traversal: Doubly linked lists allow traversal in both forward and backward directions, making them suitable for applications that require accessing elements in reverse order.</li>
	<li>Efficient Insertion and Deletion: Insertion and deletion operations at any position in the list can be done more efficiently compared to singly linked lists. This is because accessing the previous node (for deletion) or the next node (for insertion) can be done directly without needing to traverse the list from the beginning.</li>
	<li>Previous Node Access: Each node in a doubly linked list maintains a reference to its previous node, allowing for efficient backward traversal and enabling operations that require access to both the previous and next nodes.</li>
	<li>Implementation of Data Structures: Doubly linked lists are essential in implementing other data structures like queues and deques (double-ended queues) efficiently, as they support insertion and deletion operations at both ends of the list.</li>
	<li>Undo Functionality: Doubly linked lists are useful in applications that require undo functionality, where changes need to be reversed efficiently by traversing backward through a sequence of operations.</li>
</ul>
<p><strong>Nodes Structure</strong></p>
<p>Each node in a doubly linked list contains three fields: data, next, and prev.</p>
<p>The data field holds the value of the element stored in the node.</p>
<p>The next field is a reference (pointer) to the next node in the sequence.</p>
<p>The prev field is a reference (pointer) to the previous node in the sequence.</p>

```python
class Node:
	def __init__(self,data,prev=None,next=None):
		self.data=data
		self.prev=prev
		self.next=next
```

<h2>Convert Array Into Doubly Linked List</h2>
<p>You are given an array ‘Arr’ of size ‘N’ consisting of positive integers.</p>
<p>Your task is to make a doubly linked list from the array and return the head of the linked list.</p>
<p>Here, the head of the doubly linked list is the first element of the array, and the tail of the doubly linked list is the last element.</p>
<p><strong>Example</strong></p>
<p>Input: ‘N’ = 4, ‘Arr’ = [4, 2, 5, 1]</p>
<p>Output: 4 2 5 1</p>
<p><strong>Solution : </strong></p>
<ul>
    <li>Create head node from first element of array</li>
    <li>Store head node in previous variable, so that it can be assined to its next node's prev</li>
    <li>Loop from second element till last, and do following operations</li>
    <ul>
        <li>Create New Node For Current element</li>
        <li>Set prev of new node with previous node</li>
        <li>Set previous next to new node</li>
        <li>update previous to current new node</li>
    </ul>
</ul>

```python
class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

def convert(array):
    n=len(array)
    head=Node(array[0])
    previous=head
    for i in range(1,n):
        temp=Node(array[i])
        temp.prev=previous
        previous.next=temp
        previous=temp
    return head

def printLinkedList(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next


array=list(map(int,input().split()))
head=convert(array)
printLinkedList(head)
```

<h2>Deleting Node in Doubly Linked List</h2>
<p><strong>Deleting Head Node</strong></p>
<p>You are given a doubly-linked list of length ’n’ .</p>
<p>Your task is to delete the head of a doubly-linked list.</p>
<p><strong>Example</strong></p>
<p>Input: 5 <-> 8 <-> 3 <-> 7 <-> 9</p>
<p>Output: 8 <-> 3 <-> 7 <-> 9</p>
<p>Explanation: The head of the given list is at 5. After deletion of head, new list is 8 <-> 3 <-> 7 <-> 9.</p>
<p><strong>Solution</strong></p>
<ul>
    <li>check, head or head.next is None, if it is return null as answer, since if there is only one node and deleting will result none only</li>
    <li>otherwise, set head node to head.next, hence head position will be changed</li>
    <li>set head.prev to null, since head node should't have any prev node</li>
    <li>set previous head.next to None, since it should be deleted and not to refer any other node</li>
</ul>

```python
def deleteHead(head):
    if(head==None or head.next==None):
        return None
    temp=head
    head=head.next
    head.prev=None
    temp.next=None

    return head
```

<p><strong>Deleting Tail Node</strong>
<p>You are given a doubly-linked list of length ’n’ .</p>
<p>Your task is to delete the Tail of a doubly-linked list.</p>
<p><strong>Example</strong></p>
<p>Input: 5 <-> 8 <-> 3 <-> 7 <-> 9</p>
<p>Output:5 <-> 8 <-> 3 <-> 7</p>
<p>Explanation: The Tail of the given list is at 9. After deletion of Tail, new list is 5 <-> 8 <-> 3 <-> 7.</p>
<p><strong>Solution</strong></p>
<ul>
    <li>check, head or head.next is None, if it is return null as answer, since if there is only one node and deleting will result none only</li>
    <li>Otherwise, loop through linked list and get tail node.</li>
    <li>get Tail prev node and assign to previous variable</li>
    <li>set tail.prev to None</li>
    <li>set previous.next to None</li>
    <li>Then, tail will be removed from linked list</li>
</ul>

```python
def deleteTail(head):
    if(head==None or head.next==None):
        return None
    tail=head
    while tail.next!=None:
        tail=tail.next
    previous=tail.prev
    previous.next=None
    tail.prev=None
    return head
```

<p><strong>Delete Node By Position</strong></p>
<p>You are given a Doubly linked list, where every node in the linked list contains two pointers, ‘next’ and ‘prev’, which point to the next node and previous node in the list respectively. All nodes have some positive integer value associated with them.</p>
<p>Your task is to delete the node at the ‘k’-th position.</p>
<p>The 'k' given will always be less than or equal to the length of the 'list'.</p>
<p><strong>Example</strong></p>
<p> Input: ‘k’ = 3, 'list' = [1, 2, 5, 4]</p>
<p> Output: [1, 2, 4]</p>
<p> Explanation:The 3rd node, which is '5', is deleted.</p>
<p><strong>Solution : </strong></p>
<ul>
    <li>First find the node by given kth value, by using count method</li>
    <li>Check all base cases like, if node is head or tail or middle</li>
    <li>If node.prev is none and node.next is none, then there is only one element, return None</li>
    <li>if node.prev is none, then it is head node,delete head node as per discussed above</li>
    <li>if node.next is none, then it is tail node, delete tail node as per discussed above</li>
    <p>otherwise, node is in middle. take previous node and next node</p>
    <p>set previous node.next to next node</p>
    <p>set next node.previous to prvious node</p>
    <p>set node.prev and node.next to None</p>
</ul>

```python
def deleteByPosition(head,k):
    if(head==None):
        return head
    cnt=0
    temp=head
    while temp:
        cnt+=1
        if(cnt==k):
            break
        temp=temp.next
    prevNode=temp.prev
    nextNode=temp.next
    if(prevNode==None and nextNode==None):
        return None
    if(prevNode==None):
        head=deleteHead(head)
        return head
    if(nextNode==None):
        head=deleteTail(head)
        return head
    prevNode.next=temp.next
    nextNode.prev=prevNode
    temp.next=None
    temp.prev=None
    return head
```
<p><strong>Delete node by value</strong></p>
<p>We have to delete node whose data matches with given value</p>

<p><strong>Solution : </strong></p>
<ul>
    <li>First find the node by given value</li>
    <li>Check all base cases like, if node is head or tail or middle</li>
    <li>If node.prev is none and node.next is none, then there is only one element, return None</li>
    <li>if node.prev is none, then it is head node,delete head node as per discussed above</li>
    <li>if node.next is none, then it is tail node, delete tail node as per discussed above</li>
    <p>otherwise, node is in middle. take previous node and next node</p>
    <p>set previous node.next to next node</p>
    <p>set next node.previous to prvious node</p>
    <p>set node.prev and node.next to None</p>
</ul>

```python
def deleteByValue(head,data):
    if(head==None):
        return head
    temp=head
    while temp:
        if(temp.data==data):
            break
        temp=temp.next
    prevNode=temp.prev
    nextNode=temp.next
    if(prevNode==None and nextNode==None):
        return None
    if(prevNode==None):
        head=deleteHead(head)
        return head
    if(nextNode==None):
        head=deleteTail(head)
        return head
    prevNode.next=temp.next
    nextNode.prev=prevNode
    temp.next=None
    temp.prev=None
    return head
```

<p><strong>Delete Node</strong></p>
<p>There exists a doubly linked list with nodes containing integer values. You are given a specified node of the list which you have to delete.</p>
<p>The node to be deleted is guaranteed not to be the head of the list.</p>
<p><strong>Example</strong></p>
<p>List = 1 <-> 2 <-> 3 <-> 4</p>
<p>Node = '3', its position k = 3</p>
<p>Output: 1 <-> 2 <-> 4</p>

<p><strong>Solution : </strong></p>
<ul>
    <li>Check all base cases like, if node is head or tail or middle</li>
    <li>If node.prev is none and node.next is none, then there is only one element, return None</li>
    <li>if node.prev is none, then it is head node,delete head node as per discussed above</li>
    <li>if node.next is none, then it is tail node, delete tail node as per discussed above</li>
    <p>otherwise, node is in middle. take previous node and next node</p>
    <p>set previous node.next to next node</p>
    <p>set next node.previous to prvious node</p>
    <p>set node.prev and node.next to None</p>
</ul>

```python

def deleteByValue(head,node):
    if(head==None):
        return head
    prevNode=node.prev
    nextNode=node.next
    if(prevNode==None and nextNode==None):
        return None
    if(prevNode==None):
        head=deleteHead(head)
        return head
    if(nextNode==None):
        head=deleteTail(head)
        return head
    prevNode.next=node.next
    nextNode.prev=prevNode
    node.next=None
    node.prev=None
    return head
```

<h2>Inserting Node In Doubly Linked List</h2>
<p><strong>Insert Before Head</strong></p>
<ul>
    <li>Check if head is None, then return new Node with given data</li>
    <li>otherwise, create new node with given data</li>
    <li>set new node next to head</li>
    <li>set head.prev to new node</li>
    <li>return new node as head</li>
</ul>

```python
def insertBeforeHead(head,data):
    if(head==None):
        return Node(data)
    new=Node(data)
    new.next=head
    head.prev=new
    return new
```

<p><strong>Insert before tail</strong></p>
<ul>
    <li>Check if head is None, then return None</li>
    <li>Check if head.next is none, that means there is only node, so we can call insertBeforeHead(head,data)</li>
    <li>Otherwise, go to tail using while loop</li>
    <li>Get previous node of tail node</li>
    <li>Create new node</li>
    <li>set new node.next to tail and new node.prev to previous</li>
    <li>set previous.next new node and tail.prev to new node</li>
</ul>

```python  
def insertBeforeTail(head,data):
    if(head==None):
        return Node(data)
    if(head.next==None):
        head=insertBeforeHead(head,data)
        return head
    temp=head
    while temp.next:
        temp=temp.next
    tail=temp
    previous=tail.prev
    new=Node(data)
    new.next=tail
    new.prev=previous
    tail.prev=new
    previous.next=new
    return head
```

<p><strong>Insert before kth node</strong></p>
<ul>
    <li>Check if head is None, then return None</li>
    <li>Get node at kth position using count method</li>
    <li>Take previous node of kth node</li>
    <li>create new node</li>
    <li>set new node.next to kth node and new node.prev to previous</li>
    <li>previous.next to new node and kth node.prev to new node</li>
</ul>

```python
def insertBeforeKthElement(head,data,k):
    if(head==None):
        return None
    cnt=0
    temp=head
    while temp:
        cnt+=1
        if(cnt==k):
            break
        temp=temp.next
    else:
        return None
    previous=temp.prev
    new=Node(data)
    new.next=temp
    new.prev=previous
    previous.next=new
    temp.prev=new
    return head
```

<h2>Reverse Doubly Linked List</h2>
<p>You are given a doubly-linked list of size 'N', consisting of positive integers. Now your task is to reverse it and return the head of the modified list.</p>
<p>Note : A doubly linked list is a kind of linked list that is bidirectional, meaning it can be traversed in both forward and backward directions.</p>
<p><strong>Example : </strong></p>
<p>input : </p>
<p>4</p>
<p>4 3 2 1</p>
<p>This means you have been given doubly linked list of size 4 = 4 <-> 3 <-> 2 <-> 1.</p>
<p>Output:</p>
<p>1 2 3 4</p>
<p>This means after reversing the doubly linked list it becomes 1 <-> 2 <-> 3 <-> 4.</p>
<p><strong>Solution : </strong></p>
<p><strong>BruteForce : </strong></p>
<ul>
    <li>Simple loop over given linked list and push each element into stack</li>
    <li>Again loop from head, for each node take the top element from stack and assign that data to current data</li>
    <li>In this way, we can reverse the data present in linked list</li>
</ul>
<img src="https://static.takeuforward.org/wp/uploads/2023/11/dll-reverse-a1-step2-1024x813.jpgs">
<img src="https://static.takeuforward.org/wp/uploads/2023/11/dll-reverse-a3-step3-1024x958.jpg">

```python
def reverseBruteForce(head):
    stack=[]
    temp=head
    while temp:
        stack.append(temp.data)
        temp=temp.next
    temp=head
    while temp:
        temp.data=stack.pop()
        temp=temp.next
    return head
```

<p><strong>Optimized</strong></p>
<p>More optimzed solution will be, just reverse the links present for each node i.e next and prev</p>
<p>And move head node to tail</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/11/dll-reverse-a1-cum-739x1024.jpg">

```python
def reverseOptimized(head):
    temp=head
    current=head
    while temp:
        current=temp
        temp.next,temp.prev=temp.prev,temp.next
        temp=temp.prev
    head=current
    return head
```
<p>Time Complexity : O(N) We only have to traverse the doubly linked list once, hence our time complexity is O(N).</p>
<p>Space Complexity : O(1), as the reversal is done in place.</p>

<h2>Adding Two Singly Linked Lists</h2>
<p>You are given two non-negative numbers 'num1' and 'num2' represented in the form of linked lists</p>
<p>The digits in the linked lists are stored in reverse order, i.e. starting from least significant digit (LSD) to the most significant digit (MSD), and each of their nodes contains a single digit.</p>
<p>Calculate the sum of the two numbers and return the head of the sum list.</p>
<p><strong>Example-1 : </strong></p>
<p>Input Format:</p>
<p>(Pointer/Access to the head of the two linked lists)</p>
<p>num1  = 243, num2 = 564</p>
<p>l1 = [2,4,3]</p>
<p>l2 = [5,6,4]</p>
<p>Result: sum = 807; L = [7,0,8]</p>
<p>Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the or original number and then add them as → 342 + 465 = 807. Refer to the image below.</p>
<img src="https://lh3.googleusercontent.com/-6tuYtP69ITIp3DBjDKYupMDWHd2y3SruICs-HEMZtYnVTlwARbbsMRyfVkaOK5mnJC2N7DqcrcqfoQqXrTmFDEIGz1BlrjzUVfl3nd0QK6Q6ja0k-sF7X1BZJ2FtXNCruTAN1U=s1600">
<p><strong>Example-2 : </strong></p>
<p>Input Format:</p>
<p>(Pointer/Access to the head of the two linked lists)</p>
<p>num1  = 243, num2 = 564</p>
<p>l1 = [9,9,9,9,9,9,9]</p>
<p>l2 = [9,9,9,9]</p>
<p>Result: [8,9,9,9,0,0,0,1]</p>
<p>Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the original number and then add them as → 9999999 + 9999 = 8999001. Refer to the image below..</p>
<img src="https://lh4.googleusercontent.com/HbBzYULG5Q3ClLa3a6SPEgw_dio2iCyT8sQ4edmYBvQ0SqTGCqIapIaRONy5dNQ-SnzznidbKH0v3t8ivHMazZvP68k14esr3ULwPmnem4QV3j3Z-0tJw5VL5UyB1feMFKhQ3yM=s1600">

<p><strong>Solution : </strong></p>
<p>Given Two Numbers , we have to find the sum of those two numbers</p>
<p>These two numbers are represented in form two linked list (in reverse order of digits)</p>
<p>We can simply create new linked list by adding digits of both linked list</p>
<ul>
    <li>Create new linked list, by creating one dummy node and mark it as head</li>
    <li>Initialise carry with 0, since there is no carry at beggining</li>
    <li>Untill both heads of linked lists are null , loop through it</li>
    <ul>
        <li>initialise sum with 0</li>
        <li>add carry to sum</li>
        <li>add data of linked list 1 to sum, if node is not null</li>
        <li>add data of linked list 2 to sum, if node is not null</li>
        <li>update carry with new sum, carry=sum%10</li>
        <li>create new node with data as sum, Node(sum%10)</li>
        <li>link new node to new linked list</li>
    </ul>
    <li>if, carry is there, add new node with carry as data and link to new linked list</li>
    <li>return head of new linked list</li>
</ul>

```python
def sum(head1,head2):
    sumHead=Node(-1)
    temp=sumHead
    temp1=head1
    temp2=head2
    carry=0
    while temp1 or temp2:
        s=carry
        if(temp1):
            s+=temp1.data
            temp1=temp1.next
        if(temp2):
            s+=temp2.data
            temp2=temp2.next
        carry=s//10
        new=Node(s%10)
        temp.next=new
        temp=new
    if(carry!=0):
        new=Node(carry)
        temp.next=new
    return sumHead.next
```
<p>Time Complexity: O(max(m,n)). Assume that m and n represent the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.</p>
<p>Space Complexity: O(max(m,n)). The length of the new list is at most max(m,n)+1.</p>


<h2>Segregate Even and Odd Index Values in Singly Linked List</h2>
<p>You are given the head node of a singly linked list 'head'. Your task is to modify the linked list in such a way that all the odd indexed nodes appear before the all even indexed node</p>
<p><strong>Example : </strong></p>
<p>Sample Input 1</p>
<p>2 1 3 5 6 4 7</p>
<p>Sample Output 1</p>
<p>2 3 6 7 1 5 4</p>
<p>Explanation of Sample Input 1</p>
<p>Given singly linked list 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7.</p>
<p>Arrange all the odd indexed in the starting and even indexed at the end of the linked list.</p>
<p>So ‘2,3,6,7’ must appear in the starting and ‘1,5,4’ must appear at the end of linked list </p>

<p><strong>Solution : </strong></p>
<p>We have given a linked list, we have to arrange the node such that odd indexed node should come first and even indexed node should come last</p>
<p>We can solve in two different ways</p>
<p><strong>BruteForce Approach</strong></p>
<p>Create a list and add odd indexed values first and even indexed values next By looping through linked list</p>
<p>Then again loop over the given linked list and replace values as in newly create list</p>
<p>By rearranging values like this, we can solve this problem</p>

```python
def bruteForce(head):
    if(head==None or head.next==None):
        return head
    newOrder=[]

    #adding odd indexed values
    temp=head
    while temp and temp.next:
        newOrder.append(temp.data)
        temp=temp.next.next
    if(temp):
        newOrder.append(temp.data)

    #adding even indexed values
    temp=head.next
    while temp and temp.next:
        newOrder.append(temp.data)
        temp=temp.next.next
    if(temp):
        newOrder.append(temp.data)

    #replacing new values
    temp=head
    i=0
    while temp and temp.next:
        temp.data=newOrder[i]
        i+=1
        temp=temp.next
    if(temp):
        temp.data=newOrder[i]

    return head
```

<p>TC : O(2n)</p>
<p>SC : O(n)</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, first we will link the odd indexed node's together</p>
<p>Then, we will link even indexed node's together</p>
<p>finally, odd list is linked to even's start node</p>
<p>Final list will be our answer</p>
<ul>
    <li>set starting node of odd list is head</li>
    <li>set starting node of even list is head.next</li>
    <li>Loop Untill even is not null</li>
    <ul>
        <li>set currentOdd.next to currentOdd.next.next</li>
        <li>set currentEven.next to currentEven.next.next</li>
        <li>update currentOdd to currentOdd.next</li>
        <li>update currentEven to currentEven.next</li>
    </ul>
    <li>Finally, link currentOdd.next to evenStarting</li>
</ul>

```python
def optimized(head):
    if(head==None or head.next==None):
        return head
    oddHead=head
    evenHead=head.next

    odd=head
    even=head.next
    while even and even.next:
        odd.next=odd.next.next
        even.next=even.next.next

        odd=odd.next
        even=even.next

    odd.next=evenHead

    return head
```

<p>TC : O(n/2)</p>
<p>SC : O(1)</p>

<h2>Sort Linkes List Have 0's 1's and 2's</h2>
<p>Given a linked list of 'N' nodes, where each node has an integer value that can be 0, 1, or 2. You need to sort the linked list in non-decreasing order and the return the head of the sorted list.</p>
<p>Given linked list is 1 -> 0 -> 2 -> 1 -> 2. </p>
<p>The sorted list for the given linked list will be 0 -> 1 -> 1 -> 2 -> 2.</p>

<p><strong>Solution</strong></p>
<p>We have given a linked list having 0's, 1's and 2's, we have to sort the linked list based on values</p>
<p>We can solve this problem in several approaches</p>
<p><strong>BruteForce Approach : </strong></p>
<p>We can rearrange the values by tracking the values and modifing the values</p>
<ul>
    <li>Track the count of 0's,1's,2's by looping through given linked list</li>
    <li>Now, again loop through linked list and modfify each node's value based on counts of values</li>
</ul>

```python
def bruteForce(head):
    if(head==None or head.next==None):
        return head5
    cnt0,cnt1,cnt2=0,0,0
    temp=head
    while temp:
        if(temp.data==0):
            cnt0+=1
        elif(temp.data==1):
            cnt1+=1
        else:
            cnt2+=1
        temp=temp.next

    temp=head
    while temp:
        if(cnt0!=0):
            temp.data=0
            cnt0-=1
        elif(cnt1!=0):
            temp.data=1
            cnt1-=1
        else:
            temp.data=2
            cnt2-=1
        temp=temp.next
    return head
```

<p>TC : O(2N)</p>
<p>SC : O(1)</p>

<p><strong>Optimized Approach : </strong></p>
<p>In This approach, we will link 0's nodes together , 1's nodes together, 2's nodes together</p>
<p>finally, link 0's list to 1's list to 2's list</p>
<p>then we will get the final list</p>
<ul>
    <li>Create dummy node for all three new lists and mark it as head node for those</li>
    <li>create temporary variables for each three list, assign it to respective head nodes</li>
    <li>Loop through given linked list</li>
    <ul>
        <li>if current node's data matches with 0, then link that node to 0's list</li>
        <li>if current node's data matches with 1, then link that node to 1's list</li>
        <li>if current node's data matches with 2, then link that node to 2's list</li>
    </ul>
    <li>finally, link those three lists together based on availabilty of values</li>
</ul>

```python
def optimized(head):
    zeroHead,oneHead,secHead=Node(-1),Node(-1),Node(-1)
    zero,one,sec=zeroHead,oneHead,secHead
    temp=head
    while temp:
        if(temp.data==0):
            zero.next=temp
            zero=temp
        elif(temp.data==1):
            one.next=temp
            one=temp
        elif(temp.data==2):
            sec.next=temp
            sec=temp
        temp=temp.next

    temp=[]
    current=zero
    if(one.data!=-1):
        current.next=oneHead.next
        current=one
    if(sec.data!=-1):
        current.next=secHead.next
        sec.next=None
    else:
        one.next=None

    return zeroHead.next;
```

<p>TC : O(N)</p>
<p>SC : O(1)</p>

<h2>Delete Nth Node From Last Of Linked List</h2>
<p>You have been given a singly Linked List of 'N' nodes with integer data and an integer 'K'.</p>
<p>Your task is to remove the 'K'th node from the end of the given Linked List and return the head of the modified linked list.</p>
<p><strong>Example</strong></p>
<p>Input : 1 -> 2 -> 3 -> 4 -> 'NULL'  and  'K' = 2</p>
<p>Output: 1 -> 2 -> 4 -> 'NULL'</p>
<p>After removing the second node from the end, the linked list become 1 -> 2 -> 4 -> 'NULL'.</p>
<img src="https://files.codingninjas.in/untitled-7-27708.jpg">
<p><strong>Solution : </strong></p>
<p>We can solve this in two approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>Since we need to delete the nth node from end of list, from beginning we have to delete (length-n+1)th node from first</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/12/tuxpi.com_.1702843904.jpg">
<ul>
    <li>first find the lenth of given linked list</li>
    <li>then, delete (length-n+1) node</li>
    <li>To delete node (length-n+1), we need to reach (length-n) node and put its next to node.next.next</li>
</ul>

```python
def delete(head,n):
    if(head==None):
        return head
    length=0
    temp=head
    while temp:
        length+=1
        temp=temp.next

    if(length==n):
        head=head.next
        return head

    target=length-n
    cnt=0
    temp=head
    while temp:
        cnt+=1
        if(cnt==target):
            break
        temp=temp.next
    temp.next=temp.next.next
    return head
```

<p>Time Complexity: O(L)+O(L-N), We are calculating the length of the linked list and then iterating up to the (L-N)th node of the linked list, where L is the total length of the list.</p>
<p>Space Complexity: O(1), as we have not used any extra space.</p>

<p><strong>Optimized Approach : </strong></p>
<p>To enhance efficiency, we will involve two pointers, a fast pointer and a slow pointer. The fast-moving pointer will initially be exactly N nodes ahead of the slow-moving pointer. After which, both of them will move one step at a time. When the fast pointer reaches the last node, i.e., the L-th node, the slow is guaranteed to be at the (L-N)-th node, where L is the total length of the linked list.</p>
<ul>
    <li>Initialize two pointers, `slow` and `fast`, to the head of the linked list. Initially, only fast will move till it crosses N nodes, after which both of the pointers will move simultaneously.</li>
    <img src="https://static.takeuforward.org/wp/uploads/2023/12/tuxpi.com_.1702844019.jpg">
    <li>Traverse the linked list till the fast pointer reaches the last node, that is, the Lth Node, at this stage, the slow pointer is guaranteed to be at the (L-N)th node.</li>
    <img src="https://static.takeuforward.org/wp/uploads/2023/12/tuxpi.com_.1702844072.jpg">
    <li>Point this slow pointer to the (L-N+2)th node, effectively skipping the Nth node from the end or the (L-N+1)th node from the start.</li>
    <img src="https://static.takeuforward.org/wp/uploads/2023/12/tuxpi.com_.1702844098.jpg">
    <li>Finally, free up the space occupied by this to delete it.</li>
</ul>

```python
def optimized(head,n):
    slow,fast=head,head
    for i in range(n):
        fast=fast.next
    if(fast==None):
        head=head.next
        return head
    while fast.next:
        fast=fast.next
        slow=slow.next
    slow.next=slow.next.next
    return head
```

<p>Time Complexity: O(N) since the fast pointer will traverse the entire linked list, where N is the length of the linked list.</p>
<p>Space Complexity: O(1), as we have not used any extra space.</p>

<h2>Reverse Singly linked list</h2>
<p>Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.</p>
<p><strong>Example : </strong></p>
<p>Input Format:</p>
<p>LL: 1   3   2   4 </p>
<img src="https://static.takeuforward.org/wp/uploads/2023/12/reversell-1024x222.jpg">
<p>Output</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/12/reversell-1024x222.jpg">
<p>Explanation: After reversing the linked list, the new head will point to the tail of the old linked list.</p>

<p><strong>Solution : </strong></p>
<p>Given a linked list, we have to reverse it</p>
<p>We can solve this problem in several approaches</p>
<p><strong>BruteForce Approach</strong></p>
<p>Rearrage the data, create a stack and add all linked list data</p>
<p>The pop the data and update linked list again</p>
<p>Then we can get reversed linked list</p>
<ul>
    <li>Create a stack</li>
    <li>Iterate through linked list and add each node data to stack</li>
    <li>now stack contains all linked list data</li>
    <li>Now iterate through linked list again update the data of each node by poping elements from stack</li>
    <li>finally return head</li>
</ul>

```python
def bruteforce(head):
    stack=[]
    temp=head
    while temp:
        stack.append(temp.data)
        temp=temp.next
    temp=head
    while temp:
        temp.data=stack.pop()
        temp=temp.next
    return head
```
<p>Time Complexity: O(2N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and update the linked list. Both traversals take O(N) time, hence time complexity  O(2N) ~ O(N).</p>
<p>Space Complexity: O(N) We use a stack to store the values of the linked list, and in the worst case, the stack will have all N values,  ie. storing the complete linked list.</p>

<p><strong>Optimized approach</strong></p>
<p>In this approach, we will reverse the direction of linked list</p>
<p>The main idea is to flip the order of connections in the linked list, which changes the direction of the arrows. When this happens, the last element becomes the new first element of the list. This in-place reversal allows us to efficiently transform the original list without using extra space.</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/12/reversell-inplace-1024x375.png">
<ul>
    <li>Initialize temp with head, so that we can itetare throgh linked list from starting</li>
    <li>Initialize previous with None, since previous to head is none</li>
    <li>Now iterate through linked list untill it reaches end</li>
    <ul>
        <li>swap temp and previous nodes</li>
        <li>update temp to current.next (prev after swap) node</li>
        <li>update current to temp node, useful to return at the end</li>
        <li>update previous with current node</li>
    </ul>
    <li>return last node (tracked with current), after swapping head node will be last node</li>
</ul>

```python
def optimized(head):
    temp=head
    prev=None
    current=head
    while temp:
        current=temp
        temp.next,prev=prev,temp.next
        temp=prev
        prev=current
    return current
```

<p>Time Complexity: O(N) The code traverses the entire linked list once, where 'n' is the number of nodes in the list. This traversal has a linear time complexity, O(n).</p>
<p>Space Complexity: O(1) The code uses only a constant amount of additional space, regardless of the linked list's length. This is achieved by using three pointers (prev, temp and front) to reverse the list without any significant extra memory usage, resulting in constant space complexity, O(1).</p>

<h2>Check if the given Singly Linked List is Palindrome</h2>
<p>You are given a Singly Linked List of integers. You have to return true if the linked list is palindrome, else return false.</p>
<p>A Linked List is a palindrome if it reads the same from left to right and from right to left.</p>
<p><strong>Example : </strong></p>
<p>The lists (1 -> 2 -> 1), (3 -> 4 -> 4-> 3), and (1) are palindromes, while the lists (1 -> 2 -> 3) and (3 -> 4) are not.</p>

<p><strong>Solution : </strong></p>
<p>We can solve this problem in several ways</p>
<p><strong>BruteForce Approach : </strong></p>
<p>We will first add all data to a stack and compare again by poping it (reverse order), if any comparison fails, we will return False</p>
<ul>
    <li>Create a stack</li>
    <li>iterate through given linked list and push each node data to stack</li>
    <li>Iterate again through linked list and for each node pop element from stack and check if its is equal or not</li>
    <li>If any matching fails , return False</li>
    <li>Otherwise return True</li>
</ul>

```python
def bruteForce(head):
    stack=[]
    temp=head
    while temp:
        stack.append(temp.data)
        temp=temp.next
    temp=head
    while temp:
        if(temp.data!=stack.pop()):
            return False
        temp=temp.next
    return True
```

<p>Time Complexity: O(2 * N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and compare with the linked list. Both traversals take O(2*N) ~ O(N) time.</p>

<p>Space Complexity: O(N) We use a stack to store the values of the linked list, and in the worst case, the stack will have all N values,  ie. storing the complete linked list.</p>

<p><strong>Optimized Approach</strong></p>
<p></p>

<h2>Adding 1 To Given Singly Linked List</h2>
<p>You're given a positive integer represented in the form of a singly linked-list of digits. The length of the number is 'n'.</p>
<p>Add 1 to the number, i.e., increment the given number by one.</p>
<p>The digits are stored such that the most significant digit is at the head of the linked list and the least significant digit is at the tail of the linked list.</p>
<p><strong>Example : </strong></p>
<p>Input: Initial Linked List: 1 -> 5 -> 2</p>
<p>Output: Modified Linked List: 1 -> 5 -> 3</p>
<p>Explanation: Initially the number is 152. After incrementing it by 1, the number becomes 153.</p>
<p><strong>Example : </strong></p>
<p>Input: Initial Linked List: 9 -> 9 -> 9</p>
<p>Output: Modified Linked List: 1 -> 0 -> 0 -> 0</p>
<p>Explanation: Initially the number is 999. After incrementing it by 1, the number becomes 1000.</p>

<p><strong>Solution</strong></p>
<p>Given single linked list, where each node contains a digit, combines forms an integer</p>
<p>We need to add 1 to it,after adding 1, we will get new linked list with its digit</p>
<p>This problem can be solved in different ways</p>

<p><strong>Iterative Approach Approach</strong></p>
<p>As per maths, we can add 1 to a number, to its last digit and move towards to front if there is any carry</p>
<p>So, we have to reverse the given linked list and add 1 to its first node and have to add carry to its next nodes if there is any carry</p>
<p>After completion of adding , we have to reverse again to form number</p>
<ul>
    <li>Reverse given linked list</li>
    <li>loop through reversed linked list</li>
    <li>add 1 to node's data, and update carry if there is , other wise break and reverse again and return new linked list</li>
    <li>if there is any carry in previous, move to next node and add carry to node's data</li>
    <li>repeat above steps untill last node</li>
    <li>after all steps, reverse the newly linked list</li>
    <li>Still if there is any carry, insert new node with carry as data at head, update new node as head</li>
    <li>return new head</li>
</ul>

```python
def iterative(head):
    temp=head
    carry=1
    head1=reverse(temp)
    temp1=head1
    while temp1:
        s=temp1.data+carry
        if(s<10):
            temp1.data=s
            temp1=temp1.next
            carry=0
            break
        else:
            temp1.data=s%10
            temp1=temp1.next
            carry=s//10
    head2=reverse(head1)
    if(carry!=0):
        new=Node(carry)
        new.next=head2
        return new
    return head2
```

<p>TC : O(3*N)</p>
<p>SC : O(1)</p>

<p><strong>Recursive Solution</strong></p>
<p>Same above iterative solution can be done in recursive backtracking as follows</p>
<p>Helper will move towards last of linked list, when it reaches last node it return 1</p>
<p>During back tracking, it add's 1 and return's new carry</p>
<p>New carry will be returne to its upcoming node's</p>
<p>if final recursibe call return carry, new node will be created and inserts at head</p>

```python
def helper(node):
    if(node==None):
        return 1
    carry=helper(node.next)
    s=node.data+carry
    if(s>=10):
        node.data=s%10
        return s//10
    else:
        node.data=s
        return 0

def recursive(head):
    carry=helper(head)
    if(carry!=0):
        new=Node(carry)
        new.next=head
        return new
    return head
```

<p>TC : O(N)</p>
<p>SC : O(N)</p>


<h2>Find Intersection Of Node In Two Linked List</h2>
<p>Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.</p>
<p><strong>Example 1:</strong></p>
<p>Input:</p>
<p>List 1 = [1,3,1,2,4], List 2 = [3,2,4]</p>
<p>Output: 2</p>
<p>Explanation: Here, both lists intersecting nodes start from node 2.</p>
<img src="https://lh5.googleusercontent.com/4WJ3tjiiLLRYeZOXd_o4BtSYdlsSnOwWKxTGIRW8qQfW9gFymPC710FCgiIrB6vTwwa-hR5WrtWjKOk-beBhD9WtH4nFi16W4f42FQAS0PTXiD_1LmPQYzwmn_eE2OChjKVGRVTy">

<p><strong>Example 2:</strong></p>
<p>Input:</p>
<p> List1 = [1,2,7], List 2 = [2,8,1]</p>
<p>Output: None</p>
<p>Explanation: Here, both lists do not intersect and thus no intersection node is present..</p>
<img src="https://lh6.googleusercontent.com/BYrRaBAIP_iu_ygjCZ14mXh0_yjNCD0tqzptMI4A1L_iH2wJUlBkOBmSTL_npJcRV9zqhNcvgDCZ6i8kOFqFTuQw0AZsZJrggdjOeA0PwRbE_JkQLCfEAWQwEdDKaoYo2lZYYQhJ">

<p><strong>Solution : </strong></p>
<p>We have given two linked lists and there are common nodes between two nodes</p>
<p>We have to find first common node between two lists</p>
<p>We can solve this problem in several ways</p>
<p><strong>BruteForce Approach</strong></p>
<p>Since we need to find common node in two list</p>
<p>In this approach, first we will iterate through linked list and store each node in a hashset </p>
<p>Then, we will iterate through second list, if node exist in hashset, then return that node</p>

```python
def checkIntersection(head1,head2):
    check={}
    temp1=head1
    while temp1:
        check[temp1]=1
        temp1=temp1.next
    temp2=head2
    while temp2:
        if(check.get(temp2)):
            return temp2
        temp2=temp2.next
    return None
```

<p>Time Complexity: O(n+m)</p>
<p>Space Complexity: O(n)</p>

<p><strong>Optimized Approach : </strong></p>
<p>In this approach, we will compare nodes of each linked list one by one , if both nodes are equal then return that node</p>
<p>If both linked list length is equal, then it will work fine</p>
<p>If length is unequal, we have to modify head of larger linked list such that both linked list points to same length from head to tail </p>
<ul>
    <li>Find length of two linked lists, length1 and length2</li>
    <li>If lenght1 > length2, the move head to (length1-length2) nodes a head</li>
    <li>If lenght2 > length1, the move head to (length2-length1) nodes a head</li>
    <li>Then, compare nodes of each linkedlist nodes simultaneously</li>
    <li>If any node matches, return that node</li>
    <li>Otherwise, return None</li>
</ul>

```python
def checkIntersectionByLength(head1,head2):
    temp1,temp2=head1,head2
    length1,length2=0,0
    while temp1:
        length1+=1
        temp1=temp1.next
    while temp2:
        length2+=1
        temp2=temp2.next
    temp1,temp2=head1,head2
    if(length1>length2):
        diff=length1-length2
        temp1=head1
        for i in range(diff):
            temp1=temp1.next
    else:
        diff=length2-length1
        for i in range(diff):
            temp2=temp2.next
    while temp1 and temp2:
        if(temp1==temp2):
            return temp1
        temp1=temp1.next
        temp2=temp2.next
    return None
```

<p>Time Complexity:O(2max(length of list1,length of list2))+O(abs(length of list1-length of list2))+O(min(length of list1,length of list2))</p>
<p>Space Complexity: O(1)</p>

<p><strong>More Optimized Approach</strong></p>
<p>The difference of length method requires various steps to work on it. Using the same concept of difference of length, a different approach can be implemented. The process is as follows</p>
<p>Take two dummy nodes for each list. Point each to the head of the lists.</p>
<p>Iterate over them. If anyone becomes null, point them to the head of the opposite lists and continue iterating until they collide</p>

```python
def Optimized(head1,head2):
    temp1,temp2=head1,head2
    while temp1 or temp2:
        if(temp1==temp2):
            return temp1
        if(not temp1):
            temp1=head2
            temp2=temp2.next
        elif(not temp2):
            temp2=head1
            temp1=temp1.next
        else:
            temp1=temp1.next
            temp2=temp2.next
    return None
```

<p>Time Complexity: O(2*max(length of list1,length of list2))</p>
<p>Space Complexity: O(1)</p>

<h2>Find middle element in a Linked List</h2>
<p>Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.</p>
<p><strong>Examples:</strong></p>
<p>Input Format:</p>
<p>head = [1,2,3,4,5]</p>
<p>Result: [3,4,5]</p>
<p>( As we will return the middle of Linked list the further linked list will be still available )</p>
<img src="https://lh3.googleusercontent.com/Nh8QGhV2tdZq2-b9V86tQR2b0bYxOCB2NMVlFd1YigmGwSqDxE9P0Q-r6zyXP2-YwPTGUrgV0kZkVYlxNT3wpbELp_tEP_oRCegnMgQkmp1s_Qb2BOKs6u8gwlgXi22d5mPPoBI=s1600">

<p><strong>Examples:</strong></p>
<p>Input Format:</p>
<p>head = [1,2,3,4,5,6]</p>
<p>Result: [4,5,6]</p>
<p>Since the list has two middle nodes with values 3 and 4, we return the second one.</p>
<img src="https://lh5.googleusercontent.com/9QyPDwavzA0TolikO5HqpOoDGt6A6DoUSh2XxipWi75jq2LBcG_lfCKONN0R2Zg9_50gfIZb0L6nI-dPV18AQ5JnbbcWWg2SLg_uikAbiSpAz3YkkQ888ClptZ731OLwGyApkDo=s1600">

<p><strong>Solution : </strong></p>
<p>We can solve this problem in several ways</p>

<p><strong>BruteForce : </strong></p>
<p>Find the length of linked list</p>
<p>now loop through linked list for length//2</p>
<p>then we can reach to middle node</p>

```python
def bruteForce(head):
    cnt=0
    temp=head
    while temp:
        cnt+=1
        temp=temp.next
    temp1=head
    for i in range(cnt//2):
        temp1=temp1.next
    return temp1
```

<p>TC : O(N+(N/2)</p>
<p>SC : O(1)</p>

<p><strong>Optimized Solution : </strong></p>
<p>Here we can use Tortoise and Hare Algorithm</p>
<p>In this Approach, We will define two pointer slow and fast , initialize with head of linked list</p>
<p>loop untill fast pointer moves to end</p>
<p>In every iteration, move slow to next node and fast two nodes ahead</p>
<p>Since, fast pointer moved double with slow pointer</p>
<p>When fast pointer reached end, slow pointer points to middle of node</p>

```python
def optimized(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
```

<p>TC : O(N/2)</p>
<p>SC : O(1)</p>

<h2>Detect a cycle in singly linked list</h2>
<p>You are given a Singly Linked List of integers. Return true if it has a cycle, else return false.</p>
<p>A cycle occurs when a node's next points back to a previous node in the list.</p>

<p>Input Format:</p>
<p>LL: 1 2 3 4 5</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/12/Screenshot-2023-12-17-at-7.45.34-PM_red_border-1024x450.png">
<p>Result: True</p>
<p>Explanation: The last node with the value of 5 has its 'next' pointer pointing back to a previous node with the value of 3. This has resulted in a loop, hence we return true.</p>

<p>Input Format:</p>
<p>LL: 1 2 3 4 9 9</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/12/tuxpi.com_.1698730362-1-1024x268.jpg">
<p>Result: False</p>
<p>Explanation: In this example, the linked list does not have a loop hence returns false.</p>

<p><strong>Solution : </strong></p>
<p>We can solve this problem in several ways</p>
<p><strong>BruteForce : </strong></p>
<p>In this approach, we will create visited map, once node visited in traversal we will store it in map</p>
<p>While traversal, we can check whether it is already visited or not</p>
<p>if it visited, we can return true , i.e cycle existed</p>
<p>If traversal complted, no cycle existed</p>

```python
def bruteForce(head):
    visited={}
    temp=head
    while temp:
        if(visited.get(temp)):
            return True
        visited[temp]=1
        temp=temp.next
    return False
```

<p><strong>Optimized Approach : </strong></p>
<p>The previous method uses O(N) additional memory, which can become quite large as the linked list length grows. To enhance efficiency, the Tortoise and Hare Algorithm is introduced as an optimization.</p>
<p>When the tortoise and hare enter the loop, they may be at different positions within the loop due to the difference in their speeds. The hare is moving faster, so it will traverse a greater distance in the same amount of time.</p>
<p>If there is no loop in the linked list, the hare will eventually reach the end, and the algorithm will terminate without a meeting occurring.</p>
<ul>
    <li>create fast,slow pointes and point it to head of linked list</li>
    <li>Start iterating through loop untill fast reaches end</li>
    <ul>
        <li>move fast to two nodes ahead</li>
        <li>move slow a node ahead</li>
        <li>check if slow and fast nodes are same, means cycle exista</li>
    </ul>
    <li>if fast reaches end, means no cycle exists</li>
</ul>

```python
def optimized(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return True
    return False
```

<p>Time Complexity: O(N), where N is the number of nodes in the linked list. This is because in the worst-case scenario, the fast pointer, which moves quicker, will either reach the end of the list (in case of no loop) or meet the slow pointer (in case of a loop) in a linear time relative to the length of the list.</p>
<p>The key insight into why this is O(N) and not something slower is that each step of the algorithm reduces the distance between the fast and slow pointers (when they are in the loop) by one. Therefore, the maximum number of steps needed for them to meet is proportional to the number of nodes in the list.</p>
<p>Space Complexity : O(1) The code uses only a constantamount of additionalspace, regardless of the linked list's length. This is achieved by using two pointers (slow and fast) to detect the loop without any significant extra memory usage, resulting in constantspace complexity, O(1).</p>