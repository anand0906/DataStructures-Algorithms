<h1>Stack</h1>
<p>A stack is a linear data structure that follows the <strong>Last In, First Out (LIFO) principle</strong>.</p>
<p>This means that the last element added to the stack will be the first one to be removed.</p>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240606180735/Stack-representation-in-Data-Structures-(1).webp">
<h2>Characteristics of a Stack</h2>
<ul>
	<li><strong>LIFO :</strong> The most recently added element is the first to be removed.</li>
	<li><strong>Oprations :</strong></li>
	<ul>
		<li><strong>PUSH :</strong>Add an element to the top of the stack.</li>
		<li><strong>POP :</strong>Remove the element from the top of the stack.</li>
		<li><strong>PEEK/TOP :</strong>View the top element without removing it.</li>
		<li><strong>ISEMPTY :</strong>Check if the stack is empty.</li>
		<li><strong>SIZE :</strong>Get the number of elements in the stack.</li>
	</ul>
</ul>
<h2>Applications</h2>
<p>Stacks are used in various applications, such as:</p>
<ul>
	<li><strong>Function Call Management :</strong>When a function is called in a program, the current context is pushed onto the call stack. When the function returns, the context is popped from the stack and execution resumes at the previous location.</li>
	<li><strong>Expression Evaluation :</strong>Stacks are used to evaluate expressions and handle parentheses.</li>
	<li><strong>Undo Mechanisms :</strong>Many applications use stacks to implement undo functionality.</li>
	<li><strong>Backtracking Algorithms :</strong>Algorithms like depth-first search (DFS) use stacks to remember their state.</li>
	<li><strong>Browser Tabs :</strong>Some web browsers manage open tabs using a stack. The most recently opened tab is the first one to be closed when you close tabs one by one.</li>
	<li><strong>Browser History :</strong>Web browsers use a stack to keep track of the pages you've visited. The last page you visited is at the top of the stack, and when you click the back button, you go to the previous page, effectively popping the current page off the stack.</li>
</ul>
<h2>Understaning Stacks Practically</h2>
<p>There are many real-life examples of a stack. </p>
<ul>
	<li>Consider the simple example of plates stacked over one another in a canteen. The plate which is at the top is the first one to be removed, i.e. the plate which has been placed at the bottommost position remains in the stack for the longest period of time. So, it can be simply seen to follow the LIFO/FILO order.</li>
	<li>When you pile books on a desk, the last book you place on the pile is the first one you take off when you need it.</li>
	<li>When you perform an action in a text editor (like typing or deleting text), it gets pushed onto an undo stack. If you press the undo button, the last action performed is the first one to be undone.</li>
</ul>
<h2>Types Of Stack</h2>
<ul>
	<li><strong>Fixed Size Stack :</strong>As the name suggests, a fixed size stack has a fixed size and cannot grow or shrink dynamically. If the stack is full and an attempt is made to add an element to it, an overflow error occurs. If the stack is empty and an attempt is made to remove an element from it, an underflow error occurs.</li>
	<li><strong>Dynamic Size Stack :</strong>A dynamic size stack can grow or shrink dynamically. When the stack is full, it automatically increases its size to accommodate the new element, and when the stack is empty, it decreases its size. This type of stack is implemented using a linked list, as it allows for easy resizing of the stack.</li>
</ul>
<h2>Operation Of Stack</h2>
<h3>Push</h3>
<p>Adds an item to the stack. If the stack is full, then it is said to be an Overflow condition.</p>
<p><strong>Algorithm For Push</strong></p>
<pre>
	begin
	 if stack is full
	    return
	 endif
	else  
	 increment top
	 stack[top] assign value
	end else
	end procedure	
</pre>
<h3>Pop</h3>
<p>Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.</p>
<p><strong>Algorithm For Pop</strong></p>
<pre>
	begin
	 if stack is empty
	    return -1
	 endif
	 else
	  store value of stack[top]
	  decrement top
	  return value
	 end else
	end procedure	
</pre>
<h3>Peek/Top</h3>
<p>Returns the top element of the stack.</p>
<p><strong>Algorithm For Top</strong></p>
<pre>
	begin 
  		return stack[top]
	end procedure
</pre>
<h3>isEmpty</h3>
<p>Returns true if the stack is empty, else false.</p>
<p><strong>Algorithm For isEmpty</strong></p>
<pre>
	begin
	 if top < 1
	    return true
	 else
	    return false
	end procedure
</pre>

<h2>Implementation Of Stack</h2>
<p>There are two ways to implement a stack</p>
<ul>
	<li>Using Array</li>
	<li>Using Linked List</li>
</ul>

<h3>Implementation of Stack Using Array</h3>
<p>In Python, you can use a list to implement a stack. The list methods append() and pop() make it straightforward to implement stack operations.</p>

```python
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

# Example usage:
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)  # Output: [1, 2, 3]
print(s.pop())  # Output: 3
print(s.peek())  # Output: 2
print(s.size())  # Output: 2
print(s)  # Output: [1, 2]
```

<p><strong>Advantages</strong></p>
<ul>
	<li>Easy to implement.</li>
	<li>Memory is saved as pointers are not involved.</li>
</ul>
<p><strong>Disadvantages</strong></p>
<ul>
	<li>The total size of the stack must be defined beforehand.</li>
	<li>It is not dynamic i.e., it doesn’t grow and shrink depending on needs at runtime. [But in case of dynamic sized arrays like vector in C++, list in Python, ArrayList in Java, stacks can grow and shrink with array implementation as well].</li>
</ul>

<h3>Implementation of stack using linked list</h3>

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.head=None
        self.count=0

    def isEmpty(self):
        return self.head==None

    def push(self,data):
        if(self.head==None):
            self.head=Node(data)
            self.count+=1
        else:
            node=Node(data)
            node.next=self.head
            self.head=node
            self.count+=1

    def pop(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            node=self.head
            self.head=node.next
            node.next=None
            self.count-=1
            return node.data
        
    def peek(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            return self.head.data

    def size(self):
        return self.count

    def display(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<-")
                temp=temp.next
            print()

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Size Of Stack :",stack.size())
print("Peek Of Stack :",stack.peek())
stack.pop()
stack.display()
stack.pop()
stack.push(100)
stack.display()
stack.pop()
stack.display()
```

<p><strong>Advantages</strong></p>
<ul>
	<li>The linked list implementation of a stack can grow and shrink according to the needs at runtime.</li>
	<li>It is used in many virtual machines like JVM.</li>
</ul>
<p><strong>Disadvantages</strong></p>
<ul>
	<li>Requires extra memory due to the involvement of pointers.</li>
	<li>Random accessing is not possible in stack.</li>
</ul>