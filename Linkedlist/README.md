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