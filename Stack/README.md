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
            raise IndexError("StackUnderFlow : Stack is Empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("StackUnderFlow : Stack is Empty")
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

<h2>Design A Min Stack</h2>
<p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>
<p>Implement the MinStack class:</p>
<ul>
    <li>MinStack() initializes the stack object.</li>
    <li>void push(int val) pushes the element val onto the stack.</li>
    <li>void pop() removes the element on the top of the stack.</li>
    <li>int top() gets the top element of the stack.</li>
    <li>int getMin() retrieves the minimum element in the stack</li>
</ul>
<p>You must implement a solution with O(1) time complexity for each function.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in two approaches</p>
<p>In this problem, we have to develop a stack data structure that supports retrieving the minimum element in constant time, along with the standard stack operations like push, pop, and top.</p>


<p><strong>Approach-1 (Uses Extra Space)</strong></p>
<p>By storing the current minimum value along with each element in the stack, we ensure that we can always retrieve the minimum value in constant time, even after popping elements from the stack. This approach efficiently maintains the minimum value without requiring additional complex operations.</p>
<ul>
    <li><strong>Stack with Tuples:</strong>
        <ul>
            <li>We use a stack where each element is a tuple <code>(value, current_minimum)</code>.</li>
            <li>The <code>value</code> is the actual value pushed onto the stack.</li>
            <li>The <code>current_minimum</code> is the minimum value in the stack up to that point.</li>
        </ul>
    </li>
    <li><strong>Pushing Elements:</strong>
        <ul>
            <li>When you push a new element onto the stack, you need to update the minimum value.</li>
            <li>If the stack is empty, the current minimum is the new element itself.</li>
            <li>If the stack is not empty, the current minimum is the smaller value between the new element and the current minimum from the top of the stack.</li>
        </ul>
    </li>
    <li><strong>Popping Elements:</strong>
        <ul>
            <li>When you pop an element from the stack, you remove the top element (both the value and the current minimum).</li>
            <li>The previous element in the stack will have the correct current minimum for the remaining stack.</li>
        </ul>
    </li>
    <li><strong>Getting the Top Element:</strong>
        <ul>
            <li>The <code>top</code> method returns the value of the top element in the stack.</li>
        </ul>
    </li>
    <li><strong>Getting the Minimum Element:</strong>
        <ul>
            <li>The <code>getMin</code> method returns the current minimum, which is stored as the second value in the top element of the stack.</li>
        </ul>
    </li>
</ul>

```python
class MinStack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        return self.stack[-1][0]

    def getMin(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        return self.stack[-1][1]

    def push(self, data):
        if self.isEmpty():
            mini = data
        else:
            mini = min(data, self.getMin())
        self.stack.append((data, mini))

    def pop(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        return self.stack.pop()[0]

    def size(self):
        return len(self.stack)

# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Returns -3
min_stack.pop()
print(min_stack.top())     # Returns 0
print(min_stack.getMin())  # Returns -2
print(min_stack.size())    # Returns 2
```

<p><strong>Approach-2 (Efficient)</strong></p>
<p>1. <strong>Stack and Minimum:</strong></p>
<ul>
    <li>We use a single stack to store elements.</li>
    <li>We keep track of the current minimum value in a separate variable called <strong>min</strong>.</li>
</ul>
<p>2. <strong>Pushing Elements:</strong></p>
<ul>
    <li>When pushing an element, if it’s greater than or equal to the current minimum, it is pushed directly onto the stack.</li>
    <li>If the element is smaller than the current minimum, we push a transformed value (<strong>2*data - min</strong>) onto the stack and update the minimum to this new element. This transformation helps us track the minimum correctly.</li>
</ul>
<p>3. <strong>Popping Elements:</strong></p>
<ul>
    <li>When popping an element, if the popped value is greater than or equal to the current minimum, we simply pop it.</li>
    <li>If the popped value is less than the current minimum, we retrieve the original minimum value by reversing the transformation and update the minimum.</li>
</ul>
<p>4. <strong>Getting the Top Element:</strong></p>
<ul>
    <li>To get the top element, if the top value is less than the current minimum, it means the current minimum is the top element.</li>
</ul>
<p>5. <strong>Getting the Minimum Element:</strong></p>
<ul>
    <li>The <strong>getMin</strong> method simply returns the current minimum value.</li>
</ul>
<p><strong>Example</strong></p>
<p>Let’s see an example:</p>
<ol>
    <li><strong>Push -2:</strong></li>
    <ul>
        <li>Stack: <code>[-2]</code></li>
        <li>Minimum: <code>-2</code></li>
    </ul>
    <li><strong>Push 0:</strong></li>
    <ul>
        <li>Stack: <code>[-2, 0]</code></li>
        <li>Minimum: <code>-2</code></li>
    </ul>
    <li><strong>Push -3:</strong></li>
    <ul>
        <li>Stack: <code>[-2, 0, -4]</code> (transformed value <code>2*(-3) - (-2) = -4</code>)</li>
        <li>Minimum: <code>-3</code></li>
    </ul>
    <li><strong>Get Min:</strong></li>
    <ul>
        <li>Minimum: <code>-3</code></li>
    </ul>
    <li><strong>Pop:</strong></li>
    <ul>
        <li>Stack: <code>[-2, 0]</code></li>
        <li>Minimum: <code>-2</code></li>
    </ul>
    <li><strong>Top:</strong></li>
    <ul>
        <li>Top: <code>0</code></li>
    </ul>
    <li><strong>Get Min:</strong></li>
    <ul>
        <li>Minimum: <code>-2</code></li>
    </ul>
</ol>


```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        if self.stack[-1] < self.min:
            return self.min
        return self.stack[-1]

    def getMin(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        return self.min

    def push(self, data):
        if self.isEmpty():
            self.min = data
            self.stack.append(data)
        else:
            if data >= self.min:
                self.stack.append(data)
            else:
                temp = 2 * data - self.min
                self.stack.append(temp)
                self.min = data

    def pop(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        y = self.stack.pop()
        if y > self.min:
            return y
        else:
            temp = 2 * self.min - y
            self.min = temp
            return self.min

    def size(self):
        return len(self.stack)

# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Returns -3
min_stack.pop()
print(min_stack.top())     # Returns 0
print(min_stack.getMin())  # Returns -2
print(min_stack.size())    # Returns 2

```

<p>Let's break down the mathematical reasoning behind the transformation used in the <strong>MinStack</strong> to ensure it maintains the minimum element efficiently.</p>

<p><strong>Intuition and Proof</strong></p>

<ul>
    <li><strong>Pushing an Element</strong>
        <ul>
            <li><strong>Condition: x < minEle</strong></li>
            <li>Given that the new element <strong>x</strong> is less than the current minimum <strong>minEle</strong>, we push the value <strong>2x - minEle</strong> onto the stack.</li>
            <li>This transformed value will always be less than <strong>x</strong>.</li>
            <li><strong>Proof: 2x - minEle < x</strong></li>
            <li>Starting from the condition <strong>x < minEle</strong>, subtract <strong>minEle</strong> from both sides:
                <ul>
                    <li>x - minEle < 0</li>
                </ul>
            </li>
            <li>Add <strong>x</strong> to both sides:
                <ul>
                    <li>x - minEle + x < x</li>
                </ul>
            </li>
            <li>Simplify the left side:
                <ul>
                    <li>2x - minEle < x</li>
                </ul>
            </li>
            <li>This inequality shows that <strong>2x - minEle</strong> is always less than <strong>x</strong>, confirming that the transformation keeps the value lower than the new element, which helps in identifying when to update the minimum during popping.</li>
        </ul>
    </li>
</ul>

<ul>
    <li><strong>Popping an Element</strong>
        <ul>
            <li>When popping an element, we check if the top of the stack is less than the current minimum element (<strong>minEle</strong>). If it is, it indicates that the element was transformed during insertion, and we need to update the minimum value.</li>
            <li><strong>Retrieving the Previous Minimum</strong></li>
            <li>Let <strong>y</strong> be the popped value.</li>
            <li>If <strong>y < minEle</strong>, it means <strong>y</strong> was transformed and pushed as <strong>2x - prevMinEle</strong>, where <strong>prevMinEle</strong> was the minimum before <strong>x</strong> was pushed.</li>
            <li>The value of <strong>x</strong> was then set as the new <strong>minEle</strong>.</li>
            <li><strong>Proof: Updating minEle</strong></li>
            <li>From the transformation:
                <ul>
                    <li>y = 2x - prevMinEle</li>
                </ul>
            </li>
            <li>Since <strong>minEle = x</strong> (the value of <strong>x</strong> was set as the new minimum when it was pushed):
                <ul>
                    <li>minEle = x</li>
                </ul>
            </li>
            <li>To find the previous minimum, use the current minimum (<strong>minEle</strong>) and the popped value (<strong>y</strong>):
                <ul>
                    <li>newMinEle = 2 × minEle - y</li>
                </ul>
            </li>
            <li>Substitute <strong>y</strong> with <strong>2x - prevMinEle</strong>:
                <ul>
                    <li>newMinEle = 2 × x - (2x - prevMinEle)</li>
                </ul>
            </li>
            <li>Simplify:
                <ul>
                    <li>newMinEle = 2x - 2x + prevMinEle</li>
                    <li>newMinEle = prevMinEle</li>
                </ul>
            </li>
            <li>This ensures that when an element is popped and is less than the current minimum, the minimum value is correctly updated to the previous minimum.</li>
        </ul>
    </li>
</ul>

<p><strong>Summary</strong></p>

<ul>
    <li>When pushing a value <strong>x</strong> less than the current minimum (<strong>minEle</strong>), the value <strong>2x - minEle</strong> is pushed, and the minimum is updated to <strong>x</strong>.</li>
    <li>When popping a value <strong>y</strong> less than the current minimum, the previous minimum is recalculated using:
        <ul>
            <li>newMinEle = 2 × minEle - y</li>
        </ul>
    </li>
</ul>

<p>This approach ensures the stack can keep track of the minimum element efficiently while using a single stack.</p>


